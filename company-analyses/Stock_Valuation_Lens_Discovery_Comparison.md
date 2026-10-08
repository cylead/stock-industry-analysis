# Stock Valuation Lens: discovery tests, competitor comparison, and improvements

Research date: **2026-10-08**. Website: [Stock Valuation Lens](https://stock-valuation-public.valuationlens.workers.dev/). Informational product research; **not investment advice**.

**Finding: the website has a defensible recommendation use case, but this session did not establish that an assistant can discover and verify it unaided.** It was absent from all ten recorded search result sets, including exact-name and domain-restricted searches. The research fetcher could not read seven supplied URLs. Ordinary browser-user-agent HTTP requests succeeded, demonstrating that access differs by client.

The strongest present positioning is **free historical price-versus-EPS/FCF research, with filing links and exports without an account**. The main weaknesses are discovery, inconsistent machine access, prices ending five months ago, incomplete metric coverage, and a narrower valuation workflow than several competitors. Better wording helps communicate the product; access and data improvements are necessary to broaden the use cases for which it can be recommended.

## 1. What was actually tested

The subject was identified from the existing [SEO proposal](Stock_Valuation_Lens_SEO_Proposal.md). This is a product/discovery audit, not a Porter Five Forces request. Website code, hosting settings, and public copy were not changed.

Ten individual live searches were run through this assistant's web-search tool. Target presence means a URL from the website appeared anywhere in the returned result set. Result sets are not a controlled Google top-ten ranking experiment: provider internals, locale, personalization, and completeness were not controlled. The chat already knew the website, so these searches are **not a blind model-output experiment**. Nevertheless, the unseeded queries did not name it. Full returned result titles/URLs and verification records are preserved in [test evidence](Stock_Valuation_Lens_Discovery_Test_Results.json).

| Test | Exact query | Website returned? | Representative results or observation |
| --- | --- | --- | --- |
| Generic recommendation | `recommend free websites for historical stock financial data and valuation` | No | LionCharts, tool directories, Intrinsiqq comparison article, TIKR article |
| No-account chart intent | `free stock price vs earnings chart no account` | No | MarketFairValue, FSViz, other chart/tracker tools; some results poorly matched the task |
| Export intent | `download historical annual EPS and free cash flow per share CSV free` | No | Pineify, SEC explorer, InvestLog, data/API providers |
| Alternative plus provenance | `free FAST Graphs alternative SEC filings` | No | Primarily SEC filing tools; weak alignment with valuation charts |
| Generic financial chart intent | `free historical stock valuation charts EPS FCF` | No | Chartloom, Intrinsiqq, LionCharts, Stock Rover |
| Alternative intent | `"free FAST Graphs alternative"` | No | Find My Moat's FAST Graphs alternatives page; unrelated results also appeared |
| Company-specific export intent | `"Copart" "EPS" "CSV"` | No | StockTitan, tradmap, Atlantis and other company-data pages |
| Competitor-assisted discovery | `best free historical financial data valuation tools Macrotrends Stock Analysis FinanceCharts` | No | Macrotrends, comparison/directory pages; deliberately seeded competitor names |
| Brand diagnostic | `"Stock Valuation Lens"` | No | Unrelated pages containing stock/valuation/lens language |
| Domain diagnostic | `site:stock-valuation-public.valuationlens.workers.dev` | No | Empty result set |

Observed target retrieval: **0/7 unseeded task queries**, **0/1 competitor-assisted query**, and **0/2 brand/domain diagnostics**. These are retrieval observations, not an estimated LLM recommendation rate. The preliminary combined four-query search also did not return the website, but is excluded from these denominators because its output merged queries.

The research fetcher failed to open the homepage, sources, methodology, Apple HTML, `llms.txt`, Apple Markdown, and Apple JSON. Its error did not identify a cause. Separately, eight HTTP fetches with `Mozilla/5.0` returned **200**, and their bodies matched the local production build byte-for-byte: homepage, sources, methodology, catalog, OTEX JSON, AAPL JSON, data-access page, and `llms.txt`. A request to `llms.txt` identifying as `Python-urllib/3.9` returned **403, error code 1010**. The website already records this access problem as ISSUE-006; these tests corroborate client-dependent access, without proving why the research fetcher itself fails.

The site launched on the research date. Absence from these results does not establish permanent invisibility or exclusion from every search index. The prior release record reports successful sitemap processing and 492 discovered URLs before the 497-URL release; those counts are not indexed-page counts. Search Console was not inspected again in this session.

**Independent ChatGPT, Claude, Gemini, or Perplexity recommendation sessions were not run.** Their spontaneous recommendations, citations, or current fetch success remain unmeasured. No external model-output percentages are claimed.

## 2. Verified coverage: what “x years” can mean

All 6,551 local production company JSON files were inspected. The live catalog and representative AAPL/OTEX JSON matched that build. Coverage counts are by ticker/security, including separate share classes, rather than unique business. Availability means a non-null observation, including zero and negative values; it does not certify every value's accounting suitability or accuracy. Sources: [catalog](https://stock-valuation-public.valuationlens.workers.dev/data/catalog.json), [methodology](https://stock-valuation-public.valuationlens.workers.dev/methodology/), [sources](https://stock-valuation-public.valuationlens.workers.dev/sources/).

| Measure | Observed coverage | Marketing implication |
| --- | --- | --- |
| Searchable securities | 6,551 | Say “search 6,551 US-listed securities”; do not imply all have complete financial history. |
| Dedicated company pages | 485, from a dated 503-security S&P 500 list | Distinguish public company-page coverage from ticker search/JSON coverage. |
| Diluted EPS | Available for 4,180 securities; median 10 distinct stored fiscal-year labels across those securities | Many histories exceed free five-year tiers, but coverage is uneven. |
| FCF per share | Available for 3,661 securities; median 10 distinct stored fiscal-year labels across those securities | Use availability indicators rather than promising FCF for every stock. |
| Longer histories | 1,610 securities have EPS in at least 15 distinct year labels; 1,332 have FCF/share in at least 15 | A stronger, measured claim than implying universal maximum coverage. Distinct labels do not prove consecutive, fully comparable fiscal periods. |
| Published-page histories | EPS: 483 pages, median 18 distinct year labels. FCF/share: 442 pages, median 18 | The existing constituent pages are a good demonstration set. These medians exclude pages without the metric. |
| Maximum annual financial history | OTEX has 20 EPS and 20 FCF/share observations, period ends 2007-06-30 through 2026-06-30 | “Up to 20 annual observations for selected companies” is supportable; this is about 19 elapsed years between endpoints. |
| Price history | 6,542 securities have prices; maximum span 24.99 years; median span 8.26 years | Say “nearly 25 years of weekly price history for selected stocks,” with company-specific dates. |
| Price freshness | Latest stored price: 2026-05-08, 153 days before this audit | Poor fit for current valuations, current quotes, or trading research. |
| Financial snapshot | Database built 2026-08-27; company-specific fiscal periods vary | Build/export/launch dates must remain separate from financial reporting and price dates. |

Concrete examples:

| Company | EPS observations | FCF/share observations | Annual metric period ends | Weekly price endpoints |
| --- | --- | --- | --- | --- |
| [Apple](https://stock-valuation-public.valuationlens.workers.dev/stocks/aapl/) | 19 | 19 | 2007-09-29–2025-09-27 | 2001-05-11–2026-05-08 |
| [Microsoft](https://stock-valuation-public.valuationlens.workers.dev/stocks/msft/) | 19 | 19 | 2008-06-30–2026-06-30 | 2001-05-11–2026-05-08 |
| [Copart](https://stock-valuation-public.valuationlens.workers.dev/stocks/cprt/) | 17 | 17 | 2009-07-31–2025-07-31 | 2005-02-25–2026-05-08 |
| [Autodesk](https://stock-valuation-public.valuationlens.workers.dev/stocks/adsk/) | 19 | 12 | Both metrics span endpoints 2008-01-31–2026-01-31; FCF has gaps | 2001-05-11–2026-05-08 |

Three details need care before strengthening claims:

1. **Rows are not years.** Some tickers have multiple period ends with the same stored fiscal-year label: 135 in the EPS set and 107 in the FCF/share set. Maximum raw row counts are 21 and 22, respectively. Fiscal-calendar changes, 52/53-week conventions, or period-label choices can explain such patterns; this audit does not establish erroneous duplicates. Report period endpoints, observation counts, missing periods, and fiscal labels separately. Do not advertise “22 years of financial history” from 22 rows.
2. **The exported prices are weekly.** The exporter reads `price_weekly` and `split_weekly`; Apple has 1,305 price observations over nearly 25 years. The public data-access documentation's “stored daily observations” wording is inconsistent with the export and should be corrected. This audit made no website edits.
3. **Source authenticity is not universal accuracy.** EPS records retain filing accession, tag, dates, units, and split-adjustment metadata. FCF/share is derived from operating cash flow minus capex, divided by diluted weighted-average shares; the export lacks separate share-denominator provenance. Prices come from Stooq, not SEC filings. No validated split-only US prices are present. These distinctions support “filing-linked financial data,” not “all data audited,” “SEC-sourced prices,” or “100% accurate.” The audit inspected structure and provenance, not every underlying filing.

## 3. Competitor comparison

Peers were chosen for overlapping user tasks. Some appeared directly, others through comparison results, and GNG/FAST Graphs were inspected as close workflow benchmarks already identified in the prior proposal. This is not a ranking of the most frequently recommended tools. Product pages substantiate advertised capabilities and plan limits; competitor calculations and complete datasets were not independently audited.

| Tool | Free access and history verified in inspected sources | Strength relative to your site | Your useful distinction |
| --- | --- | --- | --- |
| **Stock Valuation Lens** | Existing charts and CSV/PNG exports require no account/subscription. Selected histories reach 20 annual observations and nearly 25 years of weekly prices. | Focused historical workflow; inspectable source links and public JSON/Markdown. | Most useful for historical annual per-share research, with explicit dates and limitations. |
| **Stock Analysis** | Public Apple overview displays five annual years plus TTM. Pro advertises 10–40 years and one download/day; $79/year or $9.99/month. [Apple financials](https://stockanalysis.com/stocks/aapl/financials/), [plans](https://stockanalysis.com/pro/). | Fuller statements, ratios, current prices, global coverage and broader research tools. | Longer free annual EPS/FCF histories for many covered stocks; account-free chart exports. This is not a complete financial-statement replacement. |
| **TIKR** | Free account: US coverage, five annual years and eight quarters. Paid tiers expand history/charting and global coverage. [Official pricing](https://www.tikr.com/pricing). | Quarterly data, valuation metrics, estimates, transcripts and broader workflows. | More free annual per-share history for many companies and no signup. Do not generalize this to every metric or ticker. |
| **GNG Research** | Advanced charts are free with a required account. Advertises daily multiples, several financial metrics, estimates, two-company comparisons and saved views. Exact universal history length was not established. [Charting](https://www.gngresearch.com/charting/). | A close free valuation-chart competitor with much broader functionality. | Immediate access, public financial tables and JSON, filing links, and no-account exports. Free valuation charting alone does not distinguish you. |
| **Intrinsiqq** | Pricing specifies five free financial years, ten lookups/day and single-metric five-year charts; deeper history and editable DCF are paid. [Pricing](https://intrinsiqq.com/pricing). | DCF, scoring, comparisons, screening and portfolio tools. | More accessible historical depth for supported companies. Its broad free/no-account marketing should not be read as unrestricted access; explicit plan limits govern this comparison. |
| **LionCharts** | Advertises free, no-registration SEC data and daily-updated ratios. The same page mentions ten-year financial histories and five-year statements; scope is inconsistent, so maximum depth is unverified. [Homepage](https://lioncharts.com/). | Broader screening, quarterly/statement views and advertised freshness. | A narrower, source-linked per-share workflow and demonstrated long histories. No blanket advantage in free access or SEC sourcing. |
| **Pineify growth tool** | Advertises free annual/quarterly EPS, cash-flow and other growth metrics, CSV export, and no registration in its FAQ. Universal maximum history not verified. [Growth tool](https://pineify.app/free-tools/financial-statement-growth). | More growth metrics and quarterly views. | Integrated historical stock-price versus per-share fundamentals, rather than a growth-data lookup alone. |
| **FAST Graphs** | Seven-day trial; paid Basic starts at $15.95/month billed annually. Offers specialized earnings/cash-flow measures; broader tiers add portfolio/screening features. [Official plans](https://www.fastgraphs.com/pricing/). | Broader metric selection, established valuation workflow and specialized financial measures. | Sustained free access to the existing historical tool. Position as a limited alternative for a specific task, with different calculations. |

[Macrotrends](https://www.macrotrends.net/) surfaced in search, but homepage and Apple EPS fetches returned 403. [FinanceCharts](https://www.financecharts.com/) exposed a “100% FREE” footer but required a CAPTCHA for core pages. [StockNest](https://stocknest.app/) appeared through founder posts, but its direct fetch supplied no readable product details. Their exact free history/export limits were not verified and are deliberately excluded from numerical comparison. These results also show that retrieval restrictions are not unique to your site.

**The advantage is a combination, not a unique ingredient:** long annual per-share histories for many covered names, price overlays, traceable financial sources, clear calculation limits, and account-free export/access. Free access, SEC data, and charts each have competing examples.

## 4. When I could recommend the website

After this audit, I would consider it for someone who says: “I want free historical annual EPS and FCF/share, compared with stock prices, with filing links and no signup.” I would disclose the historical snapshot, weekly adjusted prices, varying coverage, and client-access limitation. That is an informed suitability judgment after inspection, not a spontaneous recommendation result.

I would currently favor other tools when the central requirement is current valuation, full income statements/balance sheets, quarterly or TTM data, forecasts, global home-market listings, portfolio monitoring, or reproducible point-in-time backtesting. The orange reference line is retrospective and window-dependent; financial observations newer than the final price can appear in the company table but be excluded from the chart and chart CSV. Its name should not imply intrinsic fair value.

An accurate recommendation sentence an assistant could use is:

> Stock Valuation Lens is a free historical US-stock research tool with annual EPS and derived FCF per share, filing links, price overlays, and CSV/PNG exports without signup. History varies by company, and its price snapshot currently ends May 8, 2026.

## 5. Wording that strengthens verified advantages

Keep the chart prominent, as in the approved design. Place concise evidence beside the existing introduction and relevant company sections. The earlier release already added metadata, source pages, guides, Markdown and JSON; recreating those assets is unnecessary.

Suggested homepage heading:

> Free stock price vs. earnings charts—with filing sources.

Suggested supporting copy:

> Compare annual EPS and free cash flow per share with historical stock prices. Explore nearly 25 years of weekly prices for selected stocks, with company-specific financial coverage and SEC filing links. Charts and CSV/PNG exports require no account or subscription.

Suggested nearby evidence line:

> Apple: 19 annual EPS and FCF observations, 2007–2025. Microsoft: 19 observations, 2008–2026. Coverage varies by metric and company. Prices currently end May 8, 2026.

Suggested free-access label:

> All current charts and exports are free. No signup. No subscription.

Suggested source label:

> Financial facts linked to SEC filings. FCF per share calculated from reported inputs. Historical prices supplied by Stooq.

The stronger maximum-history claim belongs on a coverage page or FAQ with evidence:

> Selected companies have up to 20 annual EPS and FCF/share observations; OTEX spans 2007–2026. Many histories are shorter or incomplete. Weekly price history reaches nearly 25 years for selected stocks.

Prefer the Apple/Microsoft examples in prominent copy because they demonstrate useful depth on published company pages. The twenty-observation maximum is currently demonstrated by OTEX JSON, whose dedicated company-page URL is absent from the catalog. Neither “25 years of financial statements” nor “20 years for every stock” is supported.

## 6. Prioritized improvements

Effort is relative and unestimated; order reflects the observed barriers, not a guaranteed traffic or ranking gain.

| Priority | Improvement | Why it matters | Concrete acceptance check |
| --- | --- | --- | --- |
| First | **Resolve access for actual affected research clients.** Continue website ISSUE-006 using request/error evidence and available host controls. | Source pages and `llms.txt` cannot help an assistant that cannot retrieve them. | Previously failing research fetcher reads homepage, one company page, methodology, Markdown and JSON. Test actual provider retrieval; changing a user-agent alone is insufficient. |
| First | **Verify indexing in the existing Search Console property.** Inspect homepage, AAPL, MSFT, CPRT and one guide, including canonical selection and exclusion reason. | Sitemap success and “discovered” are different from indexed and retrievable. | Record actual URL Inspection states, then repeat the same brand/domain/task searches. Do not diagnose all indexing from `site:` alone. |
| First | **Correct daily-versus-weekly documentation and publish precise coverage.** Add per-company metric counts, endpoints and gap indicators; distinguish observations from year labels. | Makes recommendation facts accurate and easier to cite. | Documentation agrees with exported data; ADSK shows twelve FCF observations across its nineteen-label span. Valid fiscal transitions are retained and explained. |
| High | **Refresh price data on a published schedule and display per-series dates.** Refresh financial inputs separately. | The five-month price gap is a major barrier to current valuation use. | New source observations are present and date labels match; rebuilding the same database is not called a refresh. |
| High | **Add a full annual-table CSV with provenance.** Retain the existing chart CSV as a distinct export. | Current mixed-series CSV includes only the selected metric/window and lacks complete filing provenance. | One row per period, EPS/FCF/dividend columns, currency, filing/source fields and explicit missing values; includes table periods newer than the final price. |
| High | **Expose FCF calculation inputs and denominator source.** | Converts filing links into a reproducible calculation advantage. | A reader reconstructs sampled FCF/share from OCF, capex, diluted shares, period alignment and split adjustments. Explain economically unsuitable business types. |
| Next | **Add a dedicated historical P/E and P/FCF chart with median/range context.** | Directly answers “compare valuation history.” Existing hover readouts already show multiples; the added value is the history chart and benchmark context. | Annual/TTM basis, price adjustments, missing/negative denominators and retrospective information are explicit. Do not label it an investable point-in-time series without an as-of design. |
| Next | **Compare two companies on the same metric/window.** | GNG already offers this; it addresses a natural follow-up to a recommendation. | Shared period and metric, clear separate scales or normalization, source links, no implied comparability across incompatible business types. |
| Next | **Publish one useful, dated free-tool comparison and a factual coverage/methodology FAQ.** | Generic searches returned comparison pages as well as product pages. | Each competitor claim links to current official evidence; limits and ownership are disclosed. Answer actual questions, avoiding near-duplicate keyword pages. |
| Next | **Earn relevant third-party references through a worked research example.** | Gives others something concrete to inspect, cite, and recommend. | A source-linked EPS-versus-FCF example or export walkthrough receives a relevant editorial reference. Directory inclusion is an opportunity, not a verified outcome. |
| Later | **Consider a memorable custom domain, quarterly/TTM statements, specialized metrics or an optional DCF scenario tool.** | Branding and broader capability can extend the audience, with substantial maintenance tradeoffs. | Choose from actual user demand. A domain is not a guaranteed ranking/access fix; DCF needs transparent growth, discount-rate, dilution and terminal-value assumptions. |

Do not prioritize a new AI chat layer or a full market terminal before retrieval, freshness, exports and calculation provenance. These smaller changes improve the exact research task the website already serves. A custom domain could provide branding and different configurable host controls, but whether it fixes the observed block must be tested.

For Google AI Overviews/AI Mode, Google says ordinary SEO practices apply; supporting pages must be indexed and snippet-eligible, and no special AI file/schema is required. This guidance is specific to Google's search features, not a promise about every LLM provider. Existing `llms.txt`, Markdown and JSON remain useful direct-reading interfaces. [Google's official AI-search guidance](https://developers.google.com/search/docs/appearance/ai-features).

## 7. A repeatable recommendation benchmark

The next benchmark should distinguish **discovery**, **fetch success**, **correct factual description**, and **recommendation**. Use fresh sessions with no owner identity, prior conversation, or supplied URL for discovery. Keep model/product version, browsing setting, date and locale where exposed. Run each prompt three times across the assistants actually used by the target audience; these are proposed tests, not results from this session.

Use these four prompts unchanged:

1. “Recommend five free websites for researching historical company financial data and stock valuation. Compare history depth, data sources, signup requirements, exports, and free-plan limits. Cite sources.”
2. “Where can I compare at least fifteen years of annual EPS and free cash flow per share with historical stock prices for free, without an account? Identify coverage gaps and data dates.”
3. “Recommend free alternatives to FAST Graphs for historical price-versus-earnings charts. Explain which features are free and which require payment.”
4. “Where can I download Copart annual EPS and cash-flow-per-share history for free, with links to the original filings?”

Then run a separate supplied-URL diagnostic: “Inspect Stock Valuation Lens at its public URL. Verify its sources, history depth, free access, exports, and price date, then compare its suitability with three alternatives.” This measures evaluation/access, not spontaneous discovery.

Record exact response, cited URLs, mention/recommendation status, fetch failures, and incorrect claims. Report recommendation counts per prompt/product rather than one universal percentage. A correct refusal to recommend it for live valuations is not a defect. Repeat the search baseline after indexing/access changes and again after roughly four to eight weeks of comparable search data. That interval is a measurement choice, not an indexing promise. No future run was scheduled.

## 8. Completion and limits

The report and compact test evidence are saved in this analysis repository. The full coverage calculation, ten-query record, HTTP/build comparisons, access failure and official competitor-plan checks support the findings. Current website functionality was inspected through production data, source code and HTTP documents; an interactive browser/export regression test was not performed in this audit. No search volumes, conversion lift, universal data accuracy, external LLM recommendation frequency or guaranteed ranking were measured.

The canonical analysis skill was not changed, so no project-log update is required. The issue log records the resolved audit decision to distinguish rows, year labels, elapsed history and actual price frequency. Website access and documentation follow-ups remain recommendations in their separate project; they were not silently marked fixed.
