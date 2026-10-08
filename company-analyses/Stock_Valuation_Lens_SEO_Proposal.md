# Stock Valuation Lens SEO proposal

Research date: 2026-10-08. Website: [Stock Valuation Lens](https://stock-valuation-public.valuationlens.workers.dev/).

Recommended starting position: **free historical stock research with annual EPS and cash-flow charts, filing sources, and exports without an account**. Start with specific research tasks and company queries. The site already has substantial crawlable company content; improving relevance, discovery, and usefulness should take priority over rebuilding its technical SEO foundations.

Status: proposal for the owner's decision. Website implementation and deployment are outside this completed documentation change. This repository does not contain the website application source. The tool is for historical research and is not investment advice.

## Audience and product scope

Assumed primary audience: English-speaking individual investors researching US-listed businesses over several years, especially value investors who want to examine earnings and cash generation alongside historical prices. Secondary audiences include investing students and spreadsheet users. Geography is provisional: begin keyword validation with United States and English settings, then compare actual visitor countries before targeting additional markets.

The site offers annual basic/diluted EPS, derived FCF per share, dividends, historical weekly prices, adjustable chart windows and multiples, and CSV/PNG exports. Its [directory](https://stock-valuation-public.valuationlens.workers.dev/stocks/) reports 6,551 searchable stocks, with dedicated company pages for 485 of 503 securities in its dated S&P 500 membership snapshot. These are different coverage scopes; avoid promising a dedicated indexable page for every searchable ticker.

The [methodology](https://stock-valuation-public.valuationlens.workers.dev/methodology/) describes the valuation line as a retrospective formula reference rather than an intrinsic-value estimate. The [sources page](https://stock-valuation-public.valuationlens.workers.dev/sources/) dates the financial database to 2026-08-27 and prices to no later than 2026-05-08. Accordingly, current quotes, analyst forecasts, DCF valuations, stock recommendations, and point-in-time backtests are poor keyword targets for the current product.

## Findings from the live website

The audit inspected the homepage, directory, Apple/Copart/Autodesk company pages, methodology, sources, about, dividend guide, updates, robots.txt, sitemap, and public CSV-export code. Company-page findings are a sample, not a validation of every page or financial observation.

| Area | Observed state | Implication |
| --- | --- | --- |
| Page delivery | Inspected HTML pages returned HTTP 200 over HTTPS. | No access failure was found on these public routes. Google indexing still needs separate confirmation. |
| Titles and descriptions | Homepage and sampled company pages have descriptive titles, descriptions, and canonical URLs. | Improve selected titles based on target intent; the site does not need a blanket metadata retrofit. |
| Company content | Sampled company pages contain annual tables, an EPS summary, fiscal dates, and SEC filing links directly in HTML. | Core financial content is available without chart rendering. Preserve this during later changes. |
| Crawl discovery | [robots.txt](https://stock-valuation-public.valuationlens.workers.dev/robots.txt) permits crawling and points to a valid XML [sitemap](https://stock-valuation-public.valuationlens.workers.dev/sitemap.xml) containing 493 URLs. The directory links to company pages. | Keep these assets; verify processing in Search Console rather than treating sitemap submission as proof of indexing. |
| Launch and search setup | The [updates page](https://stock-valuation-public.valuationlens.workers.dev/updates/) reports launch and Search Console connection on 2026-10-08, plus sitemap submission. It explicitly leaves processing and search inclusion unconfirmed. | This is a new-site baseline. Search Console access and its reports were not supplied, so actual index coverage, impressions, and rankings remain unverified. |
| Homepage explanation | Its initial HTML has a hidden welcome heading and a hidden chart workspace; in the rendered browser it opens an Apple chart. | Add a compact, persistent explanation of the research task, coverage, and free access. Keep the chart convenient to use. |
| Metric emphasis | Sampled company titles/summaries emphasize diluted EPS; tables also contain FCF per share and, where available, dividends. | Add distinct FCF explanations and relevant headings on suitable pages before creating extra metric URLs. |
| CSV export | The public script exports the selected chart metric alongside price, formula, and available dividend series in a mixed-series CSV. | Explain the format and how to select EPS or FCF. Do not market it as a separate complete annual-table download without verifying or adding that feature. |
| Trust and dates | Author/contact, corrections, sources, methodology, and approximation disclosures are already present. | Preserve these and improve per-metric provenance where useful. Do not confuse a website rebuild date with newer financial observations. |
| Additional metadata | No JSON-LD or Open Graph tags were found in the homepage or three sampled company HTML documents. | Consider appropriate structured data and sharing previews after the higher-priority content work. Their absence does not prevent indexing. |

No Search Console export, measured search volumes, backlink audit, or Core Web Vitals test was available. The proposal therefore does not assign numerical keyword difficulty, traffic forecasts, or guaranteed rankings.

## Keyword candidates and page mapping

Priority means product fit and recommended testing order, not measured organic difficulty. The specific phrases below are candidate wording derived from the feature audit and current search-result checks. Search demand for each exact phrase remains to be validated; narrow queries can be easier to satisfy while attracting very few searches.

| Priority | Candidate queries | Search intent | Best destination | Opportunity and limitation |
| --- | --- | --- | --- | --- |
| First | free historical EPS chart; free annual EPS history chart | Find a usable earnings-history tool | Homepage or one focused EPS tool page | Excellent fit. Explicitly say stock earnings per share, since EPS also names an image format. Other free EPS tools already compete. |
| First | download annual EPS history CSV; historical stock EPS data CSV | Obtain reusable historical data | Export guide linked to company pages and chart controls | Matches the existing export capability if the guide accurately explains the selected metric, range, and mixed-series format. Demand is unmeasured. |
| First | free cash flow per share history chart; free FCF per share chart | Examine cash generation per share | FCF guide/tool section and relevant company pages | More specific than general stock analysis; explain the share denominator, missing values, and unsuitable business types. |
| First | stock price vs earnings chart free; historical stock price and EPS chart | Put price in earnings context | Homepage and a chart walkthrough | Strong fit for historical comparison. Avoid implying a live valuation or reliable trading signal. |
| First | Copart EPS history CSV; CPRT annual EPS chart | Research or export one company's history | Existing `/stocks/cprt/` | Relevant table and chart already exist. Generic Copart EPS searches have numerous competitors; the export modifier is a test hypothesis. |
| First | Autodesk free cash flow per share history; ADSK FCF per share chart | Research a specific company's cash flow | Existing `/stocks/adsk/` | Existing FCF data supports the topic. Add a useful FCF summary; do not describe missing periods as zero. Competition is unmeasured for these exact variants. |
| Next | free stock fundamental charts no signup; free historical stock research tool | Find an accessible research service | Homepage | Good audience fit but broad competition. Use as supporting language rather than the only acquisition strategy. |
| Next | Apple annual EPS history download; AAPL historical EPS CSV | Obtain recognizable company data | Existing `/stocks/aapl/` | Useful demonstration page; Apple queries face established financial sites. Do not prioritize them solely because Apple is popular. |
| Next | how to chart stock price against earnings; EPS vs free cash flow per share | Learn a research method | Two focused educational guides | Connect the explanation to a real chart and filing sources. Generic financial definitions are competitive. |
| Next | fiscal year dividend yield vs trailing dividend yield; historical year end dividend yield | Understand a specific yield calculation | Existing `/guides/fiscal-year-dividend-yield/` | Distinctive topic with an existing worked example. Likely narrow audience; exact demand is unknown. |
| Next | free S&P 500 company EPS history | Browse company histories | Existing `/stocks/` | Clarify that this means constituent company histories, not aggregate S&P 500 index earnings. Keep coverage gaps visible. |
| Optional | free FAST Graphs alternative; FAST Graphs alternative no subscription | Find a substitute for a familiar service | One factual comparison guide | Potentially relevant audience, but requires accurate capability comparisons and an independent-project statement. It is not a claim of equivalent coverage or calculations. |

Treat related query variants as one topic where one page answers them. Do not create separate pages for every spelling, ticker synonym, “free” variation, or time-window parameter.

## What the competition suggests

Searches for free valuation charts, EPS history, FCF per share, CSV exports, and FAST Graphs alternatives surfaced existing tools and company metric pages. They establish competing content and product positioning, not monthly search demand or the site's Google rank in a particular country.

- [GNG Research](https://www.gngresearch.com/charting/) advertises free valuation charting with an account, with historical multiples and additional analysis features. No-account access can distinguish Stock Valuation Lens from this particular workflow.
- [Pineify's growth tool](https://pineify.app/free-tools/financial-statement-growth) advertises free EPS/cash-flow growth data and CSV export without registration. Free access and exports alone are therefore not unique advantages.
- [Stock Analysis](https://stockanalysis.com/fundamental-chart/) already offers fundamental charting. [Macrotrends](https://www.macrotrends.net/stocks/charts/CPRT/copart/eps-earnings-per-share-diluted) and [TickerStat](https://tickerstat.com/CPRT/eps) have Copart EPS history pages. Even a company-specific query can have strong competitors.
- [FAST Graphs](https://www.fastgraphs.com/) advertises analyst expectations, screening, and portfolio features beyond the current site's historical workflow. A comparison page should describe those differences accurately and verify current pricing before publication.

The practical distinction to emphasize is the combined workflow: a focused historical chart, annual per-share data, traceable filings, explicit limitations, and accessible exports. “Free” strengthens that proposition, but does not by itself establish an organic ranking advantage.

## Proposed changes for the owner to choose

| Option | Scope | Relative effort | Decision |
| --- | --- | --- | --- |
| A | Clarify the homepage, improve a small set of existing company pages, and confirm indexing. | Small | Recommended first. Uses existing pages and features. |
| B | Add three practical guides with contextual links and export instructions. | Medium | Recommended alongside A if content maintenance is feasible. |
| C | Expand company and metric coverage using measured search demand. | Larger and ongoing | Defer until indexing, usage, and data-refresh priorities are clearer. |
| D | Move to a memorable custom domain. | Separate hosting/domain decision with ongoing cost | Optional for branding and stable ownership; no automatic ranking benefit. |

### Option A improve the existing website

1. **Confirm Google discovery.** Check sitemap processing, Page Indexing reasons, and URL Inspection for the homepage, directory, and a small company sample. Record what is indexed and what needs fixing. The site already reports a connected Search Console property; do not repeat setup unnecessarily.
2. **Add compact homepage context.** Keep the chart prominent. Put a short visible introduction and links to the directory, EPS/FCF explanations, and export instructions beside or below it. Render this text in the initial HTML. A useful heading is “Free historical stock charts and financial data.” Use natural wording, not repetition of every keyword.
3. **Pilot company improvements.** Start with the audited AAPL, CPRT, and ADSK pages. Add a short FCF summary where sufficient observations exist, identify fiscal coverage, and explain how to open the relevant chart metric and export it. Keep all supported metrics on the existing company URL initially.
4. **Strengthen contextual links.** Link from metric explanations to actual company examples and from company sections to the matching guide. Directory sector filters already exist; create indexable sector pages only if they provide useful additional content and users need them.
5. **Keep provenance and freshness precise.** Retain filing links and price approximation labels. Consider exposing the FCF share-denominator source, which the sources page says is currently absent from the public export. Decide whether periodic data refresh is feasible before targeting searches that expect the latest period.

Suggested homepage copy for review:

> Explore annual earnings per share, free cash flow per share, dividends, and historical US stock prices. Use charts and export data without an account or subscription. Coverage and dates vary by company.

Suggested title tests, rather than required replacements:

- Homepage: `Free Historical Stock Charts and EPS Data | Stock Valuation Lens`
- Company example: `Copart (CPRT) EPS History and Cash Flow per Share | Stock Valuation Lens`
- Company description example: `Explore Copart's annual EPS and free cash flow per share, with historical charts and filing links. Free access and CSV exports without signup.`

The current titles are already descriptive. Keep a consistent brand name and evaluate title changes against impressions, clicks, and actual query intent. Google recommends concise, accurate page titles and useful descriptions; it does not use a meta-keywords tag. [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).

### Option B add practical guides

Create three pages that teach a task and link directly to the relevant tool:

| Proposed page | Content that makes it useful |
| --- | --- |
| `/guides/stock-price-vs-earnings/` | Walk through one historical chart, its date window and custom multiple; distinguish the formula line from an intrinsic-value estimate. |
| `/guides/eps-vs-free-cash-flow-per-share/` | Explain the two measures, fiscal periods, stock splits, and situations where FCF per share is unavailable or unsuitable, with filing-linked examples. |
| `/guides/export-stock-history-csv/` | Show the actual export workflow, column names, selected metric/range, and how to filter mixed-series rows in a spreadsheet. |

Extend the existing dividend guide with a clear comparison to trailing and forward yields if it adds useful explanation. Use genuine screenshots or exported charts with meaningful captions. A separate EPS or FCF tool landing page should earn its place through a distinct usable workflow; it should not duplicate the homepage for a keyword variation.

Google's guidance favors original, useful information written for an intended audience and transparent authorship. Preserve the site's automated-summary disclosure and add reviewed explanation where it helps; do not imply professional credentials or manual review that has not occurred. [Helpful content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).

### Option C expand selectively after measurement

Searchable stocks outside the dedicated company-page set present a possible content opportunity. Select a small pilot of roughly 10–20 companies using actual searches, reliable coverage, and useful history. Publish a dedicated page only when its data and explanation satisfy a distinct research need. Grow in response to evidence rather than generating thousands of minimally different pages.

Separate company metric URLs should be considered only when they can offer a focused chart, a complete relevant table, calculation/source context, and meaningful interpretation. Avoid competing near-duplicate URLs for the same topic. Keep changing chart controls from producing an uncontrolled number of indexable parameter URLs.

### Option D choose a domain for branding

A short custom domain could make the project easier to remember and share. The present workers.dev address can still host crawlable content; the audit does not establish a ranking penalty for it. Keyword-rich domains alone offer little ranking benefit. [Google's domain guidance](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).

If a move is selected, plan redirects from existing public URLs, consistent new canonical URLs and sitemap entries, and Search Console verification. Preserve access to the current address and check Google's current migration guidance before implementation. Domain purchase and migration are separate decisions.

## Supporting technical work

Measure before optimizing. Test the homepage and a representative company page on mobile with PageSpeed Insights, then fix observed loading, interaction, or layout problems. Good Core Web Vitals support page experience but do not guarantee high rankings. [Google's Core Web Vitals guidance](https://developers.google.com/search/docs/appearance/core-web-vitals).

Consider accurate Organization or Person and WebSite metadata, visible breadcrumbs with BreadcrumbList where appropriate, and Article metadata for authored guides. Validate against applicable Google-supported features. Structured data can help interpretation and eligibility for search features; it should match visible content and is not a guaranteed ranking improvement. Open Graph images can improve sharing previews. [Google's structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).

The site already advertises Markdown and llms.txt resources. Keep them if useful, but prioritize ordinary crawlable text and links for Google SEO. Google says its AI search features require no special AI files or schema. [AI features guidance](https://developers.google.com/search/docs/appearance/ai-features).

## Validation and measurement plan

1. **Establish a baseline.** In the existing Search Console property, record indexing status and performance by page, query, country, and device. Newly launched pages may initially have no meaningful search data. [Search Console performance guidance](https://support.google.com/webmasters/answer/10268906?hl=en).
2. **Validate keyword demand.** Check the candidate groups in Keyword Planner using explicit country/language settings and inspect target-market Google results. Record estimated searches separately from observed relevance and organic competition. Keyword Planner's competition column measures advertisers, not organic ranking difficulty. [Keyword Planner metric definitions](https://support.google.com/google-ads/answer/3022575).
3. **Pilot A and B.** Confirm useful content remains in initial HTML, titles match visible content, company links resolve, and exports behave as described. Preserve source and date disclosures. Recheck only affected pages after implementation.
4. **Review after approximately 4–8 weeks of indexing and comparable data.** This is a review interval, not a ranking promise. Compare relevant impressions, organic clicks, and visitor use of company charts and exports. Record indexation progress before attributing changes to titles or content.
5. **Choose the next expansion.** If supported queries appear, improve pages with useful impressions and weak click-through, or address unmet tasks. If a page is not indexed, investigate indexing first. If no search demand appears, revisit the keyword hypothesis rather than assuming that adding more similar pages will solve it.

Recommended decision: begin with **A plus B**, using historical EPS/FCF and export queries as the initial tests. Revisit C after evidence accumulates, and treat D as an independent branding choice. First-place rankings cannot be promised; success is more qualified visitors who can accomplish the research task.
