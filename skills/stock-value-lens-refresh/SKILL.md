---
name: stock-value-lens-refresh
description: Refresh and verify Stock Value Lens website data from SEC Company Facts and a Stooq US daily archive, including weekly prices and monthly combined snapshots. Use for this website's data maintenance, not Five Forces reports or live quotes.
---

# Stock Value Lens data refresh

Refresh the existing universe, preserve unsupported historical records, verify a candidate, and publish when the user's request authorizes updating the public site. This skill does not authorize purchases, account creation or unrelated changes.

## Locations

- Website: `/Users/yangch/Downloads/investment/stock-valuation-public`.
- Annual extraction rules: `/Users/yangch/Downloads/investment/stock data website/fastfunds/importer.py`. Reuse them; do not create a second EPS/FCF methodology.
- Initial baseline: the original project's `app_data/fastfunds.sqlite3`.
- Subsequent baseline: the database recorded in the website's `data_hand_download/current-refresh.json`. Resolve relative paths against the website and verify existence.
- Versioned skill: `/Users/yangch/Downloads/investment/stock industry analysis/skills/stock-value-lens-refresh`.

Read applicable `AGENTS.md` files. The website has no Git repository; version the skill and compact release evidence in the analysis repository. Keep archives, databases and generated website assets out of it.

## Inputs

Inspect the current dates and coverage; capture hashes of authored files that will change to protect concurrent edits. Download the current [SEC ticker/exchange list](https://www.sec.gov/files/company_tickers_exchange.json), and, for a combined refresh, the [SEC Company Facts ZIP](https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip). Identify automated requests with an application/contact `User-Agent`, using the website's established public corrections contact. Retain download time, URL, HTTP Last-Modified and checksum. SEC publishes the ZIP nightly; not every issuer has supported annual facts. See [SEC API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).

Obtain the **US daily TXT ZIP** from [Stooq historical downloads](https://stooq.com/db/h/). The established manual-download path is the website's `data_hand_download/d_us_txt.zip`. Validate ZIP members `...stocks/.../*.us.txt`, `<DATE>/<CLOSE>` columns and sampled endpoints. On 2026-10-09, scripted requests returned browser-verification HTML with HTTP 200 and the in-app browser could not reach downloads; the user's normal browser download worked. Ask for a local archive when needed and continue SEC work meanwhile. Do not bypass verification or treat HTML as CSV. Preserve a dated copy before a later download replaces that filename.

A new price provider must support the required history, adjustment basis, public display and CSV use. Technical retrieval does not establish those rights. Do not silently substitute Yahoo or splice differently adjusted histories.

## Candidate workflow

Use a fresh working directory and a new output database. The bundled `scripts/refresh_data.py` copies the baseline read-only, reads ZIPs directly, reuses the original annual extractor/weekly sampling, and checks integrity. It preserves the ticker universe rather than automatically adding IPOs or migrating identities.

Choose a financial cutoff supported by the retrieved archive and a price cutoff no later than a **completed** US session present in the price archive. The first run used 2026-10-09 and 2026-10-08; choose new dates for future runs.

Combined example, using task-specific paths and this skill's directory as `SKILL_DIR`:

```sh
python3 "$SKILL_DIR/scripts/refresh_data.py" \
  --baseline "$BASELINE" --companyfacts-zip "$SEC_ZIP" \
  --stooq-zip "$STOOQ_ZIP" --sec-tickers "$SEC_TICKERS" \
  --importer-project '/Users/yangch/Downloads/investment/stock data website' \
  --cutoff YYYY-MM-DD --price-cutoff YYYY-MM-DD \
  --output "$WORK/candidate.sqlite3" --audit "$WORK/refresh-audit.json"
```

- **Monthly:** supply both archives. Prices refresh before fundamentals, aligning later split-normalized EPS with the newer price basis.
- **Weekly prices:** omit `--companyfacts-zip` only with the helper's adjustment-basis guard. Stocks with changed overlapping historical adjustments are held. Resolve these deferrals with current SEC data in a combined refresh; do not remove the guard to improve freshness counts.
- Supply the current SEC ticker list for price updates. Identity conflicts, absent mappings, missing/empty/stale/incomplete histories remain historical. Missing/unsupported SEC facts remain historical; post-price splits defer fundamentals. Review every audit category rather than assuming the maximum price date applies to all stocks.
- Combined refreshes also screen material adjustment changes: latest overlapping prices outside a 0.8–1.25 scale factor must reconcile within 5% with a common annual per-share factor or current SEC standard split facts, or the prior issuer snapshot is held. This is a conservative screening proxy that can hold valid restatements, not proof of wrong reported facts. Review `basisUnresolved` and `basisCorroborated`; retained snapshots carry a public explanation.
- Retain annual 10-K/10-K/A and existing US-GAAP coverage. Do not add quarterly/TTM data, IFRS extraction, forecasts, split-only prices or securities as part of a routine refresh.

Run bundled tests with `FASTFUNDS_IMPORTER_PROJECT` set to the original project: `python3 -m unittest discover -s "$SKILL_DIR/scripts" -p 'test_refresh.py' -v`. Run website `npm test` after relevant exporter/documentation changes.

Compare baseline/candidate company and CIK coverage, prices/period counts, endpoints, weekly uniqueness, historical overlap revisions, rolling 25-year retention, new annual periods, restatements, metric availability and filing dates. Investigate unexplained losses of supported facts. Check AAPL, MSFT, NVDA, CPRT, BRK-B, a bank, a loss-maker and a split issuer when relevant. Confirm source preservation and no values beyond cutoffs. P/E and reference lines are calculated from inputs, not fetched from another P/E website.

Export into a staged website using `scripts/export_data.py --db "$WORK/candidate.sqlite3"`, then `SITE_URL=https://stockvaluelens.com npm run build`. Keep an independent pre-release backup before repeated builds: the exporter/build retain only their preceding output. Inspect HTML, JSON, Markdown, catalog/source dates, chart ranges and CSV behavior. Replace obsolete hard-coded dates in authored sources; never edit `dist/` directly. Retain adjusted-price and annual-EPS timing disclosures.

## Publish and record

When checks pass and publication is authorized, retain dated inputs/database/audit under `data_hand_download/`, write `current-refresh.json`, install validated data and authored changes, and deploy with the existing Cloudflare configuration. Update website README, `PROJECT_LOG.md`, applicable `ISSUE_LOG.md`, `VERIFICATION.md` and `content/updates.json` with actual results. Preserve the prior data/build or a documented Cloudflare rollback version.

Verify deployment version and representative live bytes against the build, then the live chart endpoint/P/E view. Distinguish publication date, SEC retrieval/cutoff, fiscal periods, price cutoff and individual endpoints. Disclose exceptions. Preserve local results and report exact blockers on failure. Commit/push only authorized analysis-repository files under its standing instructions.

Record input sizes, runtime, freshness coverage, deferrals and human steps. Prefer the tested full-archive workflow until a permitted reliable incremental feed is available. Pure append-only refresh misses corporate actions and corrections; future date-range APIs need overlap replacement, split handling and periodic reconciliation.

Do not schedule recurring work merely because the user requests an on-demand update or reusable skill. Schedule only when requested; do not call a browser-dependent price download unattended. Finish with published dates, material exceptions, the skill link and actual commit/push outcome.
