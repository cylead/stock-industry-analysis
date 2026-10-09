import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parent
IMPORTER = Path(os.environ.get('FASTFUNDS_IMPORTER_PROJECT', '/Users/yangch/Downloads/investment/stock data website'))
sys.path.insert(0, str(IMPORTER))
from fastfunds.importer import SCHEMA
spec = importlib.util.spec_from_file_location('refresh_data', ROOT / 'refresh_data.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def payload(cik, split=False):
    facts = {'EarningsPerShareDiluted': {'units': {'USD/shares': [
        {'start': '2024-01-01', 'end': '2024-12-31', 'val': 2, 'form': '10-K', 'fp': 'FY', 'filed': '2025-02-01'},
        {'start': '2025-01-01', 'end': '2025-12-31', 'val': 3, 'form': '10-K', 'fp': 'FY', 'filed': '2026-02-01'},
        {'start': '2025-01-01', 'end': '2025-12-31', 'val': 99, 'form': '10-K/A', 'fp': 'FY', 'filed': '2026-11-01'},
    ]}}}
    if split:
        facts['StockholdersEquityNoteStockSplitConversionRatio1'] = {'units': {'pure': [
            {'end': '2026-06-01', 'val': 2, 'filed': '2026-06-02'}]}}
    return {'cik': cik, 'facts': {'us-gaap': facts}}


class RefreshTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.baseline = self.root / 'baseline.sqlite3'
        self.output = self.root / 'new.sqlite3'
        self.archive = self.root / 'facts.zip'
        with sqlite3.connect(self.baseline) as c:
            c.executescript(SCHEMA)
            c.execute("INSERT INTO import_meta VALUES('built_at','old')")
            for cik in [1, 2]:
                ticker = 'TEST%s' % cik
                c.execute("INSERT INTO companies(ticker,cik,name,exchange,stooq_path,is_sec_filer,latest_adjusted_date) VALUES(?,?,?,'Nasdaq','raw',1,'2026-05-08')", (ticker, cik, ticker))
                c.execute("INSERT INTO fundamentals(cik,period_end,fiscal_year,diluted_eps) VALUES(?,'2024-12-31',2024,1)", (cik,))
                c.execute("INSERT INTO price_weekly VALUES(?,'2026-05-08',100)", (ticker,))
        c.close()
        self.before = hashlib.sha256(self.baseline.read_bytes()).hexdigest()

    def tearDown(self):
        self.temp.cleanup()

    def write_archive(self, items):
        with zipfile.ZipFile(self.archive, 'w') as z:
            for cik, value in items.items():
                z.writestr('CIK%010d.json' % cik, json.dumps(value))

    def run_refresh(self):
        return module.refresh(self.baseline, self.archive, self.output, IMPORTER, '2026-10-09')

    def test_corrections_cutoff_missing_issuer_and_read_only_prices(self):
        self.write_archive({1: payload(1)})
        audit = self.run_refresh()
        self.assertEqual(audit['missing'], [2])
        with sqlite3.connect(self.output) as c:
            self.assertEqual(c.execute('SELECT period_end,diluted_eps FROM fundamentals WHERE cik=1 ORDER BY period_end').fetchall(), [('2024-12-31', 2), ('2025-12-31', 3)])
            self.assertEqual(c.execute('SELECT diluted_eps FROM fundamentals WHERE cik=2').fetchone()[0], 1)
            self.assertEqual(c.execute('SELECT * FROM price_weekly ORDER BY ticker').fetchall(), [('TEST1', '2026-05-08', 100), ('TEST2', '2026-05-08', 100)])
            self.assertEqual(c.execute('SELECT has_diluted_eps FROM companies WHERE cik=1').fetchone()[0], 1)
        self.assertEqual(hashlib.sha256(self.baseline.read_bytes()).hexdigest(), self.before)
        with self.assertRaises(ValueError):
            self.run_refresh()

    def test_post_price_split_preserves_old_basis(self):
        self.write_archive({1: payload(1, split=True), 2: payload(2)})
        audit = self.run_refresh()
        self.assertEqual(audit['deferredSplits'][0]['cik'], 1)
        with sqlite3.connect(self.output) as c:
            self.assertEqual(c.execute('SELECT diluted_eps FROM fundamentals WHERE cik=1').fetchall(), [(1,)])

    def test_identity_failure_preserves_baseline_and_no_output(self):
        self.write_archive({1: payload(99)})
        with self.assertRaisesRegex(ValueError, 'CIK mismatch'):
            self.run_refresh()
        self.assertFalse(self.output.exists())
        self.assertEqual(hashlib.sha256(self.baseline.read_bytes()).hexdigest(), self.before)

    def test_full_price_replacement_cutoff_and_missing_ticker(self):
        price_archive = self.root / 'prices.zip'
        with zipfile.ZipFile(price_archive, 'w') as z:
            z.writestr('data/daily/us/nasdaq stocks/1/test1.us.txt',
                '<TICKER>,<DATE>,<CLOSE>\nTEST1.US,20260508,100\nTEST1.US,20261008,60\nTEST1.US,20261009,99\n')
            z.writestr('data/daily/us/nasdaq etfs/1/test2.us.txt',
                '<TICKER>,<DATE>,<CLOSE>\nTEST2.US,20261008,5\n')
        audit = module.refresh(self.baseline, None, self.output, IMPORTER, '2026-10-09', price_archive, '2026-10-08')
        self.assertEqual(audit['prices']['missing'], ['TEST2'])
        with sqlite3.connect(self.output) as c:
            self.assertEqual(c.execute('SELECT date,adjusted_close FROM price_weekly WHERE ticker="TEST1" ORDER BY date').fetchall(), [('2026-05-08', 100), ('2026-10-08', 60)])
            self.assertEqual(c.execute('SELECT diluted_eps FROM fundamentals WHERE cik=1').fetchone()[0], 1)
        self.assertEqual(hashlib.sha256(self.baseline.read_bytes()).hexdigest(), self.before)

    def test_combined_refresh_aligns_split_basis_and_rejects_html(self):
        with sqlite3.connect(self.baseline) as c:
            c.execute('UPDATE fundamentals SET diluted_eps=2 WHERE cik=1')
        price_archive = self.root / 'prices.zip'
        with zipfile.ZipFile(price_archive, 'w') as z:
            z.writestr('data/daily/us/nasdaq stocks/1/test1.us.txt',
                '<TICKER>,<DATE>,<CLOSE>\nTEST1.US,20260508,50\nTEST1.US,20261008,60\n')
        self.write_archive({1: payload(1, split=True)})
        audit = module.refresh(self.baseline, self.archive, self.output, IMPORTER, '2026-10-09', price_archive, '2026-10-08')
        self.assertEqual(audit['deferredSplits'], [])
        with sqlite3.connect(self.output) as c:
            self.assertEqual(c.execute('SELECT diluted_eps FROM fundamentals WHERE cik=1 ORDER BY period_end').fetchall(), [(1,), (1.5,)])
        with zipfile.ZipFile(price_archive, 'w') as z:
            z.writestr('data/daily/us/nasdaq stocks/1/test1.us.txt', '<html>Verification required</html>')
        with self.assertRaisesRegex(ValueError, 'Invalid Stooq header'):
            module.refresh(self.baseline, None, self.root / 'bad.sqlite3', IMPORTER, '2026-10-09', price_archive)
        self.assertFalse((self.root / 'bad.sqlite3').exists())

    def test_combined_unreconciled_scale_holds_original_company(self):
        price_archive = self.root / 'prices.zip'
        with zipfile.ZipFile(price_archive, 'w') as z:
            z.writestr('data/daily/us/nasdaq stocks/1/test1.us.txt', '<DATE>,<CLOSE>\n20260508,1000\n20261008,1100\n')
        self.write_archive({1: payload(1)})
        audit = module.refresh(self.baseline, self.archive, self.output, IMPORTER, '2026-10-09', price_archive)
        self.assertEqual(audit['prices']['basisUnresolved'][0]['ticker'], 'TEST1')
        with sqlite3.connect(self.output) as c:
            self.assertEqual(c.execute('SELECT diluted_eps FROM fundamentals WHERE cik=1').fetchall(), [(1,)])
            self.assertEqual(c.execute('SELECT date,adjusted_close FROM price_weekly WHERE ticker="TEST1"').fetchall(), [('2026-05-08', 100)])

    def test_price_only_holds_revised_basis_and_crosswalk_conflicts(self):
        with sqlite3.connect(self.baseline) as c:
            c.execute("INSERT INTO companies(ticker,cik,name,exchange,stooq_path,is_sec_filer,latest_adjusted_date) VALUES('TEST3',3,'Third','Nasdaq','raw',1,'2026-05-08')")
            c.execute("INSERT INTO price_weekly VALUES('TEST3','2026-05-08',100)")
        price_archive = self.root / 'prices.zip'
        with zipfile.ZipFile(price_archive, 'w') as z:
            for ticker, old in [('TEST1', 50), ('TEST2', 100), ('TEST3', 100)]:
                z.writestr('data/daily/us/nasdaq stocks/1/' + ticker.lower() + '.us.txt',
                    '<DATE>,<CLOSE>\n20260508,%s\n20261008,60\n' % old)
        crosswalk = self.root / 'tickers.json'
        crosswalk.write_text(json.dumps({'fields': ['ticker', 'cik', 'exchange'], 'data': [
            ['TEST1', 1, 'Nasdaq'], ['TEST2', 99, 'Nasdaq'], ['TEST3', 3, 'Nasdaq']]}))
        audit = module.refresh(self.baseline, None, self.output, IMPORTER, '2026-10-09', price_archive, sec_tickers=crosswalk)
        self.assertEqual(audit['prices']['basisDeferred'], ['TEST1'])
        self.assertEqual(audit['prices']['identityPreserved'][0]['ticker'], 'TEST2')
        with sqlite3.connect(self.output) as c:
            self.assertEqual(c.execute('SELECT adjusted_close FROM price_weekly WHERE ticker="TEST1"').fetchall(), [(100,)])
            self.assertEqual(c.execute('SELECT date FROM price_weekly WHERE ticker="TEST3" ORDER BY date').fetchall(), [('2026-05-08',), ('2026-10-08',)])


if __name__ == '__main__':
    unittest.main()
