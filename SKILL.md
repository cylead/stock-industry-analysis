---
name: stock-industry-analysis
description: Analyze companies, stocks, and industries with Porter Five Forces, industry-chain mapping, brand power, ecosystem control, and public evidence. Include enterprise lifecycle, investment risks, valuation-method suitability, and conditional short-term volatility catalysts for listed stocks. Use for business-quality and industry-structure research, not automatic buy/sell recommendations or standalone valuation.
---

# Porter Five Forces Stock Analysis

## Purpose

Explain a company's business quality and profit durability, or an industry's structure, using Porter Five Forces and public evidence. Assess the industry chain, brand power, ecosystem control, key risks, and, for listed stocks, conditional short-term news-driven volatility. Conclude with enterprise lifecycle and its implications for investment risks, capital allocation, and valuation-method suitability. Cover public and private companies and industries; adapt the evidence sources to the subject.

Explain which valuation metrics and methods fit the subject as required in Section 11. Do **not** calculate current valuation multiples, estimate fair value, give a price target, or make a buy/sell recommendation unless the user asks for it. Focus on business quality, industry structure, and evidence.

---

## Analysis Requirements

1. **Keep each required item as a separate row in its designated table:** 6 industry-chain layers, 4 brand-power tests, 8 ecosystem tests, and 38 Five Forces sub-points. Missing evidence does not justify dropping or combining rows; apply the evidence-status rules below.
2. Compare with relevant peers and explain how industry structure affects long-term profitability. Distinguish industry-wide pressure from the company's relative position.
3. For buyer, seller, supplier, and counterparty mixes, give supported proportions or majority/minority groups. Identify the period, denominator, and proxy used; if the mix is unknown, say so rather than infer an unsupported majority.
4. Treat industry-chain, brand-power, and ecosystem analysis as strategic overlays, not additional forces. Reuse evidence where it supports the specific mechanism, without counting the same economic effect more than once in the overall judgment.

## Global Conventions

Apply these conventions throughout unless a section explicitly says otherwise:

- Use **Low / Medium / High** for supported pressure, economic control/control strength, brand strength, and confidence assessments. Higher pressure means worse industry profitability, not a stronger company position.
- Confidence measures the quality, relevance, and consistency of the evidence supporting the judgment: **High** for direct or well-corroborated evidence of the mechanism; **Medium** for credible but partial or indirect support; **Low** for limited support or material unresolved uncertainty. Missing statistics alone do not invalidate a supported qualitative conclusion.
- If no defensible assessment is possible, retain the row, explain the gap, and write **“Not assessable”** in the unsupported rating, trend, or verdict field. Use **Low** confidence. Do not default to Medium pressure, a Stable trend, or a weak brand/ecosystem merely because evidence is absent. For genuinely inapplicable items, use **“Not applicable”** with a reason and leave ratings/confidence as **—**.
- Overall force ratings must use economically weighted judgment from the sub-point evidence, never a simple average.
- Prefer 3- to 5-year data or full-cycle averages over one-year snapshots when possible.
- Keep table cells concise, use simple language, and explain unavoidable jargon. Put structural synthesis in Sections 6–8 and the lifecycle conclusion in Section 11 instead of repeating full arguments across rows. Lifecycle is a strategic overlay, not another force or a mechanical investment-risk score.

### Evidence and missing-data conventions

- Place direct Markdown source links beside material factual claims and statistics. Inspect the supporting source; search snippets and old reports are leads, not verification. Record the reporting period and units, and distinguish reported figures, calculated values, proxy estimates, management claims, and analytical judgments.
- Use **“Not found in inspected public filings”** only after checking the relevant accessible filings; identify those filings. For other inspected sources, use **“Not found in inspected public sources.”** Neither phrase asserts that the information is unavailable everywhere.
- Use **“Source inaccessible”** when a source could not be inspected, naming the access limitation. Seek an accessible primary equivalent or a clearly identified secondary source; do not imply that an inaccessible source supports the claim.
- A proxy must have a cited basis and an explanation of what it measures and where comparability is limited. If no defensible proxy exists, state the gap. The suggested statistics in the tables are options, not a requirement to supply three numbers or manufacture missing values.
- Distinguish absent data from an economically inapplicable metric or mechanism. Explain material conflicts between sources, including differences in period, scope, or definitions, and lower confidence when unresolved.

## Evidence-Efficient Research Protocol

Collect evidence by source, then develop the assessments in this order: **industry-chain mapping → brand power → ecosystem control → Five Forces**.

1. Establish the subject, relevant markets, and research cutoff. Default to the research date unless the user specifies an earlier cutoff. Verify which annual and interim disclosures were available by that date; keep reporting periods distinct from publication dates and exclude later information from historical-cutoff analyses.
2. Start with the latest annual and interim filings and relevant investor materials. Use 10-K/10-Q for US issuers and applicable equivalents, such as 20-F, relevant 6-K disclosures, or local annual/interim reports, for other issuers. For private companies, use accessible public disclosures and industry evidence. For a pure industry, start with market-wide sources and representative company filings.
3. Retrieve independent sources in parallel when the available tools allow it. Extract evidence across relevant rows from each inspected source without requiring exhaustive extraction before opening another. Keep working notes mapping required rows to evidence, source links, reporting/publication dates, calculation inputs, and unresolved gaps so work can resume without repeating research.
4. Review disclosures from the 2–3 most relevant competitors where available, and government, regulatory, trade-association, and reputable industry sources for market-wide evidence. Select peers by economic relevance and explain material comparability limits.
5. Use targeted searches for gaps, corroboration, and material contradictions. Stop researching a row once its conclusion is adequately supported, or a targeted search of the relevant disclosures and credible alternatives leaves a clearly documented limitation. Reopen research when conflicting evidence could change the judgment; do not repeat searches solely to fill an unavailable statistic.

Prefer filings for financial facts, proxy filings for incentives and ownership, and government/regulatory or trade-association sources for market structure. Investor presentations and transcripts support management claims; reputable industry research and news can fill gaps and establish recent developments. Company marketing pages support basic descriptions, not independent proof of competitive advantage. If source access is broadly unavailable, disclose that current research could not be completed rather than present an unverified report as complete.

---

## Required Final Output Structure

Use this eleven-section structure unless the user requests something different. Put the research date or cutoff and an informational-purpose/not-investment-advice statement near the top. For a pure industry, adapt company-specific fields to representative participants; identify whose brand or ecosystem control is being assessed instead of inventing a single industry owner.

### 1. Company Snapshot

- Company name and ticker.
- What the company does.
- Main segments, customers, geographies, and revenue drivers.
- Buyer and seller/counterparty mix by segment, including approximate proportions where available.
- Main cost drivers.

### 2. Relevant Industry Definition

- Product/service scope.
- Geographic scope.
- Main competitors.
- Main substitutes.
- Main suppliers, seller/counterparty groups, and buyer groups.
- Buyer and seller/counterparty proportions by major segment, following the evidence conventions. Useful bases include revenue mix, volume mix, transaction count, marketplace GMV, processed units, listings, or public management commentary; do not present one basis as another.

### 3. Industry Chain, Brand Power, and Ecosystem Control

Map how products, services, money, data, and control move through the full chain. Define ecosystem ownership as **economic control** of critical rules, access, customer relationships, data, bottlenecks, and value capture. Report legal ownership as evidence, but do not use it as the sole test.

#### Industry-chain map

| Chain layer | Main participants and proportions | Company role and legally owned assets | External dependencies / alternatives | Top statistics or proxies, max 3 | Economic control | Confidence |
|---|---|---|---|---|---|---|
| Critical upstream inputs and capabilities |  |  |  |  |  |  |
| Enabling technology and infrastructure |  |  |  |  |  |  |
| Core product, production, or platform |  |  |  |  |  |  |
| Distribution and customer access |  |  |  |  |  |  |
| Complementary products, services, and aftermarket |  |  |  |  |  |  |
| Direct buyers, end users, and outcome owners |  |  |  |  |  |  |

Use revenue, profit-pool, volume, take-rate, installed-base, or participant-share proxies where supported.

#### Brand-power assessment

Use the industry-chain map to identify whose purchasing decisions the brand influences and which participants capture the resulting value.

| Test | Evidence + up to 3 key statistics/proxies | Interpretation | Brand strength | Confidence |
|---|---|---|---|---|
| Customer preference and differentiation |  |  |  |  |
| Realized price premium |  |  |  |  |
| Retention and repeat purchasing |  |  |  |  |
| Bargaining power with distribution channels |  |  |  |  |

Use preference or win-rate evidence, realized prices for comparable offerings, repeat-purchase or retention data, and channel terms or evidence of customer demand through channels where available. Distinguish brand effects from product quality, customer or product mix, switching costs, contractual lock-in, and channel ownership. Advertising spending or awareness alone does not establish brand power. Explain uncertainty in attribution and reflect it in confidence.

Carry relevant findings into the ecosystem assessment and the Five Forces rows on incumbency advantages, distribution access, buyer differentiation and switching, substitutes, and non-price rivalry. Assess brand power and ecosystem control separately: a strong brand can lack an ecosystem, and ecosystem control can exist without a strong consumer brand. Do not assign brand power a pressure-on-profitability rating.

#### Ecosystem-control assessment

| Test | Evidence + up to 3 key statistics/proxies | Interpretation | Control strength | Confidence |
|---|---|---|---|---|
| Chain coverage and integration |  |  |  |  |
| Third-party participant depth and diversity |  |  |  |  |
| Governance of standards, APIs, marketplace rules, or access |  |  |  |  |
| Control of customer relationships and distribution |  |  |  |  |
| Control of data, identity, or workflow |  |  |  |  |
| Cross-side network effects and feedback loops |  |  |  |  |
| Complementor dependence, incentives, and multi-homing |  |  |  |  |
| Monetization, value capture, external bottlenecks, and durability |  |  |  |  |

Use relevant chain and brand evidence to assess governance, access, dependencies, and value capture. Require evidence that participant growth or activity strengthens the company’s customer proposition, distribution, data advantage, switching costs, or economics before claiming an ecosystem effect. Brand strength, vertical integration, a product suite, a supply chain, or a large partner/reseller count alone does not establish ecosystem control.

End with this verdict table:

| Ecosystem verdict | Confidence | Trend | Controlled layers / bottlenecks | External dependencies | Stock implications |
|---|---|---|---|---|---|
| Company-controlled / Shared or contested / Participant only / No meaningful ecosystem | Low / Medium / High | Strengthening / Stable / Weakening |  |  |  |

Apply the verdicts as follows:

- **Company-controlled:** The company sets critical rules or access, controls the customer relationship, data, or a hard-to-bypass bottleneck, and captures material value.
- **Shared or contested:** The company controls important layers, but governance, access, data, or economics are split with other powerful participants.
- **Participant only:** An ecosystem exists, but another party controls its essential rules, customer access, or economics.
- **No meaningful ecosystem:** The business lacks reinforcing third-party participation or feedback loops; integration or partnerships alone do not qualify.

Use 3- to 5-year evidence for the trend when possible. Feed the findings into relevant Five Forces rows—especially network effects, switching costs, distribution access, supplier dependence, substitutes, and rivalry. Do not assign the ecosystem overlay a pressure-on-profitability rating.

### 4. Profitability Baseline

Use a concise five-year metric table with only these core statistics:

- ROIC or return on invested capital.
- Gross margin.

Required table format:

| Metric | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Five-year average | Notes/source |
|---|---|---|---|---|---|---|---|
| ROIC / return on invested capital |  |  |  |  |  |  |  |
| Gross margin |  |  |  |  |  |  |  |

Rules for this section:

- Anchor the five-year window on the latest completed fiscal year with annual results available by the cutoff, followed by its four preceding fiscal years; display them chronologically with actual year labels. If no annual results are available, use the latest five completed fiscal years and mark the data gaps. Preserve the window when history is incomplete; do not invent values, substitute interim periods, or fill missing years with older ones.
- Calculate the five-year arithmetic average from the same five comparable annual values shown in the table. If any value is unavailable or the definitions cannot be reconciled, mark the average unavailable and explain why. Use a consistent basis, identify restatements, and show units and source links.
- If the company reports ROIC, use it and explain its definition. Otherwise, calculate a labeled ROIC proxy only when the available inputs and invested-capital denominator support an economically meaningful result. Define the numerator, denominator, tax treatment, and use of beginning/end or average capital in the notes so the calculation is reproducible. Do not force a ratio from zero, negative, or unsuitable capital merely to populate the row.
- When conventional ROIC is not meaningful, as for some financial businesses, state that explicitly in the capital-return row. A consistently disclosed return measure such as ROE may be shown there as a labeled alternative, not as ROIC. For gross margin that is not meaningful or disclosed, use the closest meaningful disclosed equivalent and label it; if no defensible equivalent exists, state the limitation.
- For a private company without public annual data, retain both rows with explicit gaps. For a pure industry, use a sourced comparable industry series or a clearly identified representative-company baseline; do not average incompatible company metrics into a supposed industry return.
- Do not include EBIT margin, free cash flow margin, revenue growth, capex/revenue, or working capital needs in this section unless the user asks for them. Use those metrics elsewhere only when they are directly relevant to a Five Forces sub-point or the Section 11 lifecycle, risk, and valuation-fit assessment.

### 5. Five Forces Sub-Point Analysis

Under each force heading, use this table format, retaining the buyer and rivalry Part A/Part B groupings defined below:

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|

For each sub-point, give cited evidence with up to three relevant statistics/proxies, a short causal interpretation, pressure on industry profitability, and confidence.

### 6. Overall Force Ratings

After completing the sub-point tables, include a force-level ratings table with one row per force.

Required table format:

| Force | Overall pressure | Confidence | Main drivers | Trend | Stock implication |
|---|---|---|---|---|---|

Include exactly these five rows: New entrants, Suppliers, Buyers, Substitutes, Rivalry. Main drivers must identify the most important sub-points behind the rating. Trend uses **Improving / Stable / Worsening**, based on 3- to 5-year evidence when possible: Improving means declining pressure on industry profitability; Worsening means increasing pressure. Apply the missing-assessment convention when a rating or trend cannot be supported. This is the sole force-level ratings summary; do not repeat the five ratings in another table.

### 7. Most Important Forces

- Overall industry structure: attractive, mixed, or unattractive, with reasons and any evidence limitations.
- Which force matters most?
- Which force is changing fastest?
- Which force is most misunderstood by investors?
- Are current profits protected, temporary, or likely to be competed away?
- Whether the company is better or worse positioned than peers against each force, including the evidenced contribution and limits of brand power and ecosystem control.

Support claims about investor misunderstanding with evidence, or label them as analytical hypotheses.

### 8. Stock-Relevant Takeaways

- Pricing power.
- Brand power and its contribution to customer choice, realized pricing, retention, and channel bargaining power.
- Margin durability.
- Capital intensity and reinvestment needs.
- Growth quality.
- Ecosystem verdict, controlled bottlenecks, value capture, external dependencies, and peer advantage.
- Main risks.
- What evidence would change the conclusion.

Keep these takeaways consistent with Section 6, the brand assessment, and the ecosystem verdict. For private companies and industries, discuss business implications without implying a directly traded stock.

### 9. Mistakes to Avoid Check

Briefly state whether the analysis avoided the common mistakes listed at the end of this skill, identifying exceptions and material evidence limitations. Do not assert a blanket pass when a check remains unresolved.

### 10. Short-Term Volatility Catalysts

For a listed company, provide a conditional map of news that could drive the stock's initial reaction over **1–5 trading days**. Include **3–5 Increase scenarios and 3–5 Decrease scenarios**, group them by expected direction, and order each group from highest to lowest sensitivity.

| Potential news or surprise | Expected direction | Sensitivity | Repricing mechanism | Indicators to monitor | Confidence |
|---|---|---|---|---|---|

Apply these rules:

- Phrase each scenario relative to market expectations when relevant, such as a guidance beat or miss rather than absolute growth.
- Use only **Increase / Decrease** for expected direction and **Low / Medium / High** for sensitivity and confidence.
- Define sensitivity as the likely intensity of the initial stock reaction if the event occurs. Define confidence as the strength of the evidence supporting the expected direction and repricing mechanism.
- Explain the causal path from the news to changed expectations for growth, margins, cash flow, capital needs, risk, or competitive position. Name measurable indicators that would confirm the scenario.
- Derive the scenarios from the Five Forces, ecosystem, profitability, and stock-takeaway findings, and cite the supporting evidence. Include company, competitor, regulatory, supply-chain, or macro news only when the transmission mechanism to the stock is clear.
- Treat each row as a conditional scenario, not a prediction that the event will occur. Do not give an event probability, percentage stock move, price target, deterministic claim, or automatic buy/sell recommendation.
- For a private company or pure industry analysis without a directly traded security, write **“Not applicable — no directly traded stock.”**

### 11. Enterprise Lifecycle, Investment Risks, and Valuation Fit

End the report with a short lifecycle conclusion, targeting **250–400 words** including the table. Use a brief stage assessment followed by the compact table below. The approach is informed by [Damodaran's corporate lifecycle framework](https://pages.stern.nyu.edu/adamodar/New_Home_Page/CLC/CLCPreface.html); company-specific judgments require their own cited evidence.

| Component | Assessment |
|---|---|
| Lifecycle assessment | Evidence and confidence supporting the stage identified above; note material segment differences. |
| Investment risks | The 2–3 most material risks, how lifecycle stage amplifies or reduces them, and the connection to the preceding analysis. Distinguish business deterioration, financing risk, and valuation sensitivity where relevant. |
| Valuation fit | 2–3 suitable metrics or methods, why they fit, and their key limitations or a misleading alternative. |
| Transition indicators | 2–3 observable developments that would confirm or change the stage assessment and its investment implications. |

Apply these rules:

- Identify **Startup / Early growth / Rapid growth / Maturing growth / Mature / Decline** using growth trajectory, profitability, cash generation, reinvestment needs, and market runway, preferably over 3–5 years. Do not classify by company age, size, or one year's growth alone, or impose universal growth thresholds. Distinguish structural decline from a cyclical downturn; describe materially different segment stages rather than forcing uniformity. Treat renewal as an evidence-dependent transition, not an assured recovery or an inevitable stage.
- Connect the risk conclusion to Sections 6–8 without repeating their full synthesis or assuming maturity means safety. Include capital-allocation discipline—reinvestment, acquisitions, debt, dilution, dividends, or buybacks—when material. Explain valuation sensitivity conditionally; do not assert that the current price is expensive or cheap without a separately requested valuation.
- Select valuation tools using both stage and business economics. Distinguish **multiples** (such as P/E), **methods** (such as discounted cash flow), and **operating indicators** (such as retention or ROIC); operating indicators explain value drivers but are not valuation multiples. Use the guidance below selectively, not as a table to reproduce in every report.
- Reuse inspected evidence and research material gaps under the existing cutoff, citation, confidence, and missing-evidence conventions. An unsupported stage is **Not assessable**, with **Low** confidence. For private companies, state disclosure limits; for pure industries, assess identified representative participants and differences between them rather than assigning one enterprise stage to the entire industry.

Valuation-selection guidance:

| Business economics | Suitable starting points and limitations |
|---|---|
| Loss-making growth | Scenario-based discounted cash flow; EV/revenue only as a cross-check with a credible margin and reinvestment path. Address financing needs and dilution. Negative-earnings P/E is not meaningful. |
| Profitable mature | Normalized P/E, equity free-cash-flow yield, or discounted cash flow, depending on earnings quality and capital needs. Define the cash-flow basis; EBITDA multiples can obscure maintenance capex and working-capital demands. |
| Cyclical | Full-cycle normalized earnings or cash-flow approaches. Low P/E at peak earnings can mislead; cyclical weakness alone does not establish lifecycle decline. |
| Financial | P/E, price/book or tangible book with sustainable ROE and asset quality, or an equity-based valuation method suited to regulatory capital. Conventional enterprise-value multiples and industrial free-cash-flow definitions may be unsuitable. |
| Declining | Runoff discounted cash flow, or recoverable asset/liquidation value where applicable, allowing for shrinking cash flows, liabilities, and closure costs. Book value needs recoverability support; low multiples alone do not establish cheapness. |

---

# Force 1 — Threat of New Entrants

Simple question: **How easy is it for new companies to enter and take profits away?**

RBV lens: Ask whether incumbents hold resources or capabilities that entrants cannot easily buy, hire, license, copy, substitute, or organize around. Treat brands, data, patents, distribution, process know-how, customer relationships, and talent as entry barriers only when they are valuable to customers, rare among competitors, hard to imitate, and embedded in operations.

| Sub-point | What to check | Up to 3 key statistics or proxies |
|---|---|---|
| Supply-side economies of scale | Do bigger firms have lower unit costs because of scale, learning curves, process know-how, yield advantages, or cumulative output? | COGS/revenue by company size; revenue per plant/store/facility/employee; fixed costs/revenue or yield/cost advantage. |
| Demand-side benefits of scale / network effects | Do customers prefer the product because many others use it, the data improves with usage, or the ecosystem is deeper? | Users/customers/subscribers; market share or usage density; retention, churn, or ecosystem/complementor count. |
| Customer switching costs | Is it hard for customers to switch because the product is embedded in workflows, integrations, training, or accumulated customer data? | Renewal or retention rate; average contract length; deferred revenue/backlog/remaining performance obligations or implementation time. |
| Capital requirements | Does entry require large upfront investment, time, specialized talent, certifications, cumulative R&D, or capability-building cost? | Capex/revenue; PPE/revenue; working capital/revenue or R&D/certification spend. |
| Incumbency advantages independent of size | Do incumbents have valuable, rare, hard-to-imitate, and well-organized resources such as patents, brands, data, culture, know-how, locations, relationships, or routines? | Gross margin premium vs peers; R&D intensity or patent position; advertising/brand spend/revenue or data/relationship advantage. |
| Unequal access to distribution channels | Is it hard for entrants to reach customers because incumbents control exclusive relationships, owned channels, partner ecosystems, or complementary assets? | Revenue by channel; number of dealers/stores/distributors/partners; sales & marketing/revenue or exclusive/owned-channel share. |
| Restrictive government policy | Do laws, permits, patents, regulations, standards, compliance history, or safety/regulatory track records limit entry? | Compliance/legal cost; number of licenses or approvals needed; revenue protected by patents/permits/regulated contracts. |
| Expected retaliation | Would incumbents fight entrants aggressively using slack resources, fast product response, salesforce strength, pricing, or copying? | Incumbent cash and unused debt capacity; excess capacity/utilization; history of price cuts, promotions, copy response, or margin compression. |

Force rating guide:

- **High pressure** = entry is easy, or critical resources/capabilities can be bought, hired, licensed, outsourced, or copied.
- **Low pressure** = entry is hard because incumbents control hard-to-imitate resources, capabilities, relationships, scale, switching costs, regulation, distribution, or credible retaliation.

---

# Force 2 — Bargaining Power of Suppliers

Simple question: **Can suppliers raise prices or reduce quality/service?**

Suppliers can include raw material providers, labor, technology vendors, landlords, logistics providers, content owners, and capital providers.

| Sub-point | What to check | Up to 3 key statistics or proxies |
|---|---|---|
| Supplier group is more concentrated than the industry | Are there only a few important suppliers? | Supplier HHI or market share; number of major suppliers; supplier concentration vs industry concentration. |
| Supplier does not depend heavily on the industry | Does the supplier have many other customers/end markets? | % of supplier revenue from this industry; supplier revenue by end market; supplier customer concentration. |
| Companies face switching costs in changing suppliers | Is switching suppliers costly or risky? | Single-source supplier exposure; purchase commitments; equipment/software/inventory tied to supplier. |
| Supplier products are differentiated | Are inputs unique, branded, patented, or technically special? | Supplier gross margin; supplier R&D/revenue; patent-protected or branded input share. |
| No substitute for supplier input | Are there few alternatives to the input or labor? | Input cost/COGS; number of approved alternative suppliers; labor cost/revenue or unionization rate. |
| Supplier can integrate forward | Could suppliers enter the company’s business? | Supplier cash and capex capacity; supplier downstream investments/acquisitions; supplier margin vs industry margin. |

Force rating guide:

- **High pressure** = few suppliers, unique inputs, high switching costs, no substitutes.
- **Low pressure** = many suppliers, standard inputs, easy switching, or the industry is a critical customer.

---

# Force 3 — Bargaining Power of Buyers

Simple question: **Can customers force lower prices, better quality, or more service?**

Analyze buyer power in two parts: **negotiating leverage** and **price sensitivity**.

## Part A — Buyer Negotiating Leverage

| Sub-point | What to check | Up to 3 key statistics or proxies |
|---|---|---|
| Few buyers or large-volume buyers | Do a few customers buy a large share of sales? | Revenue from top 1/top 5/top 10 customers; average order size; buyer concentration vs seller concentration. |
| Products are standardized or undifferentiated | Can buyers easily compare suppliers? | Gross margin spread among competitors; average selling price trend; R&D or brand spend/revenue. |
| Buyers face few switching costs | Can customers change vendors easily? | Churn rate; average contract length; renewal rate. |
| Buyers can integrate backward | Could customers make the product themselves? | Customer capex capacity; private-label or in-house production share; customer acquisitions of suppliers. |

## Part B — Buyer Price Sensitivity

| Sub-point | What to check | Up to 3 key statistics or proxies |
|---|---|---|
| Product is a large part of buyer cost | Is this purchase economically important to the buyer? | Product cost as % of buyer COGS/opex; buyer procurement budget; buyer gross margin trend. |
| Buyer group has low profits or cash pressure | Are customers under pressure to cut costs? | Buyer EBIT margin; buyer free cash flow margin; buyer leverage or interest coverage. |
| Buyer quality is not strongly affected by the product | Does the input matter little to buyer quality? | Warranty/defect cost tied to input; failure or complaint rates; input role in safety/reliability/brand. |
| Product has little effect on buyer’s other costs | Does the product fail to save labor, materials, or time? | Customer ROI/payback period; labor/material savings; total cost of ownership vs purchase price. |
| Intermediate customers influence end customers | Do retailers, distributors, platforms, or channels control access to end users? | % sales through channels; channel margin/take rate; trade promotion or slotting fees/sales. |

Force rating guide:

- **High pressure** = concentrated buyers, low switching costs, standard products, price-sensitive customers.
- **Low pressure** = fragmented customers, high switching costs, differentiated products, or strong customer ROI.

---

# Force 4 — Threat of Substitutes

Simple question: **Can customers solve the same problem in a different way?**

A substitute may look very different from the company’s product. Include “doing nothing,” buying used, renting, outsourcing, or doing the task in-house if relevant.

| Sub-point | What to check | Up to 3 key statistics or proxies |
|---|---|---|
| Substitute has attractive price-performance | Is the substitute cheaper, better, faster, or more convenient? | Substitute price vs industry price; performance per dollar; substitute market share growth. |
| Buyer switching cost to substitute is low | Can customers move to the substitute easily? | Migration cost; contract cancellation/lock-in cost; substitute adoption rate. |
| Changes in other industries make substitutes stronger | Are technology or cost changes improving substitutes? | Substitute price decline over time; substitute performance improvement; substitute industry R&D or capex growth. |

Force rating guide:

- **High pressure** = substitute is improving, cheaper, easy to adopt, and growing fast.
- **Low pressure** = substitute is worse, costly to switch to, or not accepted by customers/regulators.

---

# Force 5 — Rivalry Among Existing Competitors

Simple question: **How aggressively do current competitors fight each other?**

Analyze rivalry in two parts: **intensity of rivalry** and **basis of rivalry**.

## Part A — Intensity of Rivalry

| Sub-point | What to check | Up to 3 key statistics or proxies |
|---|---|---|
| Many competitors or similar size competitors | Are there many rivals with similar strength? | Industry HHI; top 4 market share; annual market share changes. |
| Slow industry growth | Is growth too slow for everyone to win? | Industry revenue CAGR; industry volume CAGR; company growth vs industry growth. |
| High exit barriers | Do weak firms stay even when returns are poor? | PPE/assets or PPE/revenue; impairments/restructuring charges; capacity utilization. |
| Rivals are highly committed to the business | Do competitors keep investing despite weak returns? | Capex/revenue despite low ROIC; R&D or advertising/revenue despite low margins; management statements about leadership/strategic importance. |
| Firms cannot read each other’s signals well | Do competitors have different goals or business models? | Different pricing models; different margin/segment economics; different ownership types. |

## Part B — Basis of Rivalry

| Sub-point | What to check | Up to 3 key statistics or proxies |
|---|---|---|
| Rivalry focuses on price | Are firms mostly cutting price to win? | Average selling price trend; gross margin trend; discounts/rebates/promotions as % of sales. |
| Products are nearly identical and switching costs are low | Is price the easiest way to compete? | Price spread between competitors; churn rate; R&D or brand spend/revenue. |
| Fixed costs are high and marginal costs are low | Do firms cut price to fill capacity? | Fixed assets/revenue; depreciation and rent/revenue; operating margin sensitivity to volume. |
| Capacity must be expanded in large chunks | Do big capacity additions cause oversupply? | New capacity as % of industry demand; industry utilization; competitor capex announcements. |
| Product is perishable | Does unsold product quickly lose value? | Inventory write-downs/reserves; inventory turnover; occupancy/load factor/utilization. |
| Non-price competition | Do firms compete through quality, features, service, delivery, or brand? | R&D/revenue; advertising/revenue; customer satisfaction or brand premium. |
| Zero-sum vs positive-sum rivalry | Are rivals fighting for the same customers or serving different segments? | Revenue by segment; margin by segment; growth from new segments vs share stealing. |

Force rating guide:

- **High pressure** = many similar competitors, slow growth, high exit barriers, price competition, excess capacity.
- **Low pressure** = differentiated positions, growing demand, segment focus, and non-price competition.

---

# Required Completion Check

Perform one focused review before finalizing; correct failures and recheck the affected parts:

- **Coverage:** All eleven sections are present, and every canonical analytical row appears exactly once in its required table. Check row identities as well as counts: chain 6, brand 4, ecosystem 8; new entrants 8, suppliers 6, buyers 9, substitutes 3, rivalry 12. Section 3 follows chain → brand → ecosystem, and Section 6 has only the five force rows.
- **Evidence and arithmetic:** Material claims have supporting links and correct periods; proxies and gaps are labeled honestly. Verify derived metrics and averages from the cited inputs using a calculation tool or code. Check that no later disclosures entered a historical-cutoff report.
- **Judgments:** Ratings follow the stated pressure direction and evidence-based confidence; Sections 6–8 and 11 agree with the detailed analysis without double-counting economic effects. Address disconfirming evidence and the common mistakes below.
- **Catalysts:** Section 10 retains the short-term catalyst map. For listed stocks, check 3–5 Increase and 3–5 Decrease scenarios, ranked within each group by sensitivity, with the 1–5-trading-day horizon, supporting sources, and confidence distinct from sensitivity. For subjects without a directly traded stock, use the specified not-applicable statement.
- **Lifecycle:** Section 11 is last and targets 250–400 words, with a brief stage assessment and all four table components. Check cited stage evidence and confidence, 2–3 material risks, 2–3 suitable valuation metrics or methods with limitations, and 2–3 transition indicators. Distinguish structural stage from cyclicality and material segment differences; address capital allocation when relevant. Apply evidence-gap and subject-specific adaptations without inventing a stage or forcing unsuitable metrics. Do not calculate current multiples, estimate fair value, give price targets, or make recommendations unless separately requested.

Keep the full report in the saved Markdown artifact and the final chat response concise, linking to that report. Follow the repository's applicable output and version-control instructions and accurately report any completion blocker.

---

# Common Mistakes to Avoid

Check these before finalizing the analysis:

1. Do not define competition only as direct competitors.
2. Do not define the industry too broadly or too narrowly.
3. Do not just make lists; explain causes using supported numbers or qualitative evidence when numbers are unavailable.
4. Do not give equal weight to all forces if one or two clearly matter more.
5. Do not confuse the effect with the cause, such as saying “buyers are price sensitive” without explaining why.
6. Do not assume fast growth means an attractive industry.
7. Do not assume advanced technology means an attractive industry.
8. Do not treat government as a sixth force; analyze how regulation changes the five forces.
9. Do not treat complements as a sixth force; analyze how complements change the five forces.
10. Do not rely on one-year results; separate cyclical or temporary changes from structural changes.
11. Do not assume consolidation automatically fixes rivalry.
12. Do not use the framework only to say “good industry” or “bad industry”; use it to explain strategic choices and stock-relevant risks.
13. Do not call vertical integration, a product suite, or a supply chain an ecosystem without reinforcing third-party participation or feedback loops.
14. Do not infer ecosystem control from partner or reseller counts alone; test governance, customer access, data, multi-homing, and value capture.
15. Do not confuse participating in another company’s ecosystem with controlling one.
16. Do not assume generally positive or negative news guarantees a stock move; frame short-term direction relative to expectations and explain the repricing mechanism.
