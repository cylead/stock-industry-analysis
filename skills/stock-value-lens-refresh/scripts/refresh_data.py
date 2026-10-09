#!/usr/bin/env python3
"""Refresh SEC annual facts and/or a full Stooq ZIP into a new database."""
import csv
import argparse
import datetime as dt
import json
import math
from pathlib import Path
import sqlite3
import sys
import tempfile
import time
import zipfile


def replace_prices(connection, archive, cutoff, crosswalk=None, allow_revisions=True):
    from fastfunds.core import normalize_ticker
    from fastfunds.importer import _weekly_rows
    companies = {r[0]: r[1:] for r in connection.execute(
        'SELECT ticker,latest_adjusted_date,cik FROM companies WHERE is_sec_filer=1')}
    audit = {'refreshed': [], 'missing': [], 'emptyPreserved': [], 'stalePreserved': [],
             'incompletePreserved': [], 'identityPreserved': [], 'absentCrosswalkPreserved': [],
             'basisDeferred': [], 'revisedOverlap': []}
    with zipfile.ZipFile(archive) as bundle:
        files = {}
        for item in bundle.infolist():
            if 'stocks' not in item.filename.lower() or not item.filename.lower().endswith('.us.txt'):
                continue
            ticker = normalize_ticker(Path(item.filename).name[:-7])
            if ticker in companies:
                if ticker in files:
                    raise ValueError('Duplicate price files for ' + ticker)
                files[ticker] = item
        for position, ticker in enumerate(sorted(companies), 1):
            if crosswalk is not None:
                if ticker not in crosswalk:
                    audit['absentCrosswalkPreserved'].append(ticker)
                    continue
                if crosswalk[ticker]['cik'] != companies[ticker][1]:
                    audit['identityPreserved'].append({'ticker': ticker, 'oldCik': companies[ticker][1], 'newCik': crosswalk[ticker]['cik']})
                    continue
            if ticker not in files:
                audit['missing'].append(ticker)
                continue
            lines = bundle.read(files[ticker]).decode('utf-8-sig').splitlines()
            if not lines:
                audit['emptyPreserved'].append(ticker)
                continue
            reader = csv.reader(lines)
            header = next(reader, [])
            if '<DATE>' not in header or '<CLOSE>' not in header:
                raise ValueError('Invalid Stooq header for ' + ticker)
            date_column = header.index('<DATE>')
            close_column = header.index('<CLOSE>')
            daily = []
            for row in reader:
                if len(row) <= max(date_column, close_column) or row[date_column] > cutoff.replace('-', ''):
                    continue
                try:
                    raw_date = row[date_column]
                    date = dt.date(int(raw_date[:4]), int(raw_date[4:6]), int(raw_date[6:8]))
                    close = float(row[close_column])
                except ValueError:
                    continue
                if math.isfinite(close) and close > 0:
                    daily.append((date, close))
            rows, latest = _weekly_rows(sorted(daily), max_price_years=25)
            if not rows or (companies[ticker][0] and latest < companies[ticker][0]):
                audit['stalePreserved'].append(ticker)
                continue
            old = dict(connection.execute('SELECT date,adjusted_close FROM price_weekly WHERE ticker=?', (ticker,)))
            new = dict(rows)
            expected_start = dt.date.fromisoformat(latest) - dt.timedelta(days=int(25 * 365.2425))
            missing_dates = [date for date in old if date >= expected_start.isoformat() and date not in new]
            if missing_dates:
                weeks = {dt.date.fromisoformat(date).isocalendar()[:2] for date in new}
                missing_dates = [date for date in missing_dates if dt.date.fromisoformat(date).isocalendar()[:2] not in weeks]
            if missing_dates:
                audit['incompletePreserved'].append({'ticker': ticker, 'missingWeeks': len(missing_dates)})
                continue
            revisions = [abs(close / old[date] - 1) for date, close in rows if date in old and old[date] > 0]
            if revisions and max(revisions) > 0.000001 and not allow_revisions:
                audit['basisDeferred'].append(ticker)
                continue
            if revisions and max(revisions) > 0.000001:
                audit['revisedOverlap'].append({'ticker': ticker, 'maxRelativeChange': max(revisions)})
            connection.execute('DELETE FROM price_weekly WHERE ticker=?', (ticker,))
            connection.executemany('INSERT INTO price_weekly VALUES(?,?,?)', [(ticker, date, close) for date, close in rows])
            connection.execute('UPDATE companies SET latest_adjusted_date=?,price_source=? WHERE ticker=?', (latest, 'Stooq', ticker))
            audit['refreshed'].append({'ticker': ticker, 'beforeCount': len(old), 'afterCount': len(rows), 'latestDate': latest})
            if position % 1000 == 0:
                print('Processed %s/%s price files' % (position, len(companies)), flush=True)
    if not audit['refreshed']:
        raise ValueError('No stock prices refreshed; check the archive format')
    connection.execute('INSERT OR REPLACE INTO import_meta VALUES(?,?)', ('prices_cutoff', cutoff))
    connection.execute('INSERT OR REPLACE INTO import_meta VALUES(?,?)', ('prices_refreshed_at', dt.datetime.now(dt.timezone.utc).isoformat()))
    return audit


def hold_unreconciled_basis(baseline, connection, audit, archive=None):
    """Conservatively hold material price/per-share scale disagreements for review."""
    old = sqlite3.connect(Path(baseline).resolve().as_uri() + '?mode=ro', uri=True)
    held = []
    corroborated = []
    bundle = zipfile.ZipFile(archive) if archive else None
    refreshed_ciks = {r['cik'] for r in audit['refreshed']}
    try:
        revisions = {r['ticker']: r['maxRelativeChange'] for r in audit['prices']['revisedOverlap']}
        for item in audit['prices']['refreshed']:
            ticker = item['ticker']
            if revisions.get(ticker, 0) <= 0.25:
                continue
            overlap = connection.execute(
                'SELECT date,adjusted_close FROM price_weekly WHERE ticker=? ORDER BY date DESC', (ticker,)
            ).fetchall()
            old_prices = dict(old.execute('SELECT date,adjusted_close FROM price_weekly WHERE ticker=?', (ticker,)))
            shared = next(((date, close / old_prices[date]) for date, close in overlap
                           if date in old_prices and old_prices[date] > 0), None)
            if not shared or 0.8 <= shared[1] <= 1.25:
                continue
            cik = old.execute('SELECT cik FROM companies WHERE ticker=?', (ticker,)).fetchone()[0]
            if bundle and cik in refreshed_ciks:
                from fastfunds.importer import _split_events
                payload = json.loads(bundle.read('CIK%010d.json' % cik))
                events = [event for event in _split_events(payload.get('facts', {}).get('us-gaap', {}))
                          if shared[0] < event['date'] <= audit['cutoff']
                          and (event.get('filed') or '') <= audit['cutoff']]
                ratio = 1.0
                for event in events:
                    ratio *= event['ratio']
                if events and abs((1 / ratio) / shared[1] - 1) <= 0.05:
                    corroborated.append({'ticker': ticker, 'cik': cik, 'events': events})
                    continue
            observations = old.execute(
                'SELECT period_end,diluted_eps,basic_eps,fcf_per_share FROM fundamentals '
                'WHERE cik=? AND period_end<=? ORDER BY period_end DESC', (cik, shared[0])
            ).fetchall()
            for end, *old_values in observations:
                current = connection.execute(
                    'SELECT diluted_eps,basic_eps,fcf_per_share FROM fundamentals WHERE cik=? AND period_end=?',
                    (cik, end)).fetchone()
                if current is None:
                    continue
                ratios = [new / prior for prior, new in zip(old_values, current)
                          if prior and new is not None]
                if not ratios:
                    continue
                if not any(abs(ratio / shared[1] - 1) <= 0.05 for ratio in ratios):
                    held.append({'ticker': ticker, 'cik': cik, 'overlapDate': shared[0],
                                 'priceFactor': shared[1], 'annualPeriod': end, 'perShareFactors': ratios})
                break
        held_ciks = {r['cik'] for r in held}
        held_tickers = set()
        for cik in held_ciks:
            connection.execute('DELETE FROM fundamentals WHERE cik=?', (cik,))
            records = old.execute('SELECT * FROM fundamentals WHERE cik=?', (cik,)).fetchall()
            if records:
                connection.executemany('INSERT INTO fundamentals VALUES(' + ','.join('?' * len(records[0])) + ')', records)
            for record in old.execute('SELECT ticker,latest_adjusted_date,has_basic_eps,has_diluted_eps,has_fcf,has_fcf_per_share,has_dividend_per_share FROM companies WHERE cik=?', (cik,)):
                ticker, latest, *flags = record
                held_tickers.add(ticker)
                connection.execute('DELETE FROM price_weekly WHERE ticker=?', (ticker,))
                connection.executemany('INSERT INTO price_weekly VALUES(?,?,?)', old.execute('SELECT * FROM price_weekly WHERE ticker=?', (ticker,)))
                connection.execute('UPDATE companies SET latest_adjusted_date=?,has_basic_eps=?,has_diluted_eps=?,has_fcf=?,has_fcf_per_share=?,has_dividend_per_share=? WHERE ticker=?', (latest, *flags, ticker))
        audit['prices']['basisUnresolved'] = held
        audit['prices']['basisCorroborated'] = corroborated
        audit['prices']['refreshed'] = [r for r in audit['prices']['refreshed'] if r['ticker'] not in held_tickers]
        audit['refreshed'] = [r for r in audit['refreshed'] if r['cik'] not in held_ciks]
        notes = {ticker: 'Earlier snapshot retained while historical price and annual per-share adjustments are reviewed.'
                 for ticker in held_tickers}
        connection.execute('INSERT OR REPLACE INTO import_meta VALUES(?,?)', ('refresh_notes', json.dumps(notes)))
    finally:
        if bundle:
            bundle.close()
        old.close()


def refresh(baseline, archive, output, importer_project, cutoff, stooq_archive=None, price_cutoff=None, sec_tickers=None):
    baseline, output = Path(baseline).resolve(), Path(output).resolve()
    dt.date.fromisoformat(cutoff)
    if not archive and not stooq_archive:
        raise ValueError('Supply SEC facts and/or Stooq prices')
    price_cutoff = price_cutoff or cutoff
    dt.date.fromisoformat(price_cutoff)
    if price_cutoff > cutoff:
        raise ValueError('Price cutoff cannot exceed the research cutoff')
    if baseline == output or output.exists():
        raise ValueError('Use a new output database path; preserve the baseline')
    sys.path.insert(0, str(Path(importer_project).resolve()))
    from fastfunds.importer import (
        _empty_audit, _insert_fundamental_row, _split_events, extract_fundamentals, load_crosswalk,
    )
    started = time.monotonic()
    audit = {'cutoff': cutoff, 'source': str(Path(archive).resolve()) if archive else None,
             'refreshed': [], 'missing': [], 'noSupportedFacts': [], 'invalidSource': [], 'deferredSplits': []}
    extraction_audit = _empty_audit()
    crosswalk = load_crosswalk(sec_tickers) if sec_tickers else None
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.refresh-', dir=str(output.parent)) as temp:
        candidate = Path(temp) / 'candidate.sqlite3'
        source = sqlite3.connect(baseline.as_uri() + '?mode=ro', uri=True)
        connection = sqlite3.connect(str(candidate))
        try:
            source.backup(connection)
            source.close()
            connection.execute('PRAGMA journal_mode=DELETE')
            connection.execute('PRAGMA foreign_keys=ON')
            with connection:
                if stooq_archive:
                    audit['prices'] = replace_prices(connection, stooq_archive, price_cutoff, crosswalk, bool(archive))
            issuers = connection.execute(
                'SELECT cik,MIN(COALESCE(latest_split_date,latest_adjusted_date)) '
                'FROM companies WHERE is_sec_filer=1 GROUP BY cik ORDER BY cik'
            ).fetchall()
            with connection:
                bundle = zipfile.ZipFile(archive) if archive else None
                members = set(bundle.namelist()) if bundle else set()
                for position, (cik, price_date) in enumerate(issuers if archive else [], 1):
                    member = 'CIK%010d.json' % cik
                    if member not in members:
                        audit['missing'].append(cik)
                        continue
                    payload = json.loads(bundle.read(member))
                    if 'cik' not in payload:
                        audit['invalidSource'].append(cik)
                        continue
                    if int(payload['cik']) != cik:
                        raise ValueError('CIK mismatch in ' + member)
                    for taxonomy in payload.get('facts', {}).values():
                        for concept in taxonomy.values():
                            for unit, facts in concept.get('units', {}).items():
                                concept['units'][unit] = [f for f in facts
                                    if (f.get('filed') or '') <= cutoff
                                    and (f.get('end') or '') <= cutoff]
                    # New split-normalized EPS cannot be paired with the old price basis.
                    events = [e for e in _split_events(payload.get('facts', {}).get('us-gaap', {}))
                              if price_date and price_date < e['date'] <= cutoff]
                    if events:
                        audit['deferredSplits'].append({'cik': cik, 'priceDate': price_date, 'events': events})
                        continue
                    rows = extract_fundamentals(payload, extraction_audit)
                    if not rows:
                        audit['noSupportedFacts'].append(cik)
                        continue
                    before = connection.execute(
                        'SELECT COUNT(*),MAX(period_end) FROM fundamentals WHERE cik=?', (cik,)
                    ).fetchone()
                    connection.execute('DELETE FROM fundamentals WHERE cik=?', (cik,))
                    for row in rows:
                        _insert_fundamental_row(connection, cik, row)
                    audit['refreshed'].append({'cik': cik, 'beforeCount': before[0],
                        'afterCount': len(rows), 'beforeEnd': before[1], 'afterEnd': rows[-1]['period_end']})
                    if position % 500 == 0:
                        print('Processed %s/%s issuers' % (position, len(issuers)), flush=True)
                if bundle:
                    bundle.close()
                if archive and not audit['refreshed']:
                    raise ValueError('No issuers refreshed')
                if archive and stooq_archive:
                    hold_unreconciled_basis(baseline, connection, audit, archive)
                for flag, column in [('basic_eps', 'basic_eps'), ('diluted_eps', 'diluted_eps'),
                                     ('dividend_per_share', 'dividend_per_share'),
                                     ('fcf', 'fcf'), ('fcf_per_share', 'fcf_per_share')]:
                    connection.execute('UPDATE companies SET has_%s=EXISTS('
                        'SELECT 1 FROM fundamentals f WHERE f.cik=companies.cik '
                        'AND f.%s IS NOT NULL)' % (flag, column))
                refreshed_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
                metadata = [('built_at', refreshed_at)]
                if archive:
                    metadata += [('fundamentals_refreshed_at', refreshed_at), ('fundamentals_cutoff', cutoff)]
                for key, value in metadata:
                    connection.execute('INSERT OR REPLACE INTO import_meta VALUES(?,?)', (key, value))
            if connection.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                raise ValueError('Candidate database integrity check failed')
            if connection.execute('PRAGMA foreign_key_check').fetchall():
                raise ValueError('Candidate foreign-key check failed')
            audit['summary'] = {'issuers': len(issuers), 'refreshed': len(audit['refreshed']),
                'missingPreserved': len(audit['missing']), 'unsupportedPreserved': len(audit['noSupportedFacts']),
                'invalidSourcePreserved': len(audit['invalidSource']),
                'splitDeferred': len(audit['deferredSplits']),
                'annualRows': connection.execute('SELECT COUNT(*) FROM fundamentals').fetchone()[0],
                'latestAnnualEnd': connection.execute('SELECT MAX(period_end) FROM fundamentals').fetchone()[0],
                'latestPriceDate': connection.execute('SELECT MAX(date) FROM price_weekly').fetchone()[0]}
        finally:
            source.close()
            connection.close()
        candidate.rename(output)
    audit['elapsedSeconds'] = round(time.monotonic() - started, 2)
    audit['extraction'] = extraction_audit['summary']
    return audit


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', required=True)
    parser.add_argument('--companyfacts-zip')
    parser.add_argument('--stooq-zip')
    parser.add_argument('--price-cutoff')
    parser.add_argument('--sec-tickers', help='Current SEC ticker/exchange list; check issuer identity before price updates')
    parser.add_argument('--output', required=True)
    parser.add_argument('--importer-project', required=True)
    parser.add_argument('--cutoff', required=True)
    parser.add_argument('--audit', required=True)
    args = parser.parse_args()
    if args.stooq_zip and not args.sec_tickers:
        parser.error('--sec-tickers is required for stock-price identity checks')
    result = refresh(args.baseline, args.companyfacts_zip, args.output, args.importer_project, args.cutoff,
                     args.stooq_zip, args.price_cutoff, args.sec_tickers)
    Path(args.audit).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'summary': result['summary'], 'elapsedSeconds': result['elapsedSeconds']}, indent=2))
