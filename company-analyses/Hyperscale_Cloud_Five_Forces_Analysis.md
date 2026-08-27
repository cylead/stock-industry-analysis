# Hyperscale Public Cloud (AWS, Microsoft Azure, Google Cloud) — Porter Five Forces Analysis

**Information cutoff:** 13 August 2026  
**Financial period used:** calendar FY2021–FY2025 where available (Microsoft's FY ends 30 June)  
**Rating convention:** *Impact* and *overall pressure* mean pressure on **industry profitability**. A low score is favorable for cloud-provider profitability; it does **not** mean low importance to customers. Facts and source-linked data are separated from analytical judgments.

## Bottom line

Public cloud is usually favored over a traditional customer-owned data center because it turns a large, slow, and often under-used infrastructure investment into **on-demand, pooled capacity**, managed services, and global resilience. A customer can launch a workload in minutes, scale it down when demand falls, use advanced databases/security/AI without building the underlying platform, and pay for measured use. NIST's definition captures the core mechanisms: on-demand self-service, resource pooling, rapid elasticity, and measured service. [NIST]

That customer value does **not** mean cloud is automatically the cheapest option. A stable, predictable, high-utilization workload on already-depreciated hardware can be cheaper in an owned or colocated data center. Migration, redesign, data transfer, and ongoing usage management are real costs. The best economic answer is often hybrid or multi-cloud rather than "everything in one public cloud." Recent GAO evidence is useful here: cloud can be quicker and possibly cheaper than building and operating infrastructure, but 17 of 24 federal agencies reported difficulty controlling cloud costs. [GAO26]

For providers, the structure is **mixed but attractive for the three hyperscalers** and much less attractive for a new general-purpose entrant. The same scale that creates customer value—pooled demand, global networks, specialized chips, security certification, and a broad managed-service catalog—creates formidable entry barriers. The hard part is that AWS, Azure, and Google Cloud also compete intensely, are spending heavily on AI capacity, and rely on concentrated suppliers of accelerators, power, networking, and data-center inputs.

**Overall conclusion:** AWS is best positioned on global scale and standalone cloud profitability; Azure has the strongest enterprise distribution and software bundle; Google Cloud is smaller but has strong AI/data differentiation and fast improvement in cloud profitability. The controlling forces are **rivalry** and **supplier/power availability**, not simple customer demand.

## 1. Company snapshot

| Provider / parent | What it sells | FY2025 public scale | Main buyers and revenue model | Main cost drivers | Relative position |
|---|---|---:|---|---|---|
| **AWS / Amazon (AMZN)** | IaaS, PaaS, storage, databases, analytics, security, AI, edge and support | **$128.7bn** AWS sales; **$45.6bn** segment operating income; 18% of Amazon revenue | Enterprises, digital-native firms, public sector and software vendors. Mostly usage-based fees, with committed-use/reserved-capacity discounts and support. Buyer-size split is **not disclosed**. | Servers/accelerators, data centers, power, networking, depreciation, engineering and sales/support | Largest independent cloud platform and broadest mature ecosystem. |
| **Azure / Microsoft (MSFT)** | Azure IaaS/PaaS/AI plus hybrid tooling; sold alongside Microsoft 365, Dynamics, GitHub, Windows Server and security | Azure revenue surpassed **$75bn** in Microsoft FY2025; Azure and other cloud services grew **34%**. Azure-only operating income is **not disclosed**. | Large enterprises, governments and developers. Consumption, enterprise agreements and software bundles. Customer-size split is **not disclosed**. | Same infrastructure inputs, plus software R&D, enterprise sales and partner channel | Strongest installed enterprise distribution and bundle/identity advantage. |
| **Google Cloud / Alphabet (GOOGL)** | GCP infrastructure, data/analytics, cyber security, AI/Vertex/Gemini, plus Workspace | **$58.7bn** segment revenue; **$13.9bn** segment operating income. Segment includes GCP and Workspace, so it is broader than infrastructure cloud alone. | Enterprises, developers, public sector and data/AI-centric firms. Consumption plus subscriptions. Buyer-size split is **not disclosed**. | Servers/accelerators (including TPUs), data centers, networking, technical infrastructure and engineering | Smaller share, but strong data/AI stack and proprietary TPU option; cloud margin has improved sharply. |

The relevant global market is **public cloud infrastructure and platform services**: IaaS, PaaS and hosted private-cloud infrastructure, plus the managed data/AI services that make these platforms valuable. It is *not* all SaaS, all IT outsourcing, or all data-center hardware. Synergy estimated 2025 cloud-infrastructure-service revenue of **$419bn**; AWS, Azure and Google Cloud together represented about **68%** of Q4 2025 spend (AWS **28%**, Azure **21%**, Google **14%**). [SYNERGY]

### Buyer, counterparty and channel mix

| Group | Approximate proportion / proxy | What it means |
|---|---|---|
| Large enterprises and public sector | The economically important minority by spend; exact provider revenue shares are **not found in public filings**. UK public-cloud buyers spent about **£9bn** in 2023, and the CMA describes financial services, retail, startups and public services as key buyer groups. [CMA25] | Large procurement teams have leverage on price and terms, especially for committed spending. |
| Smaller enterprises, developers and digital natives | Large in account count; exact revenue share **not disclosed** | They value self-service and speed, but are individually fragmented and have less negotiating leverage. |
| Direct versus indirect/channel sales | Exact shares **not disclosed**. Systems integrators, managed-service providers, resellers and independent software vendors influence design, migration and purchasing. | The providers own the infrastructure relationship, but channels influence workload placement and cost. |
| Supplier/counterparty groups | Semiconductors/accelerators, servers/network gear, electricity, data-center developers/landlords, telecom/network providers, model providers, and engineering labor | These groups matter more as AI raises the share of scarce compute and power. |

## 2. Why customers favor cloud over the traditional way

| Decision dimension | Public cloud | Customer-owned / traditional data center | Economic implication |
|---|---|---|---|
| Up-front commitment | Rent capacity as needed; usage is metered | Buy/lease servers, network, facilities and staff before demand is proven | Cloud reduces the irreversible initial commitment and preserves cash, particularly for uncertain demand. |
| Utilization and scale | Provider pools many customers' peaks and can add capacity across regions | One company must provision for its own peak and refresh cycles | Pooling usually lifts utilization and reduces idle-capacity risk; this is the fundamental cloud advantage. |
| Speed and innovation | Self-service provisioning; managed databases, security, data and AI services | Procurement, installation, upgrades and internal operations take longer | Faster experiments and product launches can be more valuable than a small unit-cost difference. |
| Reliability and reach | Multiple regions/AZs, global network and compliance tooling already available | Customer must build and test redundancy, disaster recovery and local presence itself | Hyperscalers spread the fixed cost of resilience and compliance over a huge base. |
| Cost transparency | Detailed metering, but many service, storage and data-transfer meters | Capex can hide utilization, depreciation, staff and facility cost; budgeting is more familiar | Cloud needs active FinOps/cost discipline. It is not a blank cheque. [GAO26] |
| Best use case | Variable/fast-growing demand, global services, modern apps, data/AI, limited infrastructure staff | Steady high-utilization workloads, special sovereignty/latency needs, depreciated assets or unusual hardware | Hybrid is often rational; “cloud first” should not be “cloud only.” |

**A simple economic test:** compare *three-to-five-year total cost of ownership* (hardware/facility/power/network/staff/refresh, utilization and downtime risk) with cloud run-rate **after** rightsizing, reserved-capacity discounts, data-transfer costs, migration/rebuild cost and staff productivity. Do not compare an on-premise server's sunk purchase price only with a cloud list price.

## 3. Profitability baseline

Cloud-segment **ROIC and gross margin are not disclosed** by all three providers, and allocating parent-company assets or cost of revenue to a cloud segment would be misleading. The table therefore shows the closest consistently disclosed profitability proxy, *segment operating margin*. This is not a gross margin and should not be read as a like-for-like comparison: Google Cloud includes Workspace and Microsoft does not disclose Azure-only segment profit.

| Metric | 2021 | 2022 | 2023 | 2024 | 2025 | Five-year average | Notes/source |
|---|---:|---:|---:|---:|---:|---:|---|
| ROIC / return on invested capital — AWS | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not calculable | AWS does not disclose segment operating assets or a segment ROIC. Using Amazon consolidated ROIC would not describe AWS. [AMZN25] |
| Gross margin — AWS | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not calculable | Amazon explicitly uses operating income rather than gross profit because of its varied product/service mix. [AMZN25] |
| **Closest disclosed proxy: AWS segment operating margin** | **29.8%** | **28.5%** | **27.1%** | **37.0%** | **35.4%** | **31.6%** | Calculated as disclosed AWS operating income / AWS sales; 2021–24 figures are from prior Amazon 10-Ks and 2025 from [AMZN25]. |
| ROIC / return on invested capital — Google Cloud / Azure | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not calculable | Google and Microsoft do not disclose standalone cloud-segment invested capital; Azure-only results are not disclosed. [GOOG25] [MSFT25] |
| Gross margin — Google Cloud / Azure | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not disclosed | Not calculable | Neither company discloses a standalone cloud gross margin. Google Cloud includes Workspace; Microsoft’s Intelligent Cloud includes more than Azure. [GOOG25] [MSFT25] |
| **Closest disclosed proxy: Google Cloud segment operating margin** | **-16.1%** | **-7.1%** | **5.2%** | **14.1%** | **23.7%** | **4.0%** | Calculated from reported segment revenue and operating income; useful for direction, but it includes Workspace and allocated costs. [GOOG25] |

**Interpretation:** AWS shows that a scaled cloud platform can produce substantial reported operating profit, while Google Cloud's move from loss to 23.7% segment operating margin shows the importance of utilization and scale. The figures do *not* prove that future AI capacity will earn the same return: depreciation, power and accelerator spend are rising quickly.

## 4. Five Forces sub-point analysis

### Force 1 — Threat of new entrants

| Force | Sub-point | Evidence found | Top statistics / proxies (max 3) | Interpretation | Impact | Confidence |
|---|---|---|---|---|---|---|
| New entrants | Supply-side economies of scale | Hyperscalers pool infrastructure demand, buy at large volume, operate global networks and design custom chips. AWS had 111 AZs in 35 regions by early 2025; Google offers proprietary TPUs; cloud market is concentrated. [AWSREG] [GOOG25] [SYNERGY] | AWS 111 AZs/35 regions; top 3 68% Q4 share; $419bn 2025 market | A new general cloud cannot match purchasing, utilization, network and learning economies just by leasing a few data centers. | **Low** | **High** |
| New entrants | Demand-side benefits of scale / network effects | There is no pure consumer network effect, but scale produces a deeper marketplace, partner base, certified integrations, skills pool and service catalog. Public provider ecosystem counts are not comparable. [CMA25] | Top 3 68% share; 2025 market $419bn; AWS 111 AZs/35 regions | Indirect network effects reinforce the cost advantage: more users attract more software/partners and create more operational learning. | **Low** | **Medium** |
| New entrants | Customer switching costs | Customers must move data, rebuild integrations, retrain teams and retest security/compliance. The CMA found egress fees and interoperability barriers restrict switching and multi-cloud. [CMA26] | 68% top-3 share; egress/interoperability barriers confirmed; EU switching-charge ban begins 12 Jan 2027 | Switching protects an installed workload, though it does not stop entrants winning new workloads. | **Low** | **High** |
| New entrants | Capital requirements | New providers need land, power, data centers, servers/accelerators, global network, security operations and years of software/service development. The CMA found very large capital investment is a significant entry/expansion barrier. [CMA25] [MSFT25] [GOOG25] | Microsoft FY2025 depreciation $22.0bn; Alphabet 2026 capex plan $175–185bn; AWS 2025 sales $128.7bn | This is the decisive barrier for a broad hyperscale competitor. AI makes it larger, not smaller. | **Low** | **High** |
| New entrants | Incumbency advantages independent of size | AWS has long operating history; Azure has enterprise identity, Windows/SQL/GitHub/Office links; Google has data/AI expertise and TPUs. These are embedded capabilities, not just brands. [MSFT25] [GOOG25] | Azure revenue >$75bn FY2025; GCP/Workspace revenue $58.7bn; AWS margin 35.4% | Each leader has a distinct resource system that is hard to copy quickly. | **Low** | **High** |
| New entrants | Unequal access to distribution channels | Azure starts with Microsoft enterprise agreements and software partners; AWS and Google have extensive direct, partner and marketplace channels. Exact channel revenue shares are not disclosed. [MSFT25] [CMA25] | Azure +34% FY2025; 68% top-3 market share; £9bn UK buyer market in 2023 | A technically good entrant still has to gain CIO trust, procurement access and implementation partners. Azure is strongest here. | **Low** | **Medium** |
| New entrants | Restrictive government policy | Security authorizations, data residency, sovereignty, privacy and procurement certifications slow entry. FedRAMP authorizations among 24 U.S. agencies rose about 60% from Jul-2019 to Apr-2023. [GAO24] | +60% federal authorizations; EU Data Act applies Sep-2025; AWS 35 regions | Policy can also open markets by mandating portability, but compliance history favors established providers. | **Low** | **High** |
| New entrants | Expected retaliation | Leaders can respond with credits, reserved-use discounts, product releases, bundling and enormous capital/R&D. They are currently expanding capacity rather than harvesting profits. [CMA25] [AMZN25] [MSFT25] | AWS sales +20% in 2025; Azure +34% FY2025; Google Cloud revenue +36% in 2025 | An entrant should expect fast matching and aggressive commercial responses in strategic accounts. | **Low** | **High** |

**Force judgment:** **Low pressure, High confidence, Stable.** Starting a focused GPU cloud, sovereign cloud or managed-service business is feasible; starting a credible global, general-purpose AWS/Azure/GCP alternative is not. AI creates niches for entrants but raises the capital and power hurdle for the broad market.

### Force 2 — Bargaining power of suppliers

| Force | Sub-point | Evidence found | Top statistics / proxies (max 3) | Interpretation | Impact | Confidence |
|---|---|---|---|---|---|---|
| Suppliers | Supplier group is more concentrated than the industry | Critical AI accelerators, advanced networking, power interconnection and suitable data-center sites are scarcer and more concentrated than cloud providers’ buyer base. Exact supplier HHI and contracts are not public. [MSFT25] [GOOG25] | Microsoft depreciation $22.0bn; Alphabet expects sharply higher 2026 infra spend; 3 hyperscalers = 68% share | Accelerator and power suppliers can capture value during shortages, particularly for AI. | **High** | **Medium** |
| Suppliers | Supplier does not depend heavily on the industry | Chip, server, networking, power and real-estate suppliers sell to many cloud firms, enterprises, governments and other industries. Supplier revenue exposure is **not found in the providers’ filings**. | $419bn cloud market; 3 top buyers; broad non-cloud demand proxy | The very largest clouds are important customers, but the critical inputs have alternative buyers, limiting cloud leverage. | **Medium** | **Medium** |
| Suppliers | Companies face switching costs in changing suppliers | Hardware/software stacks, power contracts, data-center design and developer tools are tied to chosen architectures. AWS, Azure and Google mitigate this with custom chips and multiple vendors, but migration takes time. [GOOG25] [MSFT25] | Google seventh-generation TPU; Microsoft 2025 depreciation $22.0bn; AWS 111 AZs | Multi-sourcing is possible over product cycles, not instantly when capacity is scarce. | **High** | **Medium** |
| Suppliers | Supplier products are differentiated | Leading accelerators and advanced networking are technologically differentiated. Google’s custom TPU is direct evidence that owning part of the stack is strategically valuable. [GOOG25] | Google 7th-gen TPU; Google Cloud 2025 revenue $58.7bn; 2026 capex plan $175–185bn | Differentiated compute allows suppliers to command premium pricing; custom silicon is a key defense. | **High** | **High** |
| Suppliers | No substitute for supplier input | Data centers cannot operate without power, network, servers and skilled technical labor. CPU/TPU/alternative GPU choice offers partial substitution; it does not remove the need for compute. [GOOG25] [AWSREG] | AWS 111 AZs; Google offers GPUs + TPUs; Microsoft depreciation $22.0bn | Provider design choices can lower dependence on a single chip, but not on physical capacity and energy. | **High** | **High** |
| Suppliers | Supplier can integrate forward | Chip and model suppliers can offer managed compute/model APIs; data-center owners can lease capacity. But reproducing a global service catalogue, security posture and enterprise channel is much harder. [NIST] [CMA25] | 68% top-3 share; £9bn UK buyer market; very large capex barrier | Forward integration is credible in AI/compute niches, but less credible as a full hyperscaler replacement. | **Medium** | **Medium** |

**Force judgment:** **Medium pressure, Medium confidence, Worsening.** Custom silicon, volume purchasing and long-term capacity contracts help the three leaders. Yet AI increases dependence on scarce accelerators, power and data-center construction, so supplier pressure is becoming more economically important.

### Force 3 — Bargaining power of buyers

| Force | Sub-point | Evidence found | Top statistics / proxies (max 3) | Interpretation | Impact | Confidence |
|---|---|---|---|---|---|---|
| Buyers | Few buyers or large-volume buyers | Accounts are numerous, but the largest enterprise/government customers spend enough to negotiate committed-use pricing. Provider top-customer concentration is **not found in public filings**. [CMA25] | UK cloud spend £9bn in 2023; market $419bn; 68% top-3 share | Large accounts can run competitive tenders, while smaller self-service buyers are fragmented. | **Medium** | **Medium** |
| Buyers | Products are standardized or undifferentiated | Basic VMs, object storage and networking are comparable; managed data, identity, AI, security and ecosystems differ materially. [NIST] [GOOG25] | 3 largest providers; Google AI/data services; Azure cloud +34% | Commoditized layers give buyers leverage; differentiated higher services reduce it. | **Medium** | **High** |
| Buyers | Buyers face few switching costs | Evidence points the other way for existing workloads: egress, code/API differences, operational practices and compliance make switching hard. [CMA26] [EUDA] | Egress/interoperability barriers; EU ban from Jan-2027; 68% top-3 share | Low buyer mobility restrains buyer power today; upcoming portability rules should improve it gradually. | **Low** | **High** |
| Buyers | Buyers can integrate backward | Very large firms can retain/build private cloud, colocate, or run hybrid infrastructure; most cannot match the hyperscalers’ global platform. [GAO26] [CMA25] | 17/24 agencies report cloud-cost challenges; 111 AWS AZs; capex barrier significant | In-house infrastructure is a credible negotiating alternative for only a minority of very large or specialized buyers. | **Medium** | **High** |
| Buyers | Product is a large part of buyer cost | Cloud can be a material operating cost for digital natives, AI users and data-heavy firms; it is smaller for many diversified enterprises. Exact buyer cost shares are **not found in public filings**. [GAO26] | 17/24 agencies cite cost control; $7bn projected U.S. federal IaaS spend 2023–28; 68% top-3 share | Material spend encourages optimization and tenders, especially when AI use grows. | **Medium** | **Medium** |
| Buyers | Buyer group has low profits or cash pressure | Startups and many software/AI users are cost sensitive, whereas large governments and enterprises vary widely. Industry-wide buyer profitability is **not found**. [GAO26] | 17/24 agencies face cost control issues; $15.3m avoided cost in one Army FinOps example; 40% savings reported by NRC pilot | Budget pressure increases scrutiny but is not uniform across buyers. | **Medium** | **Medium** |
| Buyers | Buyer quality is not strongly affected by the product | The evidence points opposite: uptime, security, latency, scalability and compliance directly affect customers’ products and operations. [NIST] [GAO24] | 5 NIST cloud characteristics; federal authorization +60%; AWS multi-AZ design | Cloud quality is mission-critical, reducing willingness to select solely on lowest price. | **Low** | **High** |
| Buyers | Product has little effect on buyer’s other costs | Evidence points opposite for suitable workloads: cloud can reduce build/operate/maintain effort and allows idle VMs to be switched off. [GAO26] | 17/24 agencies cost challenges; Army avoided $15.3m; NRC reported ~40% annual savings | Customer ROI protects pricing when cloud replaces staff, delay and excess capacity—not merely a server rental. | **Low** | **High** |
| Buyers | Intermediate customers influence end customers | Integrators, resellers and managed service providers influence platform choice and migration. Exact channel share is **not disclosed**. [CMA25] [GAO26] | 11/24 agencies report multi-cloud interoperability considerations; £9bn UK spend; 68% top-3 share | Channels aggregate expertise and may gain bargaining leverage, but they usually do not own the end workload. | **Medium** | **Medium** |

**Force judgment:** **Medium pressure, High confidence, Worsening.** Customers are locked in enough to protect the installed base, and cloud quality/ROI matters. But big buyers can negotiate, cloud bills demand attention, and EU/UK portability measures aim to lower switching friction.

### Force 4 — Threat of substitutes

| Force | Sub-point | Evidence found | Top statistics / proxies (max 3) | Interpretation | Impact | Confidence |
|---|---|---|---|---|---|---|
| Substitutes | Substitute has attractive price-performance | Main substitutes are customer-owned data centers/private cloud, colocation/bare metal, outsourcing, SaaS, and doing nothing. GAO says cloud can be faster and possibly cheaper than building/operating infrastructure, but cost control is hard. [GAO26] | 17/24 agencies report cost challenges; $7bn federal IaaS 2023–28; 111 AWS AZs/35 regions | Cloud wins for volatility, speed, global reach and managed services; traditional infrastructure can win for stable high-utilization workloads. | **Medium** | **High** |
| Substitutes | Buyer switching cost to substitute is low | Repatriating a live cloud workload requires data movement, redesign, retraining and retesting; the CMA confirmed technical/egress barriers. Greenfield buyers can choose a substitute more easily. [CMA26] [EUDA] | Egress/interoperability barriers; switching-charge ban Jan-2027; 68% top-3 share | Substitution is difficult for the installed base but still constrains new workload placement. | **Low** | **High** |
| Substitutes | Changes in other industries make substitutes stronger | Open-source software, containers, bare-metal/GPU specialists and SaaS/model APIs can reduce the need for generic IaaS. Conversely, AI’s demand for scarce compute makes hyperscaler access more compelling. [NIST] [GAO26] | $419bn 2025 market; Google TPUs; 2026 Alphabet capex $175–185bn | Technology creates two-way pressure: it commoditizes some layers while raising the value of hyperscale AI infrastructure. | **Medium** | **Medium** |

**Force judgment:** **Medium pressure, High confidence, Stable.** On-premise/private cloud remains a real economic substitute, especially for steady workloads, but it does not replicate the elasticity, service breadth and global resilience of a hyperscaler. This is the key reason cloud is favored—while still not being universal.

### Force 5 — Rivalry among existing competitors

| Force | Sub-point | Evidence found | Top statistics / proxies (max 3) | Interpretation | Impact | Confidence |
|---|---|---|---|---|---|---|
| Rivalry | Many competitors or similar size competitors | Three leaders have 68% of Q4 2025 share, yet Oracle, IBM, Alibaba, sovereign providers and GPU clouds compete in segments. AWS is largest; Azure and Google grow faster in some periods. [SYNERGY] | AWS 28%; Azure 21%; Google 14% | Concentration reduces classic fragmentation, but three exceptionally well-funded rivals are sufficient for real competition. | **Medium** | **High** |
| Rivalry | Slow industry growth | Evidence points opposite: 2025 market revenue reached $419bn and Q4 revenue was $119.1bn. [SYNERGY] | $419bn FY2025; $119.1bn Q4; AWS +20% FY2025 | Growth lets firms add revenue without taking every dollar from each other, reducing price-war pressure. | **Low** | **High** |
| Rivalry | High exit barriers | Data centers, power commitments, custom hardware and enterprise support are sunk/long-lived. However, leaders can repurpose capacity to their own products or AI demand. [MSFT25] [GOOG25] | Microsoft depreciation $22.0bn; AWS 111 AZs; Alphabet plans $175–185bn 2026 capex | Exit is difficult, but capacity has internal uses; current constraints matter more than oversupply. | **Medium** | **High** |
| Rivalry | Rivals are highly committed to the business | AWS, Microsoft and Alphabet are scaling AI infrastructure and treat cloud as strategic. [AMZN25] [MSFT25] [GOOG25] | AWS $128.7bn sales; Azure >$75bn; Google Cloud $58.7bn | Each has the resources and strategic incentive to maintain investment even if short-term returns compress. | **High** | **High** |
| Rivalry | Firms cannot read each other’s signals well | Pricing combines pay-as-you-go, reservations, enterprise agreements, support, software bundles and AI-specific capacity; terms are mostly negotiated. [CMA25] [GAO26] | 3 leaders; 17/24 agency cost challenges; $419bn market | Opaque bundles and cross-subsidy make a rival’s effective price and response hard to observe. | **Medium** | **High** |
| Rivalry | Rivalry focuses on price | Providers offer credits, reserved use and committed-spend discounts. The CMA found committed-spend discounts widespread, though not at that time proven to harm competition. [CMA25] | £9bn UK market; 68% top-3 share; $419bn market | Price matters at the infrastructure layer and large deals, but quality, services, security and sales channels prevent a pure price war. | **Medium** | **High** |
| Rivalry | Products are nearly identical and switching costs are low | Basic compute is similar, but cloud APIs, managed services, identity, data platforms, compliance and enterprise software differ; switching is not low for installed workloads. [CMA26] [GOOG25] | Egress/interoperability barriers; Google TPU/Vertex; Azure +34% | Functional convergence raises competition, but platform differentiation and lock-in restrain commoditization. | **Medium** | **High** |
| Rivalry | Fixed costs are high and marginal costs are low | Data centers, networks, depreciation and R&D are large fixed commitments; serving an additional workload can have lower incremental cost until capacity tightens. [MSFT25] [GOOG25] | Microsoft depreciation $22.0bn; Alphabet 2026 capex $175–185bn; AWS 35 regions | High fixed cost creates an incentive to fill capacity with discounts, especially if AI supply moves from shortage to excess. | **High** | **High** |
| Rivalry | Capacity must be expanded in large chunks | Regions, power interconnects and AI clusters are built in large increments and years ahead of demand. [AWSREG] [CMA25] | AWS 111 AZs; significant capex barrier; Alphabet 2026 capex $175–185bn | Chunky capacity can cause localized oversupply, but today scarcity and broad demand soften it. | **Medium** | **High** |
| Rivalry | Product is perishable | An unused compute hour cannot be stored; servers also depreciate quickly. Capacity can nonetheless be allocated to other customers/workloads. [MSFT25] | Microsoft depreciation $22.0bn; $419bn market; AWS 111 AZs | Perishability raises utilization pressure but is less severe than hotel seats because capacity is flexible across workloads. | **Medium** | **Medium** |
| Rivalry | Non-price competition | Providers compete through AI models/chips, managed services, security, compliance, resiliency, developer tools, data platforms and partner ecosystems. [GOOG25] [MSFT25] [NIST] | Google 7th-gen TPU; Azure +34%; AWS 111 AZs | Non-price differentiation preserves value, but the required R&D and capex increase reinvestment needs. | **Medium** | **High** |
| Rivalry | Zero-sum vs positive-sum rivalry | The market is expanding with cloud migration and AI; at the same time, each provider tries to become the customer’s central data/AI/control platform. [SYNERGY] [AMZN25] [GOOG25] | $419bn market; AWS +20%; Google Cloud +36% | Demand remains positive-sum, but strategic workload capture and software bundling are increasingly zero-sum. | **Medium** | **High** |

**Force judgment:** **Medium pressure, High confidence, Worsening.** Rapid market growth and differentiated platforms keep rivalry below High today. AI-driven capex, overlapping product stacks, capacity commitments and a fight for central enterprise workloads make rivalry the controlling risk.

## 5. Overall force ratings

| Force | Overall pressure | Confidence | Main drivers | Trend |
|---|---|---|---|---|
| New entrants | **Low** | **High** | Global scale, capex/power, service catalogue, certifications, ecosystem and installed-base switching costs | **Stable** |
| Suppliers | **Medium** | **Medium** | Concentrated accelerators, power and data-center inputs; mitigated by hyperscaler scale and custom chips | **Worsening** |
| Buyers | **Medium** | **High** | Large-account procurement and cost scrutiny versus high migration friction, mission-critical quality and customer ROI | **Worsening** |
| Substitutes | **Medium** | **High** | On-premise/private/cloud alternatives remain sensible for steady workloads; public cloud wins on elasticity, speed and services | **Stable** |
| Rivalry | **Medium** | **High** | Three well-funded leaders, high fixed-cost/capacity commitments and AI convergence, offset by fast industry growth and differentiation | **Worsening** |

These are weighted judgments, not averages. For example, supplier inputs are highly concentrated, but the three hyperscalers are enormous customers with in-house chip alternatives. Rivalry is the most important force because it determines whether massive investment becomes customer value *and* durable provider profit.

## 6. Most important forces

**Which force matters most? — Rivalry.** AWS, Azure and Google Cloud all have the capital to match product launches and capacity investment. Azure can bundle cloud with a dominant enterprise software footprint; AWS has independent scale and a broad catalog; Google uses data/AI/TPUs to differentiate. This prevents the industry from becoming a comfortable monopoly despite high entry barriers.

**Which force is changing fastest? — Suppliers.** AI raises the importance of accelerators, power, land and data-center construction. That is moving the industry from a relatively asset-light *customer purchase* to a heavily capital-intensive *provider buildout*.

**Which force is most misunderstood? — Substitutes.** “Cloud is cheaper” is too simple. Cloud is often more valuable because it avoids overbuilding and speeds execution. For a steady workload already running on paid-for equipment, it can cost more. The comparison must include utilization, operational labor, resilience, refresh, migration and transfer costs—not just a VM hourly price.

**Are current profits protected?** AWS’s five-year 31.6% average segment operating-margin proxy and Google Cloud’s rapid improvement suggest profits can be durable after scale is reached. They are protected by barriers and switching costs, but not guaranteed: incremental AI profits will face high capex/depreciation, supplier scarcity and competition from two equally capable peers.

## 7. Stock-relevant takeaways

| Topic | Assessment |
|---|---|
| Pricing power | Good for differentiated managed services and installed workloads; weaker for commodity compute, giant contracts and bundles. |
| Margin durability | AWS shows mature potential. AI may delay margin expansion because it raises depreciation, power and accelerator cost; Google’s margin trend is encouraging but not proof of a cycle-free outcome. |
| Capital intensity | High and rising at the provider level. Cloud shifts capital intensity away from customers and concentrates it in hyperscalers. |
| Growth quality | High when growth is recurring, diversified and consumed after capacity is built. Lower quality if it depends on a few AI customers, subsidized credits or capacity built far ahead of demand. |
| Main risks | AI capacity overspend; chip/power bottlenecks; price/bundle competition; regulatory portability/egress changes; cybersecurity/outages; customer cost optimization; data sovereignty; workload repatriation for stable applications. |
| Evidence that would change the conclusion | **More favorable:** AI utilization and cloud margins rise after new capacity comes online; customers broaden managed-service use; power/chip cost per unit falls. **Less favorable:** widespread capacity excess/price cuts, structurally lower utilization, rising data-center depreciation without revenue, easier cross-cloud portability, or major workloads moving back on premise. |

### Relative provider position

| Provider | Strongest structural advantages | Main structural exposure |
|---|---|---|
| AWS | Largest independent scale, broad mature service catalogue, large operating-profit base, deep cloud-native ecosystem | Less pre-existing office/desktop software bundle than Microsoft; must keep investing heavily to retain AI leadership. |
| Azure | Enterprise agreements, identity/security, Windows/SQL/GitHub/Office/Dynamics distribution and hybrid positioning | Regulatory scrutiny of software licensing/bundling; Azure-only financial profitability is not disclosed. |
| Google Cloud | Data/analytics, AI research, Google internal scale and proprietary TPU stack; cloud margin moving sharply higher | Smaller installed enterprise footprint than AWS/Azure; reported segment includes Workspace, complicating pure-infrastructure comparisons. |

This is an industry-structure analysis, not a buy/sell recommendation, valuation, or price target.

## 8. Mistakes-to-avoid check

| # | Common mistake | Check |
|---:|---|---|
| 1 | Define competition only as direct competitors | **Avoided.** Included on-prem/private cloud, colocation, bare metal, SaaS/model APIs, AI/GPU specialists and in-house builds. |
| 2 | Define the industry too broadly or narrowly | **Avoided.** Defined IaaS/PaaS/hosted-private infrastructure and managed platform services, not all software or data centers. |
| 3 | Make lists without explaining causes using numbers | **Avoided.** All 38 required sub-points include evidence, up to three proxies, interpretation, impact and confidence. |
| 4 | Give equal weight to every force | **Avoided.** Rivalry and suppliers are identified as controlling; ratings are weighted judgments. |
| 5 | Confuse effect with cause | **Avoided.** Buyer/supplier conclusions tie to switching, concentration, differentiation, cost and alternatives. |
| 6 | Assume fast growth means an attractive industry | **Avoided.** Growth moderates rivalry but does not remove capex, supplier or bundle pressure. |
| 7 | Assume advanced technology means an attractive industry | **Avoided.** AI is both a differentiation opportunity and a source of capital/supplier risk. |
| 8 | Treat government as a sixth force | **Avoided.** Government is analyzed through entry certification, buyer procurement and portability regulation. |
| 9 | Treat complements as a sixth force | **Avoided.** Partners, chips, models and integrators appear through suppliers, buyer channels and entry barriers. |
| 10 | Rely on one-year results | **Avoided.** Uses FY2021–25 profitability direction and current market/regulatory evidence. |
| 11 | Assume consolidation automatically fixes rivalry | **Avoided.** High concentration is weighed against three committed rivals and specialist entrants. |
| 12 | Use the framework only to label the industry good/bad | **Avoided.** Connects structure to customer economics, margins, reinvestment, growth quality and disconfirming evidence. |

## Final synthesis

| Force | Overall pressure | Trend | Why it matters for the stock |
|---|---|---|---|
| New entrants | **Low** | **Stable** | The global fleet, service catalogue, compliance and ecosystem protect mature providers’ profit pools. |
| Suppliers | **Medium** | **Worsening** | AI chips, power and sites can claim more of the value created by cloud demand and keep capex high. |
| Buyers | **Medium** | **Worsening** | Switching costs protect existing workloads, but enterprise tenders, FinOps and portability rules limit pricing headroom. |
| Substitutes | **Medium** | **Stable** | Traditional infrastructure is still valid for stable workloads; cloud is favored where elasticity, speed and service breadth matter. |
| Rivalry | **Medium** | **Worsening** | Three giants can fund an AI/product/capacity arms race, so revenue growth must translate into utilization and returns. |

## Source notes

Primary filings and government sources were used where possible. Company sources support only their own financial and infrastructure disclosures; the CMA, GAO and NIST are used for the broader structural and customer-economics evidence.

- [AMZN25] [Amazon 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm) — AWS sales, operating income and company reporting limitations.
- [GOOG25] [Alphabet 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm) — Google Cloud revenue, operating income, TPU and infrastructure disclosures.
- [MSFT25] [Microsoft 2025 Annual Report](https://www.microsoft.com/investor/reports/ar25/index.html) and [Microsoft 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm) — Azure revenue milestone, Azure growth, Intelligent Cloud and depreciation disclosures.
- [SYNERGY] [Synergy Research: Q4 2025 cloud infrastructure services](https://www.srgresearch.com/articles/genai-helps-drive-quarterly-cloud-revenues-to-119-billion-as-growth-rate-jumped-yet-again-in-q4) — market size and share estimates.
- [CMA25] [UK CMA cloud services market investigation](https://www.gov.uk/cma-cases/cloud-services-market-investigation) — market structure, switching, entry barriers and pricing evidence.
- [CMA26] [UK CMA actions on business software and cloud services](https://www.gov.uk/government/news/cma-announces-package-of-actions-on-business-software-and-cloud-services) — final findings on market power, egress, interoperability and multi-cloud.
- [NIST] [NIST SP 800-145: The NIST Definition of Cloud Computing](https://csrc.nist.gov/pubs/sp/800/145/final) — cloud characteristics and service models.
- [GAO26] [GAO-26-107530: Federal Government Needs to Address Procurement Challenges](https://files.gao.gov/reports/GAO-26-107530/index.html) — customer economics, cost controls, FinOps and procurement experience.
- [GAO24] [GAO-24-106591: FedRAMP usage](https://www.gao.gov/products/gao-24-106591) — federal authorization/compliance evidence.
- [EUDA] [European Commission: Data Act explained](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained) — cloud switching and egress-charge rules.
- [AWSREG] [AWS Regions and Availability Zones](https://press.aboutamazon.com/sg/aws/2025/1/aws-launches-infrastructure-region-in-thailand) — AWS infrastructure footprint at the cited date.
