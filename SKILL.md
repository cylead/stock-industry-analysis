---
name: stock-five-forces
description: Analyze public companies, stocks, and industries with Porter Five Forces, industry-chain mapping, ecosystem-control assessment, and evidence from public filings. Use for business-quality and industry-structure research; do not use for automatic buy/sell recommendations or valuation.
---

# Porter Five Forces Stock Analysis

## Purpose

Use this skill to analyze a public company or stock that the user is not familiar with. The goal is to understand the business, industry chain, ecosystem control, industry structure, durability of profits, and key risks using Porter Five Forces and public information such as 10-Ks, 10-Qs, annual reports, investor presentations, transcripts, proxy filings, competitor filings, government data, and reputable industry sources.

Do **not** give a buy/sell recommendation, price target, or valuation unless the user asks for it. Focus on business quality, industry structure, and evidence.

---

## Non-Negotiable Rules

1. **Analyze every industry-chain layer, ecosystem test, and Five Forces sub-point listed in this skill.** Do not skip or combine required rows.
2. Show each required item as its own table row; do not summarize only at the force level.
3. Compare the company with key competitors when possible, separate facts from judgment, and explain how industry structure affects long-term profitability.
4. When listing buyers, sellers, suppliers, or counterparties by segment, include approximate proportions where available. If exact percentages are unavailable, state the majority/minority groups and the proxy used.
5. Treat industry-chain and ecosystem analysis as a strategic overlay that informs the five forces, not as a sixth force.

## Global Conventions

Apply these conventions throughout unless a section explicitly says otherwise:

- If evidence is limited or unavailable, write **“Not found in public filings”** and use the best public proxy.
- For each Five Forces sub-point, include evidence, up to **three** important statistics or proxies, a short interpretation, pressure on industry profitability, and confidence.
- Use **Low / Medium / High** for pressure, economic control/control strength, and confidence as applicable.
- Overall force ratings must use economically weighted judgment from the sub-point evidence, never a simple average.
- Prefer 3- to 5-year data or full-cycle averages over one-year snapshots when possible.
- Use simple language and explain unavoidable jargon.
- Keep facts/evidence distinct from interpretation/judgment.

## Evidence-Efficient Research Protocol

1. Start with the company’s latest 10-K, latest 10-Q, and relevant investor materials; extract evidence for **all applicable required rows** from each source before opening another source.
2. Review filings from the 2–3 most relevant competitors and reuse them across applicable rows.
3. Use government, regulatory, trade-association, and reputable industry sources for market-wide evidence.
4. After mining the core sources, run targeted searches only for required rows that still lack adequate evidence or corroboration.
5. Reuse the same evidence across relevant rows when economically appropriate, but do not double-count it in force-level judgments.
6. Do not launch a separate search for a sub-point when existing sources already support a well-corroborated conclusion at the required confidence level.

---

## Required Final Output Structure

Use this structure unless the user requests something different.

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
- Approximate buyer and seller/counterparty proportions by major segment. If exact percentages are unavailable, identify at least the majority group and explain the proxy used, such as revenue mix, volume mix, transaction count, marketplace GMV, processed units, listings, or public management commentary.

### 3. Industry Chain and Ecosystem Control

Map how products, services, money, data, and control move through the full chain. Define ecosystem ownership as **economic control** of critical rules, access, customer relationships, data, bottlenecks, and value capture. Report legal ownership as evidence, but do not use it as the sole test.

#### Industry-chain map

Include each required layer as a separate row.

| Chain layer | Main participants and proportions | Company role and legally owned assets | External dependencies / alternatives | Top statistics or proxies, max 3 | Economic control | Confidence |
|---|---|---|---|---|---|---|
| Critical upstream inputs and capabilities |  |  |  |  |  |  |
| Enabling technology and infrastructure |  |  |  |  |  |  |
| Core product, production, or platform |  |  |  |  |  |  |
| Distribution and customer access |  |  |  |  |  |  |
| Complementary products, services, and aftermarket |  |  |  |  |  |  |
| Direct buyers, end users, and outcome owners |  |  |  |  |  |  |

Apply the Global Conventions. Include revenue, profit-pool, volume, take-rate, installed-base, or participant-share proxies where available. If a layer is not applicable, write **“Not applicable”** and explain why.

#### Ecosystem-control assessment

Include every test as a separate row.

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

Apply the Global Conventions and compare with key peers. Require evidence that participant growth or activity strengthens the company’s customer proposition, distribution, data advantage, switching costs, or economics before claiming an ecosystem effect. Do not equate vertical integration, a product suite, a supply chain, or a large partner/reseller count with ecosystem control.

End with this verdict table:

| Ecosystem verdict | Confidence | Trend | Controlled layers / bottlenecks | External dependencies | Stock implications |
|---|---|---|---|---|---|
| Company-controlled / Shared or contested / Participant only / No meaningful ecosystem | Low / Medium / High | Strengthening / Stable / Weakening |  |  |  |

Apply the verdicts as follows:

- **Company-controlled:** The company sets critical rules or access, controls the customer relationship, data, or a hard-to-bypass bottleneck, and captures material value.
- **Shared or contested:** The company controls important layers, but governance, access, data, or economics are split with other powerful participants.
- **Participant only:** An ecosystem exists, but another party controls its essential rules, customer access, or economics.
- **No meaningful ecosystem:** The business lacks reinforcing third-party participation or feedback loops; integration or partnerships alone do not qualify.

Use 3- to 5-year evidence for the trend when possible. Feed the findings into relevant Five Forces rows—especially network effects, switching costs, distribution access, supplier dependence, substitutes, and rivalry—without double-counting. Do not assign the ecosystem overlay a pressure-on-profitability rating.

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

- Use the latest five completed fiscal years available from public filings.
- Calculate the five-year average from the same five annual values shown in the table.
- If the company reports ROIC, use the reported metric. If not, calculate a clearly labeled ROIC proxy and briefly define the numerator and denominator in the notes/source column.
- If gross margin is not meaningful or not disclosed for the business model, use the closest disclosed equivalent and label it clearly.
- Do not include EBIT margin, free cash flow margin, revenue growth, capex/revenue, or working capital needs in this section unless the user asks for them. Use those metrics elsewhere only when they are directly relevant to a Five Forces sub-point.

### 5. Five Forces Sub-Point Analysis

For each force, include a table. Every listed sub-point must appear as a separate row.

Under each force heading, use this table format:

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|

Apply the Global Conventions. Every listed sub-point must appear as a separate row; do not combine rows or replace the table with a force-level paragraph.

### 6. Overall Force Ratings

After completing the sub-point tables, include a force-level ratings table with one row per force.

Required table format:

| Force | Overall pressure | Confidence | Main drivers | Trend | Stock implication |
|---|---|---|---|---|---|

Include exactly these five rows: New entrants, Suppliers, Buyers, Substitutes, Rivalry. Apply the Global Conventions. Main drivers must identify the most important sub-points behind the rating. Trend must be **Improving / Stable / Worsening**, based on 3- to 5-year evidence when possible.

### 7. Most Important Forces

- Which force matters most?
- Which force is changing fastest?
- Which force is most misunderstood by investors?
- Are current profits protected, temporary, or likely to be competed away?

### 8. Stock-Relevant Takeaways

- Pricing power.
- Margin durability.
- Capital intensity.
- Growth quality.
- Ecosystem control, value capture, and external dependencies.
- Main risks.
- What evidence would change the conclusion.

### 9. Mistakes to Avoid Check

Explicitly state whether the analysis avoided the common mistakes listed at the end of this skill.

---

# Force 1 — Threat of New Entrants

Simple question: **How easy is it for new companies to enter and take profits away?**

RBV lens: Ask whether incumbents hold resources or capabilities that entrants cannot easily buy, hire, license, copy, substitute, or organize around. Treat brands, data, patents, distribution, process know-how, customer relationships, and talent as entry barriers only when they are valuable to customers, rare among competitors, hard to imitate, and embedded in operations.

Analyze every sub-point below.

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

Analyze every sub-point below.

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

Analyze every sub-point below.

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

Before finalizing, verify that **every row defined in the canonical Industry Chain, Ecosystem Control, and Five Forces tables above appears exactly once in its required analysis section**. Add any missing row before giving the final answer.

---

# Final Synthesis Rules

After all sub-points are analyzed, summarize:

1. **Overall industry structure:** attractive, mixed, or unattractive — but explain why.
2. **Controlling force:** the one or two forces that most explain profitability.
3. **Company position:** whether this company is better or worse positioned than peers against each force.
4. **Trend:** whether each force is improving, worsening, or stable.
5. **Stock implications:** how the structure affects pricing power, margins, reinvestment needs, growth quality, and risk.
6. **Disconfirming evidence:** what facts would make the conclusion wrong.
7. **Ecosystem position:** whether the company controls, shares, merely participates in, or lacks an ecosystem; name the controlled bottlenecks, external dependencies, and peer advantage.

Use the **Overall Force Ratings** table in Section 6 as the final force-level summary; do not repeat the same five ratings in a second table. Keep the synthesis and Stock-Relevant Takeaways consistent with that table and the ecosystem verdict; do not add ecosystem as a sixth force row.

---

# Common Mistakes to Avoid

Check these before finalizing the analysis:

1. Do not define competition only as direct competitors.
2. Do not define the industry too broadly or too narrowly.
3. Do not just make lists; explain causes using numbers.
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

---

# Data Source Priority

Use sources in this order when possible:

1. Latest 10-K and 10-Q.
2. Competitor 10-Ks and 10-Qs.
3. Investor presentations and earnings transcripts.
4. Proxy filings for incentives and ownership.
5. Government, regulatory, and trade association data.
6. Reputable industry research and news.
7. Company websites only for basic descriptions, not final proof.

Always cite sources or clearly name where each statistic came from.
