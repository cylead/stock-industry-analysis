# NVIDIA (NASDAQ: NVDA) — Porter Five Forces Analysis

**Research cutoff: August 22, 2026.** Latest reported operating period: Q1 FY2027, ended April 26, 2026. The profitability baseline uses the latest five completed fi
scal years, FY2022–FY2026.

**Bottom line:** The industry structure is **mixed-to-attractive for NVIDIA, but much less attractive for an undifferentiated entrant**. NVIDIA controls the most valuable merchant accelerated-computing bottlenecks—CUDA, GPU architecture, NVLink, system design, and a large developer flywheel—and captures that value in exceptional margins and returns. The offsets are concentrated fabrication/HBM suppliers, increasingly concentrated hyperscale buyers, rapid customer backward integration into custom silicon, and heavy dependence on power, data centers, and cloud distribution. NVIDIA's competitive advantages look durable; the *current magnitude* of profit is less certain than the existence of the advantage.

This is a business-quality and industry-structure analysis, not a valuation, price target, or buy/sell recommendation.

## Source key

- **NV26:** [NVIDIA FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- **NVQ1:** [NVIDIA Q1 FY2027 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)
- **NV24 / NV22:** [NVIDIA FY2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000029/nvda-20240128.htm), [NVIDIA FY2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000036/nvda-20220130.htm)
- **NVEco:** [NVIDIA 2025 Annual Review](https://images.nvidia.com/pdf/Annual-NVIDIA-CEO-Letter-2025.pdf), [August 2026 compute-financing announcement](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Partners-With-Apollo-BlackRock-Blackstone-Brookfield-Goldman-Sachs-and-KKR-to-Establish-AI-Compute-Infrastructure-Financing-Platforms-to-Mobilize-Over-500-Billion-of-Third-Party-Capital/default.aspx)
- **AMD25 / AMDQ2:** [AMD 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/2488/000000248826000021/amd-20251227.htm), [AMD Q2 2026 results](https://ir.amd.com/news-events/press-releases/detail/1295/amd-reports-second-quarter-2026-financial-results)
- **INTC25:** [Intel 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm)
- **TSMC25:** [TSMC 2025 annual report](https://investor.tsmc.com/static/annualReports/2025/english/index.html)
- **GOOG25:** [Alphabet 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm) and [2025 annual-report letter](https://www.sec.gov/Archives/edgar/data/1652044/000130817926000344/goog014907-ars.pdf)
- **AMZN26:** [Amazon 2025 annual-report letter](https://www.sec.gov/Archives/edgar/data/1018724/000110465926041036/tm263815d4_ars.pdf), [Amazon Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm)
- **MSFT26:** [Microsoft FY2026 Form 10-K](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- **JPR:** [Jon Peddie Research Q1 2026 add-in-board report](https://www.jonpeddie.com/news/q126-pc-graphics-add-in-board-shipments-decreased-0-6-from-last-quarter-to-12-million-units-with-a-cagr-to-2029-of-3-3/)

Company claims about relative performance or price-performance are identified as claims rather than independent benchmarks. “Pressure” below means pressure on industry profitability.

## 1. Company Snapshot

- **Company and ticker:** NVIDIA Corporation (NASDAQ: NVDA).
- **What it does:** Designs accelerated-computing platforms spanning GPUs, CPUs, DPUs, networking, rack-scale systems, CUDA/CUDA-X software, libraries, models, APIs, and enterprise software. It is fabless: third parties manufacture and assemble the physical products. [NV26]
- **FY2026 segments:** Compute & Networking was $193.5 billion, or **89.6%** of revenue; Graphics was $22.5 billion, or **10.4%**. [NV26]
- **FY2026 end markets:** Data Center $193.7 billion (**89.7%**), Gaming $16.0 billion (**7.4%**), Professional Visualization $3.2 billion (**1.5%**), Automotive $2.35 billion (**1.1%**), and OEM/Other $0.62 billion (**0.3%**). [NV26]
- **Current buyer mix:** In Q1 FY2027, Hyperscale was $37.9 billion (**46.4%** of company revenue), AI Clouds/Industrial/Enterprise (“ACIE”) $37.4 billion (**45.8%**), and Edge Computing $6.4 billion (**7.8%**). Hyperscalers were approximately half of Data Center revenue, with the other half from AI clouds, industrial, enterprise, and sovereign customers. [NVQ1]
- **Customer concentration:** Three direct customers were **21%, 17%, and 16%** of Q1 FY2027 revenue—54% combined. FY2026's two largest direct customers were 22% and 14%. Exact identities and indirect-customer proportions were not disclosed. [NVQ1, NV26]
- **Geography:** Customers headquartered in the U.S. represented approximately **78%** of Q1 FY2027 revenue; 22% was outside the U.S. Headquarters location can differ from end-user and shipment location. [NVQ1]
- **Supplier/counterparty mix:** Exact purchase proportions are **not found in public filings**. NVIDIA names TSMC and Samsung for wafers; SK hynix, Micron, and Samsung for memory; and Hon Hai, Wistron, and Fabrinet among assembly/test/contract-manufacturing providers. Its manufacturing, supply, and capacity commitments were **$119 billion** at April 26, 2026. [NV26, NVQ1]
- **Main cost drivers:** Wafer fabrication, HBM and other memory, advanced packaging such as CoWoS, assembly/test, boards and systems, yield losses, inventory/warranty provisions, tariffs and shipping; plus talent and compute for R&D. FY2026 R&D was **$18.5 billion**, 8.6% of revenue; 31,000 of 42,000 employees worked in R&D. [NV26]

### Segment buyer and counterparty mix

| Business / segment | Buyer mix and approximate proportion | Sellers / counterparties and proportion proxy | Revenue driver |
|---|---|---|---|
| Data Center / Compute & Networking | Q1 FY2027: Hyperscale **50.3%** and ACIE **49.7%** of Data Center revenue. Direct buyers include CSPs, OEMs, ODMs, system integrators, distributors, and model makers; indirect buyers include AI clouds, enterprises, sovereign/public-sector users, and model makers. [NVQ1] | Wafer, HBM, packaging, systems, and cloud/R&D counterparties. Segment purchase percentages are **not found in public filings**; named-supplier count and the $119 billion commitment balance are the best proxies. [NV26, NVQ1] | GPU compute plus NVLink/InfiniBand/Ethernet networking, rack-scale systems, CUDA software, and enterprise licenses. |
| Graphics / Edge | Q1 FY2027 Edge was **7.8%** of company revenue. FY2026 Gaming was 7.4% and Professional Visualization 1.5%; buyers are gamers, creators, workstations, PC OEMs/AIBs, and cloud-gaming users. [NV26, NVQ1] | AIBs, PC OEMs, distributors, retailers, foundries, memory, and board partners. Exact counterparty proportions are **not found in public filings**. | Architecture transitions, installed PC base, game/application support, RTX/DLSS features, and supply/price availability. |
| Automotive / physical AI | Automotive was **1.1%** of FY2026 revenue; buyers include automakers, tier-1 suppliers, robotaxi and mobility providers, and robotics companies. [NV26] | Foundries, module/board partners, automotive OEMs and tier-1 integrators; exact proportions are **not found in public filings**. | Long design cycles, DRIVE hardware/software adoption, simulation, and deployment volumes. |

## 2. Relevant Industry Definition

- **Primary product scope:** Global merchant accelerated-computing platforms for AI/HPC—processors, interconnects, networking, rack-scale systems, development software, and enterprise support. This is the core economic industry because Data Center generated 89.7% of FY2026 revenue. Gaming/professional graphics and automotive are retained where they materially change the force assessment.
- **Geographic scope:** Global, but segmented by export-control eligibility, data-sovereignty rules, local supply chains, and access to power/data-center infrastructure. NVIDIA reported that it was effectively foreclosed from China's data-center compute market at the end of FY2026. [NV26]
- **Direct competitors:** AMD, Intel, Huawei, and other GPU/accelerator vendors; Broadcom, Marvell, Arista, Cisco and others in networking; AMD and Intel in PC graphics. [NV26]
- **Customer-competitors / backward integrators:** Alphabet TPUs, Amazon Trainium, Microsoft custom accelerators, Alibaba, Baidu, Huawei and other cloud or system companies with internal chip teams. [NV26, GOOG25, AMZN26]
- **Main substitutes:** CPU-only computing; custom ASICs/TPUs/Trainium; FPGAs for specialized or low-volume work; integrated GPUs and game consoles; renting cloud compute instead of owning systems; algorithm/model efficiency that reduces compute per outcome; and “doing nothing” or delaying deployment when ROI is uncertain.
- **Suppliers and sellers:** TSMC/Samsung for wafers; SK hynix/Micron/Samsung for HBM; CoWoS and other advanced packaging; Hon Hai/Wistron/Fabrinet and other assembly/system providers; EDA/IP tools; data centers, electricity, cloud capacity, optical/network components, and specialized engineering labor. Exact NVIDIA spend shares are **not found in public filings**. [NV26]
- **Buyer groups and proportions:** Q1 FY2027 is the best current proxy: Hyperscale 46.4% of company revenue, ACIE 45.8%, and Edge 7.8%. Three direct buyers represented 54%, while direct versus indirect totals were not disclosed. [NVQ1]
- **Seller/counterparty proportions:** The best public proxy is participant concentration, not NVIDIA spend: two named foundries, three named HBM vendors, and three named assembly/test/contract manufacturers. TSMC itself served 534 customers and derived 74% of 2025 wafer revenue from 7nm-and-below technologies, showing both its diversification and the scarcity of advanced production. [NV26, TSMC25]

## 3. Industry Chain and Ecosystem Control

Money moves from hyperscalers, AI clouds, enterprises, consumers, automakers, and public-sector users through CSPs/OEMs/ODMs/distributors to NVIDIA; NVIDIA pays foundries, memory/packaging/system suppliers, cloud/data-center providers, and talent. Product and data flows do not follow the same path: NVIDIA controls architecture and developer interfaces, whereas customers retain most application data, identity, workloads, and end-user relationships.

### Industry-chain map

| Chain layer | Main participants and proportions | Company role and legally owned assets | External dependencies / alternatives | Top statistics or proxies, max 3 | Economic control | Confidence |
|---|---|---|---|---|---|---|
| Critical upstream inputs and capabilities | TSMC/Samsung wafers; SK hynix/Micron/Samsung memory; CoWoS packaging; EDA/IP; specialized talent. Exact NVIDIA spend shares are **not found in public filings**. [NV26] | NVIDIA owns chip/system designs, patents, trade secrets, supplier specifications, and demand forecasts; it does not own high-volume fabs or HBM plants. | Alternative named suppliers exist, but advanced-node, HBM, packaging, and qualification capacity are not freely interchangeable. | $119bn manufacturing/supply/capacity commitments; lead times can exceed 12 months; 31,000 R&D employees. [NVQ1, NV26] | Medium | High |
| Enabling technology and infrastructure | CSPs, data-center operators, utilities, OEM/ODM rack builders, optical/network vendors; hyperscalers were ~50% of Data Center revenue. [NVQ1] | Owns NVLink, InfiniBand/Ethernet products, DPUs/NICs, system architecture, and CUDA software; leases/uses external cloud and data-center capacity for R&D. | Power, permitted data centers, customer capital, cloud capacity, CPUs, optics, and deployment services remain external. | $30bn cloud-service commitments; $32.4bn not-yet-commenced leases; hyperscale 46.4% of Q1 revenue. [NVQ1] | Medium | High |
| Core product, production, or platform | NVIDIA; merchant peers AMD/Intel/Huawei; custom silicon from Alphabet/Amazon/Microsoft and others. | Designs GPUs, CPUs, DPUs, interconnects, networking, rack-scale systems, CUDA/CUDA-X, models, APIs, and enterprise software. Production is outsourced. | AMD ROCm/Instinct, Intel accelerators, Huawei, TPUs/Trainium and other ASICs; external manufacturing is unavoidable. | Data Center 89.7% of FY2026 revenue; Q1 FY2027 gross margin 74.9%; one-year data-center architecture cadence. [NV26, NVQ1] | High | High |
| Distribution and customer access | CSPs, OEMs, ODMs, system integrators, distributors, AIBs, automakers, and retailers. Exact channel shares are **not found in public filings**. | Direct technical sales, solution architects, developer relations, reference systems, GeForce/enterprise brands, and direct software licenses; most physical access is partner-mediated. | Major CSPs and system partners aggregate demand and own cloud/end-user access; they can promote their own silicon. | Top three direct customers 54% of Q1 revenue; U.S.-headquartered buyers 78%; all major public/private clouds are customers. [NVQ1, NV26] | Medium | High |
| Complementary products, services, and aftermarket | Developers, AI frameworks, model makers, ISVs, system integrators, AI clouds, enterprise consultants, financiers, and used/rental GPU markets. | Owns CUDA toolchain, hundreds of libraries/frameworks, AI Enterprise, vGPU, NIMs/models, Omniverse and DRIVE software; supports—but does not own—most third-party applications. | PyTorch/JAX and open models can multi-home; CSPs control rentals; financing and application demand remain external. | >6m developers; 40,000 companies building on NVIDIA; announced financing MOUs target >$500bn over time (not deployed capital). [NVEco] | High | Medium |
| Direct buyers, end users, and outcome owners | Hyperscale 46.4%, ACIE 45.8%, Edge 7.8% of Q1 revenue; consumers, enterprises, governments, and automakers own the outcomes. [NVQ1] | NVIDIA influences developer workflow and system choice, but usually does not own customer data, model IP, application identity, or the end-user relationship. | Buyers can rent, delay, optimize models, use custom/competitor chips, or shift workload among clouds. | Three direct buyers 54%; long-contract RPO only $2.6bn; U.S. buyer headquarters 78%. [NVQ1] | Medium | High |

### Ecosystem-control assessment

| Test | Evidence + up to 3 key statistics/proxies | Interpretation | Control strength | Confidence |
|---|---|---|---|---|
| Chain coverage and integration | NVIDIA spans GPU/CPU/DPU, NVLink/networking, systems, CUDA software and services; Data Center was 89.7% of FY2026 revenue; Blackwell was the majority of Data Center revenue. [NV26] | Full-stack co-design improves performance and time-to-market, but manufacturing, HBM, power, data centers, and customer applications remain outside the company. | High | High |
| Third-party participant depth and diversity | More than 6m developers, 40,000 companies building on the platform, and hundreds of libraries/SDKs; NVIDIA works with all major cloud providers. [NVEco, NV26] | Participation is deep across developers, ISVs, clouds, OEMs, integrators, models, and vertical industries—not merely a reseller list. | High | Medium |
| Governance of standards, APIs, marketplace rules, or access | CUDA runs across NVIDIA GPUs; NVIDIA controls CUDA-X, NVLink and many libraries/APIs; NVLink Fusion allows custom CPUs/XPUs into part of the system. [NV26] | NVIDIA sets critical platform interfaces and release cadence. Open frameworks and Ethernet reduce absolute control, but do not erase CUDA governance. | High | High |
| Control of customer relationships and distribution | NVIDIA has direct engineering/sales relationships, but CSPs/OEMs/distributors mediate much access; three direct customers were 54% of Q1 revenue. [NVQ1] | Customer intimacy is strong, yet the most powerful buyers also own distribution and can steer workloads toward internal accelerators. | Medium | High |
| Control of data, identity, or workflow | NVIDIA controls development tools, optimized libraries, deployment runtimes, and parts of AI/graphics workflow; customers retain data, accounts, applications, and most model IP. | Workflow control creates switching costs, but lack of data/identity ownership prevents end-to-end ecosystem control. | Medium | High |
| Cross-side network effects and feedback loops | Developers create optimized applications that increase GPU utility; a broad installed/cloud base increases developer reach; customer workloads inform new libraries/systems. More than 6m developers and 40,000 participating companies support the loop. [NVEco] | This is a genuine reinforcing ecosystem effect: participation improves customer proposition, availability, switching costs, and performance—not just scale. | High | Medium |
| Complementor dependence, incentives, and multi-homing | Many libraries/apps are CUDA-optimized, but PyTorch, JAX, open models, Ethernet, ROCm and cloud abstractions allow multi-homing; NVIDIA invested $18.6bn in private companies/infrastructure funds in Q1 and had $27bn of investment commitments. [NVQ1] | NVIDIA can subsidize complement growth, while complementors retain alternatives. Investments strengthen demand but also raise capital-allocation and circular-demand concerns. | Medium | High |
| Monetization, value capture, external bottlenecks, and durability | FY2026 gross margin 71.1%, Q1 FY2027 74.9%, and FY2026 Compute & Networking segment operating income $130.1bn; external bottlenecks include TSMC/HBM/power/CSP distribution. [NV26, NVQ1] | Hardware economics show very strong value capture. Durability rests on staying ahead of custom silicon while securing scarce external capacity and proving customer ROI. | High | High |

| Ecosystem verdict | Confidence | Trend | Controlled layers / bottlenecks | External dependencies | Stock implications |
|---|---|---|---|---|---|
| **Shared or contested** | High | **Strengthening** | CUDA/CUDA-X, GPU architecture, NVLink, system co-design, developer workflow, performance libraries, and release cadence | TSMC/Samsung, three HBM vendors, CoWoS, power/data centers, CSP distribution, customer data/models, and buyer capex | Ecosystem rents support pricing and switching costs, but supplier constraints and hyperscaler backward integration mean NVIDIA does not own the whole profit pool. The distinction argues for durable premium economics, not permanently uncontested economics. |

The verdict is “shared or contested,” rather than “company-controlled,” because NVIDIA governs the central compute platform but does not control fabrication, HBM, power, cloud access, customer data, or end demand. The trend is strengthening because the developer/company base, product breadth, networking attachment, and financing/investment links expanded over the last several years; the same expansion increases scrutiny of investment-led demand and customer concentration.

## 4. Profitability Baseline

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Five-year average | Notes/source |
|---|---:|---:|---:|---:|---:|---:|---|
| ROIC proxy | 68.8% | 24.4% | 124.9% | 197.2% | 137.4% | **110.5%** | NOPAT ÷ average invested capital. NOPAT = operating income × (1 − reported income-tax expense/pre-tax income). Invested capital = equity + current/non-current debt − cash − marketable debt securities. Marketable equity investments are retained, making the proxy more conservative. FY2023 includes a tax benefit; NVIDIA's fabless model and customer/supplier financing make the denominator unusually small, so use the level directionally. Calculated from audited data in NV26, NV24 and NV22. |
| Gross margin | 64.9% | 56.9% | 72.7% | 75.0% | 71.1% | **68.1%** | GAAP gross profit ÷ revenue. FY2023 included $2.17bn of inventory charges; FY2026 included the $4.5bn H20 charge and a richer mix of lower-margin full data-center systems. [NV26, NV24, NV22] |

The five-year pattern shows both structural and cyclical effects. CUDA/platform differentiation and a fabless model support exceptional returns, while architecture transitions, export controls, inventory provisions, and systems mix can move gross margin by many points.

## 5. Five Forces Sub-Point Analysis

### Force 1 — Threat of New Entrants

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|
| Supply-side economies of scale | FY2026 revenue $215.9bn; gross margin 71.1% versus AMD's 50% in 2025; NVIDIA committed $119bn to manufacturing/supply/capacity by Q1 FY2027. [NV26, NVQ1, AMD25] | Volume, supplier reservations, shared architectures, software reuse, and learning lower effective unit/system cost. A new fabless designer can outsource production, but cannot instantly recreate NVIDIA's volume economics. | Low | High |
| Demand-side benefits of scale / network effects | More than 6m developers and 40,000 companies build on NVIDIA; all major clouds offer its platform. [NVEco, NV26] | A larger installed/cloud base increases developer reach; more optimized software raises hardware utility. This reinforcing loop is a real entry barrier. | Low | Medium |
| Customer switching costs | CUDA, CUDA-X libraries, model/application optimization, training, integrations, and system design embed NVIDIA in workflows; long-contract RPO was only $2.6bn. [NVQ1] | Contract lock-in is modest relative to quarterly hardware sales, but technical and organizational switching costs can be high. Cloud abstractions and open frameworks lower them over time. | Low | High |
| Capital requirements | FY2026 R&D $18.5bn; 31,000 R&D employees; Q1 FY2027 R&D $6.3bn. [NV26, NVQ1] | Fabrication can be outsourced, but frontier architecture, software, networking, validation, talent, and multi-generation credibility require years and billions. Hyperscalers are the important exception because they already have capital and captive demand. | Low | High |
| Incumbency advantages independent of size | One-year data-center architecture cadence; thousands of software components; 42,000 employees with >80% in technical roles and 3.7% turnover. [NV26] | Architecture/software know-how, developer trust, execution routines, and accumulated compatibility are valuable, rare, hard to copy, and embedded in the organization. | Low | High |
| Unequal access to distribution channels | NVIDIA products are available through major clouds/OEMs/ODMs, but three direct customers represented 54% of Q1 revenue and those same clouds can promote internal chips. [NVQ1, NV26] | An unknown entrant lacks qualification and channel credibility. Access is not exclusive, however, and powerful cloud platforms can sponsor alternatives. | Medium | High |
| Restrictive government policy | Export controls effectively excluded NVIDIA from China data-center compute; FY2026 incurred a $4.5bn H20 charge; patents extend from 2026 to 2045. [NV26] | IP and qualification rules deter copying, but industrial subsidies can fund rivals and export controls can transfer ecosystem growth to foreign competitors. Policy is two-sided rather than a clean NVIDIA barrier. | Medium | High |
| Expected retaliation | NVIDIA had $62.6bn of cash/marketable securities at FY2026; FY2026 R&D rose 43%; it responds on a one-year cadence across hardware, networking, and software. [NV26] | NVIDIA can accelerate roadmaps, bundle systems/software, reserve capacity, invest in complementors, or selectively price. Entrants backed by hyperscaler economics remain less deterrable. | Low | High |

**Force judgment:** Entry pressure is **Low**, but worsening at the margin. Generic startups face formidable barriers; the credible entrants are giant customers with captive workloads, proprietary data, cloud distribution, and very large capex budgets.

### Force 2 — Bargaining Power of Suppliers

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|
| Supplier group is more concentrated than the industry | NVIDIA names two foundries, three HBM suppliers, and three assembly/test/contract manufacturers; TSMC's advanced nodes were 74% of its wafer revenue. [NV26, TSMC25] | Critical supply is concentrated at each bottleneck, particularly leading-edge wafers, HBM qualification, and CoWoS packaging. NVIDIA scale helps, but alternatives are few. | High | High |
| Supplier does not depend heavily on the industry | TSMC served 534 customers and 12,682 products in 2025; nevertheless, HPC/AI is a major growth driver. Exact supplier exposure to NVIDIA is **not found in public filings**. [TSMC25] | Dependence is mutual: suppliers have other customers/end markets, while NVIDIA is a huge and fast-growing offtaker. This tempers but does not remove supplier power. | Medium | Medium |
| Companies face switching costs in changing suppliers | Manufacturing lead times can exceed 12 months; commitments reached $119bn; moving a design requires process, packaging, memory, yield, and system requalification. [NV26, NVQ1] | Switching can delay an architecture and jeopardize yield/reliability. Supplier redundancy is strategic, not frictionless. | High | High |
| Supplier products are differentiated | TSMC offers leading-edge nodes and CoWoS; 3nm was 24% and ≤7nm 74% of its 2025 wafer revenue; HBM is a specialized, qualified input. [TSMC25, NV26] | These inputs are technically differentiated, scarce, and co-designed with the accelerator/system. They capture part of the AI profit pool. | High | High |
| No substitute for supplier input | No commercial NVIDIA GPU ships without foundry capacity, memory, packaging, and assembly; approved alternatives are limited to the named groups. [NV26] | NVIDIA can diversify and redesign, but cannot eliminate frontier manufacturing or HBM. In the short run there is no practical substitute. | High | High |
| Supplier can integrate forward | TSMC explicitly operates a pure-play model and does not design branded chips; Samsung already participates in components/systems, while other memory/assembly suppliers have not disclosed credible CUDA-class platforms. [TSMC25, NV26] | Forward integration is a limited threat because it creates customer conflict and requires a software/developer ecosystem. Samsung is the main partial exception. | Low | High |

**Force judgment:** Supplier pressure is **High**. NVIDIA's purchasing scale and architecture influence are unusually strong, but the economic question is whether a short list of suppliers can constrain output or raise total system cost. The $119 billion commitment balance and >12-month lead-time disclosure show that they can.

### Force 3 — Bargaining Power of Buyers

#### Part A — Buyer negotiating leverage

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|
| Few buyers or large-volume buyers | Three direct customers were 21%, 17%, and 16% of Q1 FY2027 revenue; hyperscale was 46.4% of company revenue. [NVQ1] | Concentration gives the largest buyers forecasting, configuration, allocation, and price leverage. Indirect concentration may be higher because one end user can buy through several direct customers. | High | High |
| Products are standardized or undifferentiated | Q1 gross margin was 74.9%; CUDA plus GPU/network/system co-design is differentiated; AMD 2025 gross margin was 50%. [NVQ1, AMD25] | The product is not a commodity. Comparable peak FLOPS do not equal compatible software, cluster networking, availability, reliability, or time-to-solution. | Low | High |
| Buyers face few switching costs | CUDA-optimized code, libraries, staff skills and deployment tooling raise switching costs, although RPO was only $2.6bn and cloud APIs/open frameworks support multi-homing. [NVQ1] | Economic switching cost is higher than contractual lock-in. It is greatest for complex training/HPC and lower for standardized inference behind a cloud service. | Low | High |
| Buyers can integrate backward | Alphabet is shipping its seventh-generation TPU and planned ~$180bn 2026 capex; Amazon said Trainium/Graviton exceeded a $10bn run rate in late 2025 and Trainium2 had 1.4m chips deployed; NVIDIA lists major clouds as competitors. [GOOG25, AMZN26, NV26] | The largest buyers have capital, workloads, distribution, and data to design chips optimized for their own economics. They need not replace NVIDIA universally to cap its share or margins. | High | High |

#### Part B — Buyer price sensitivity

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|
| Product is a large part of buyer cost | Amazon expected roughly $200bn of 2026 capex and Alphabet ~$180bn, mostly driven by infrastructure; NVIDIA manufacturing commitments reached $119bn. [AMZN26, GOOG25, NVQ1] | Accelerators and associated systems are a major capital cost, so even cash-rich buyers aggressively optimize price-performance and asset utilization. | High | Medium |
| Buyer group has low profits or cash pressure | Microsoft Cloud gross margin was 66% in FY2026; large hyperscalers have strong cash generation, while neoclouds/model startups rely more on financing. [MSFT26, NVQ1] | Large buyers can pay for scarce capacity and value speed-to-market; less-capitalized AI clouds are more price-sensitive and can delay or rent. Mixed group economics reduce the rating. | Medium | Medium |
| Buyer quality is not strongly affected by the product | NVIDIA says Rubin could reduce cost per token by up to 10x versus Blackwell; its systems determine throughput, reliability, model time-to-market, graphics quality, and automotive safety. [NV26] | Product choice strongly affects the buyer's output quality and competitiveness. That reduces willingness to switch solely for price. The 10x figure is a company claim, not an independent benchmark. | Low | High |
| Product has little effect on buyer’s other costs | NVIDIA sells on total cost of ownership, performance per watt, cluster scale, and time-to-solution; Amazon claims Trainium2 had ~30% better price-performance than comparable GPUs. [NV26, AMZN26] | Both sides compete on total cost, not chip price. Strong customer ROI supports NVIDIA pricing, while credible custom-chip savings create a ceiling. | Medium | Medium |
| Intermediate customers influence end customers | CSPs/OEMs/ODMs/system integrators/distributors mediate sales; three direct customers were 54% of Q1 revenue; cloud providers own billing, capacity allocation, and many end-user relationships. [NVQ1, NV26] | Intermediaries are powerful gatekeepers even though end users often request NVIDIA. Cloud platforms can price instances and steer standardized workloads to internal silicon. | High | High |

**Force judgment:** Buyer pressure is **Medium**. Concentration and backward integration are high-pressure factors; differentiation, developer pull, time-to-market, and switching costs are strong offsets. The rating would move to High if custom silicon won broad third-party workloads, not merely captive inference.

### Force 4 — Threat of Substitutes

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|
| Substitute has attractive price-performance | Amazon claims Trainium2 delivered ~30% better price-performance than comparable GPUs; its custom-chip run rate exceeded $20bn by Q1 2026; Alphabet offers seventh-generation TPU alongside NVIDIA GPUs. [AMZN26, GOOG25] | ASICs can beat general GPUs on stable, high-volume workloads; CPUs/FPGAs/integrated GPUs fit other niches. NVIDIA retains breadth, programmability, and faster workload coverage. | Medium | Medium |
| Buyer switching cost to substitute is low | CUDA workflows and skills raise migration cost, but cloud services, compilers, PyTorch/JAX, standardized model formats and new greenfield inference reduce it; long-contract RPO was only $2.6bn. [NVQ1] | Switching is costly for mature CUDA estates, but much easier for new workloads abstracted behind managed services. Pressure varies sharply by workload. | Medium | High |
| Changes in other industries make substitutes stronger | Hyperscaler capex is funding custom silicon; open-source models can run on competitor platforms; AMD Data Center revenue grew 107% YoY to $6.7bn in Q2 2026. [GOOG25, AMZN26, AMDQ2, NVQ1] | Compiler improvement, open frameworks/models, and massive buyer capex are improving substitute usability and scale faster than in the prior five years. | High | High |

**Force judgment:** Substitute pressure is **Medium and worsening**. Custom silicon is strongest in predictable, high-volume inference and captive cloud workloads; NVIDIA is strongest where programmability, fast model change, broad availability, and end-to-end scale matter.

### Force 5 — Rivalry Among Existing Competitors

#### Part A — Intensity of rivalry

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|
| Many competitors or similar size competitors | FY2026 NVIDIA Data Center revenue was $193.7bn; AMD's 2025 Data Center revenue was $16.6bn and included CPUs; Intel total 2025 revenue was $52.9bn. [NV26, AMD25, INTC25] | There are many technical rivals, but no similar-sized merchant accelerated-computing platform. Concentration protects current profit while inviting entry. | Low | High |
| Slow industry growth | NVIDIA Data Center grew 68% in FY2026 and 92% YoY in Q1 FY2027; AMD Data Center grew 107% YoY in Q2 2026. [NV26, NVQ1, AMDQ2] | Rapid demand lets multiple vendors grow without pure share stealing. Growth can mask weak customer ROI and future overcapacity, so it is not proof of permanent attractiveness. | Low | High |
| High exit barriers | NVIDIA capex was only $6.1bn (2.8% of revenue), but R&D was $18.5bn; supplier fabs/packaging and customer data centers have large dedicated assets. [NV26] | NVIDIA's fabless balance sheet lowers physical exit barriers, while sunk software/R&D and ecosystem commitments keep rivals engaged. Upstream/downstream fixed assets can sustain capacity after returns fall. | Medium | High |
| Rivals are highly committed to the business | AMD spent $8.1bn on 2025 R&D; Alphabet planned ~$180bn 2026 capex; Amazon spent $96.3bn cash capex in H1 2026. [AMD25, GOOG25, AMZN26] | Rival investment is strategic to cloud economics and national/technology leadership, so it may continue even at initially weak chip-level returns. | High | High |
| Firms cannot read each other’s signals well | Competitors include merchant chip vendors, vertically integrated clouds, telecom/network firms, and state-supported Chinese companies; NVIDIA itself lists all of these groups. [NV26] | Different objectives, transfer pricing, captive demand, bundles, and regulation make capacity and pricing signals difficult to interpret. | High | High |

#### Part B — Basis of rivalry

| Sub-point | Evidence + up to 3 statistics/proxies | Interpretation | Pressure | Confidence |
|---|---|---|---|---|
| Rivalry focuses on price | NVIDIA gross margin was 71.1% in FY2026 and 74.9% in Q1 FY2027; AMD 2025 gross margin was 50%; both emphasize performance and roadmap rather than broad price cuts. [NV26, NVQ1, AMD25] | Current competition is mainly price-performance, availability, and ecosystem—not a commodity price war. Custom silicon creates an internal-cost benchmark that can pressure pricing. | Low | High |
| Products are nearly identical and switching costs are low | CUDA/software, memory, networking, system topology, performance, power, availability, and support differ materially; migration requires code and operational work. [NV26] | Differentiation and switching costs keep rivalry from collapsing into price alone. Managed inference and framework abstraction make some workloads more similar. | Low | High |
| Fixed costs are high and marginal costs are low | NVIDIA FY2026 R&D was $18.5bn and Q1 FY2027 R&D $6.3bn; fabrication and data-center partners carry additional high fixed costs. [NV26, NVQ1] | Chip design/software have high upfront cost and low incremental software cost, encouraging volume competition. Physical systems retain meaningful marginal component cost. | Medium | High |
| Capacity must be expanded in large chunks | NVIDIA commitments rose to $119bn; supplier lead times can exceed 12 months; customer data centers require multi-year power/construction projects. [NVQ1, NV26] | Lumpy capacity and long forecasts create shortage/oversupply cycles, worsening price and inventory risk when demand misses. | High | High |
| Product is perishable | One-year architecture cadence; FY2026 provisions for inventory/excess purchase obligations were $7.2bn; the H20 export-control charge was $4.5bn. [NV26] | Hardware loses economic value quickly when a new architecture or regulation arrives, creating write-down and discount risk. | High | High |
| Non-price competition | NVIDIA uses a one-year architecture cadence and spent $18.5bn on R&D; AMD spent $8.1bn; competition spans performance, power, networking, software, support, and availability. [NV26, AMD25] | Non-price innovation can expand the market and preserve differentiation, but it requires relentless reinvestment and execution. | Medium | High |
| Zero-sum vs positive-sum rivalry | NVIDIA and AMD both posted rapid Data Center growth; networking, inference, sovereign AI, robotics, and edge uses are expanding; PC AIB shipments were 11.8m in Q1 2026 but JPR forecasts a −3.3% 2024–2029 CAGR. [NVQ1, AMDQ2, JPR] | AI infrastructure is currently positive-sum, while mature gaming/PC pockets are closer to zero-sum. Rivalry will intensify if AI demand growth slows before committed capacity does. | Medium | High |

**Force judgment:** Rivalry pressure is **Medium and worsening**. NVIDIA's scale lead and rapid market growth prevent a High rating today; strategic custom-chip investment, AMD's acceleration, heterogeneous business models, and lumpy capacity point to greater pressure over time.

## 6. Overall Force Ratings

These are economically weighted judgments, not simple row averages.

| Force | Overall pressure | Confidence | Main drivers | Trend | Stock implication |
|---|---|---|---|---|---|
| New entrants | Low | High | CUDA/developer flywheel, R&D/talent, supply scale, architecture cadence; offset by hyperscalers with capital and captive demand | Worsening | The moat should remain meaningful, but more value may migrate to customer-designed silicon in standardized workloads. |
| Suppliers | High | High | Few advanced foundry/HBM/packaging options, high requalification cost, >12-month lead times, $119bn commitments | Worsening | Growth and gross margin depend on securing scarce capacity without absorbing disproportionate input cost or inventory risk. |
| Buyers | Medium | High | Three direct buyers at 54%, gatekeeper CSPs and backward integration versus differentiated product, switching costs and high customer ROI | Worsening | Concentration can raise volatility and cap pricing even while developer pull protects share. |
| Substitutes | Medium | High | Trainium/TPUs/custom ASICs, cloud abstraction and open software versus CUDA breadth and programmability | Worsening | Inference mix and workload portability matter more than headline accelerator market growth. |
| Rivalry | Medium | High | Huge NVIDIA scale lead and fast growth versus strategic rival capex, AMD growth, lumpy capacity and rapid obsolescence | Worsening | Current margins are protected better than peers', but the reinvestment rate and risk of normalization are rising. |

## 7. Most Important Forces

- **Which force matters most?** The interaction of **low entry pressure** and the CUDA ecosystem explains NVIDIA's extraordinary value capture. Supplier power is the largest current negative because it can constrain revenue before competitors take share.
- **Which force is changing fastest?** **Substitutes/buyer backward integration.** Amazon's deployed Trainium base, Alphabet's seventh-generation TPU, and enormous hyperscaler capex show that custom silicon is no longer a laboratory project. It is still a workload-specific substitute, not a universal CUDA replacement.
- **Which force is most misunderstood?** **Buyer power.** Concentrated cloud buyers can both buy NVIDIA and design a substitute. That single fact affects buyer leverage and substitution, but it should not be counted twice when judging total industry economics. Their best negotiating tool is a credible internal alternative, not merely order size.
- **Are current profits protected, temporary, or likely to be competed away?** The existence of an above-average profit pool is structurally protected by software, workflow, supply scale, execution, and developer demand. A five-year gross-margin average of 68.1% supports that conclusion. The latest ~75% quarterly gross margin and triple-digit ROIC should not be assumed permanent: mix, scarcity, export controls, customer concentration, and custom silicon can normalize the *level* without destroying the moat.

Overall industry structure is **mixed-to-attractive for NVIDIA**: entry is hard and products are differentiated, but suppliers are powerful and the largest buyers are simultaneously distributors, customers, financiers, and competitors. NVIDIA is better positioned than merchant peers against every force except upstream supply, where its scale improves allocation but cannot manufacture an alternative to leading-edge wafers, HBM, and packaging.

## 8. Stock-Relevant Takeaways

- **Pricing power:** Strong, evidenced by a 71.1% FY2026 and 74.9% Q1 FY2027 gross margin despite a growing mix of complete systems. The best evidence is sustained economics alongside volume, not company performance claims alone.
- **Margin durability:** Above-peer margins are durable; the exact current level is not. Full-system mix, HBM/foundry pricing, export-control inventory charges, warranty/yield, and custom-chip competition can move gross margin materially.
- **Capital intensity:** Corporate capex looks low at 2.8% of FY2026 revenue because NVIDIA is fabless, but economic capital intensity is shifted into $119bn of supply commitments, $30bn of cloud commitments, future R&D leases, supplier fabs, and customer data centers. Reported capex understates ecosystem-wide reinvestment.
- **Growth quality:** Current growth is broadening from hyperscale: ACIE was nearly half of Q1 Data Center revenue. Quality is weakened by 54% direct-customer concentration, investment/financing links to ecosystem participants, and the need for end customers to monetize very large AI infrastructure bills.
- **Ecosystem control and value capture:** NVIDIA controls CUDA, developer workflow, architecture, NVLink, and system co-design and captures substantial value. It shares the ecosystem with fabs/HBM suppliers, clouds, model makers, financiers, and application owners; it does not control power, customer data, or end demand.
- **Main risks:** AI infrastructure overbuild; a sharp inference shift to custom ASICs; three-customer concentration; TSMC/HBM/CoWoS or power constraints; annual product-transition errors; export controls and China ecosystem loss; regulatory remedies affecting bundling/allocation/investments; investment-led or circular demand; open software improving portability; and failure of customers to earn acceptable returns.
- **Evidence that would strengthen the conclusion:** Stable gross margin near or above the five-year average through a demand slowdown; ACIE/enterprise diversification without greater credit support; sustained developer/application growth; high utilization and resale values for successive architectures; and NVIDIA retaining broad inference workloads despite custom chips.
- **Evidence that would weaken or reverse it:** Several quarters of share loss in merchant accelerators; hyperscalers moving material third-party workloads—not just captive inference—to internal chips; CUDA migration becoming routine; gross margin below the five-year average absent one-off charges; customer concentration rising further; repeated inventory/purchase-obligation charges; or suppliers capturing a growing share of system economics.

## 9. Mistakes to Avoid Check

| Common mistake | Avoided? | How |
|---|---|---|
| Define competition only as direct competitors | Yes | Included customer-designed ASICs, CPU/FPGA alternatives, cloud rental, integrated graphics, and delaying deployment. |
| Define the industry too broadly or narrowly | Yes | Anchored the force ratings to merchant accelerated-computing platforms because Data Center is ~90% of revenue, while retaining smaller markets where their economics differ. |
| Make lists without explaining causes using numbers | Yes | Every required row links facts/proxies to a profitability mechanism. |
| Give every force equal weight | Yes | Entry/ecosystem control explain the profit pool; supplier power and custom silicon are the main offsets. |
| Confuse effect with cause | Yes | Buyer and supplier pressure are tied to concentration, switching, qualification, cost importance, and vertical integration. |
| Assume fast growth means an attractive industry | Yes | Rapid AI growth is separated from supply commitments, customer concentration, overbuild, and profit durability. |
| Assume advanced technology means an attractive industry | Yes | Technology matters only when paired with ecosystem control, switching costs, manufacturing access, customer ROI, and value capture. |
| Treat government as a sixth force | Yes | Export controls, patents, subsidies, tariffs, AI rules, and antitrust are incorporated into entry, rivalry, buyer access, and supplier risk. |
| Treat complements as a sixth force | Yes | Developers, frameworks, models, clouds, financing, and networking feed entry, switching, distribution, substitutes, and rivalry. |
| Rely on one-year results | Yes | Used five completed fiscal years and 3–5 year directional evidence; Q1 FY2027 is a current pulse only. |
| Assume consolidation automatically fixes rivalry | Yes | Strategic cloud, state-backed, networking, and custom-chip rivals can invest even without a standalone merchant share. |
| Use the framework only to label the industry good/bad | Yes | Connected structure to pricing, margins, capital commitments, growth quality, and disconfirming evidence. |
| Call vertical integration or a product suite an ecosystem | Yes | Required reinforcing third-party participation and documented the developer/application/cloud feedback loop. |
| Infer ecosystem control from partner counts alone | Yes | Tested governance, workflow/data, customer access, multi-homing, bottlenecks, and monetization separately. |
| Confuse participation in another ecosystem with control | Yes | Distinguished NVIDIA-controlled CUDA/NVLink from CSP-controlled cloud access and supplier-controlled manufacturing capacity. |

### Completion check

All **6** industry-chain layers, **8** ecosystem-control tests, and **38** canonical Five Forces sub-points appear once in their required analysis tables. Ratings are weighted judgments, and facts are separated from interpretation. Method followed: [SKILL.md](../SKILL.md).
