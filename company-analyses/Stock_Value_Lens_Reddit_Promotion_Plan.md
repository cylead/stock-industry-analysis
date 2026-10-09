# Stock Value Lens Reddit promotion plan

**Research and revision date: 2026-10-09.** Website: [Stock Value Lens](https://stockvaluelens.com/). **Owner-confirmed objective: repeat use by individual stock investors.** This is a product-demand validation and outreach plan, not investment advice. Product-market fit is unproven: no cohort retention, existing-user interviews or usage analytics were available for this assessment.

**Recommendation:** validate a narrow historical-research task before expanding promotion. Prioritize r/ValueInvesting when its one-time free-service route is confirmed. General developer testing is optional usability work. Recruit people because of their research behavior, not because they are active Reddit users.

Use the [posts and messages](#posts-and-messages), [people and contact routes](#people-and-contact-routes), [validation study](#validation-study), and [frequency and calendar](#frequency-and-calendar). All drafts remain unsent. This revision replaces the earlier launch-first calendar and generic-tester recruitment priority.

## Audience and recurring job

The primary hypothesis is **individual investors who regularly research US-listed operating businesses and want to inspect a company's long-term earnings and cash generation alongside price before deciding what to investigate in its filings**. They can already explain what EPS and cash flow mean; they need historical context, not a lesson in buying stocks.

The recurring job is:

> When I start researching another company or revisit one after new information, help me inspect price, annual EPS and cash-flow history quickly, identify what needs deeper investigation, and carry useful observations into my research notes.

The proposed positioning is:

> Historical price, earnings and cash-flow context before deeper stock research, with filing links and chart exports that do not require signup.

“Free” and “no signup” remove friction. They do not establish that this job is important, that current alternatives fail, or that the user will return.

| Segment | Possible job | Fit with the current product | Treatment |
|---|---|---|---|
| Fundamental investors doing recurring company research | Inspect long-term earnings/cash trends in context with price | Best hypothesis; annual history and filing links support it, subject to coverage and basis limits | Primary study cohort |
| Investors who currently assemble those observations in spreadsheets | Reuse selected chart observations in notes or a model | Plausible secondary use; chart CSV is not a complete statement/provenance export | Record export use separately; do not promise a model-ready financial database |
| FAST Graphs or other valuation-chart users | A fast second view of historical context | Relevant benchmark, but often already satisfied and reliant on estimates/TTM data absent here | Test a complementary role before claiming replacement |
| Beginners wanting “is this cheap?” or a buy/sell answer | Obtain a valuation verdict or forecast | Weak fit; a historical chart does not answer that question by itself | Do not target with a valuation-verdict pitch |
| Traders, quantitative backtesters and live-quote users | Point-in-time signals, intraday data or backtesting | Poor fit with weekly prices and retrospective annual EPS | Exclude from acquisition targeting |
| General builders and volunteer QA testers | Find interface bugs | Can validate usability, but not investor demand unless they also qualify as investors | Separate results from the primary cohort |

A qualified participant has researched an individual US-listed stock within the last 30 days, expects another research occasion within roughly the next month, and uses historical earnings or cash-flow information in that process. Ask about a public research task, not holdings, balances, income or risk tolerance. This is a study definition, not a claim about all investors.

## What the product can credibly promise

The current [local product documentation](/Users/yangch/Downloads/investment/stock-valuation-public/README.md) describes annual basic/diluted EPS, derived FCF/share, historical weekly prices, approximate P/E history, filing-linked financial observations and CSV/PNG exports without an account. It supports a focused historical workflow. It does not support analyst forecasts, a full financial terminal, automatic investment recommendations or a complete financial-statement export.

Keep four constraints visible:

- P/E uses annual EPS carried retrospectively from fiscal-period end. It is neither TTM/forward P/E nor a point-in-time backtest.
- Price adjustment, share basis and issuer-history exceptions can affect comparisons.
- History, available metrics and financial/price endpoints vary by company.
- The current chart CSV covers the chosen series/window; it is not the full annual financial table with all provenance.

For the first demonstration, choose a covered company with useful EPS and cash-flow history. Verify its actual dates, gaps and source links. Avoid REIT/FFO, bank-specific or loss-making-company use cases as the lead example unless their relevant metrics and limitations have been checked. Do not revive old May price-cutoff wording from the October 8 comparison report: the October 9 refresh advanced many prices, but individual endpoints still vary.

The key hypothesis is **a useful historical check with less effort than the user's present workflow**. Whether the site delivers that is to be tested, not asserted as a measured speed or accuracy advantage.

## Competitive and demand evidence

| Alternative or signal | Evidence checked | Implication for Stock Value Lens |
|---|---|---|
| GNG Research | Official charting page offers free valuation charts with an account, daily TTM-based P/E, other metrics, comparisons and estimates | Free valuation charts are already available. Immediate access may help, but annual retrospective P/E must not be sold as equivalent to its TTM series. [Official charting](https://www.gngresearch.com/charting/) |
| FAST Graphs | Official site emphasizes price/fundamental relationships, forecasts, screening and portfolios | There is a recognizable research job, but a much broader incumbent workflow. Test where our narrower view helps alongside it. [Official site](https://www.fastgraphs.com/) |
| Stock Analysis and TIKR | Stock Analysis offers broad financial tools; TIKR's pricing table lists five years/eight quarters in its free financial-history tier | Test the actual task against the participant's tool. Longer history and exports may matter to some users; neither service's entire workflow is replaced. [Stock Analysis](https://stockanalysis.com/pro/), [TIKR](https://www.tikr.com/pricing) |
| StockNest | Its creator advertises a free/no-account product with statements, comparisons and other tools. Its homepage returned no readable text for verification. | A competing “free/no signup” claim exists. Features, coverage and data quality remain creator claims, not an audited comparison. [Creator post](https://www.reddit.com/r/ValueInvesting/comments/1trya9n/i_built_a_free_stock_fundamental_analysis_app_no/) |
| Historical requests for price-versus-earnings graphs | Investor threads ask for that visualization and name existing substitutes | Evidence that some people have the job, not proof of current market size or unmet demand. These older threads are research context, not outreach lists. [2020 request](https://www.reddit.com/r/ValueInvesting/comments/g0e3sv), [2021 discussion](https://www.reddit.com/r/ValueInvesting/comments/ri9ic2) |

The StockNest discussion also contains both praise and a user who prefers their existing Stock Analysis workflow. Another commenter wants valuation context rather than more generic financial graphs. Those comments point to substitution, trust and usefulness as interview topics; they do not represent the whole market.

Existing promotion examples help choose a format, not establish our fit. TickerFS's disclosed creator link in a relevant tools discussion attracted favorable replies. TradeHints reported user growth from Reddit, but its numbers were self-reported. SideProject demos such as Life in Mist and Safearea.info received discussion that included criticism or audience confusion. None establishes repeat investor use of this website. [Tools thread](https://www.reddit.com/r/ValueInvesting/comments/1w0yyv9/share_your_favorite_stock_analyzing_tool/), [TradeHints](https://www.reddit.com/r/SideProject/comments/1wvtyo9/i_got_240_people_to_use_a_tool_i_built_reddit_was/), [Life in Mist](https://www.reddit.com/r/SideProject/comments/1wbu40o/i_built_an_iphone_app_that_turns_your_walks_into/), [Safearea.info](https://www.reddit.com/r/SideProject/comments/1wljtu9/i_got_tired_of_checking_safe_area_insets_in/).

## Subreddits by audience fit and permission

Membership is secondary to the number of relevant researchers and the permitted route. These rounded member figures retain the earlier cached `subscribers` observations; they are not live counts.

| Community | Cached members | Investor fit | Role in this plan |
|---|---:|---|---|
| [r/ValueInvesting](https://www.reddit.com/r/ValueInvesting/about/) | ~805,000 | Strongest fit for recurring fundamental research | Primary conditional channel: one genuinely free-service introduction |
| [r/SecurityAnalysis](https://www.reddit.com/r/SecurityAnalysis/about/) | ~214,000 | Strong research fit, higher standards | Read for workflow understanding; no promotion/recruitment without specific moderator permission and contribution access |
| [r/SideProject](https://www.reddit.com/r/SideProject/about.json) | ~853,000 | Mixed; builder status does not qualify someone | At most one conditional post seeking builders who also research stocks, or diagnosing a demonstrated UI problem |
| [r/alphaandbetausers](https://www.reddit.com/r/alphaandbetausers/about.json) | ~46,700 | Mixed, requiring investor screening | Hold: sidebar limits submissions to alpha/beta products; released website eligibility needs moderator clarification |
| [r/webdev](https://www.reddit.com/r/webdev/about/) | ~3.32 million | Low for investor-demand validation | No scheduled growth post; technical usability help only if needed and permitted on Saturday |
| [r/dividends](https://www.reddit.com/r/dividends/about/) | ~910,000 | Some historical-fundamental interest | Organic product promotion excluded under its rules, even when unmonetized |
| [r/investing](https://www.reddit.com/r/investing/about/) | ~3.46 million | Broad investor interest | Organic app/tool awareness promotion excluded |
| [r/stocks](https://www.reddit.com/r/stocks/about/) | ~9.37 million | Broad individual-stock interest | Promotion and app market-research routes excluded |
| [r/StockMarket](https://www.reddit.com/r/StockMarket/about/) | ~4.12 million | Broad stock interest | Website traffic/beta-recruitment promotion excluded |

ValueInvesting allows one introduction of a genuinely free service without registration or freemium restrictions. It also bars repeated domain promotion, promotion-focused/single-source accounts, off-topic technical trading, low-quality content and soliciting DMs/contact information. Resolve the older sidebar's software-distribution wording through modmail first. Keep the discussion public; do not add “DM me for access.” [Rules](https://www.reddit.com/r/ValueInvesting/about/).

**Correction to the earlier plan:** alphaandbetausers' empty custom-rules endpoint did not establish permission. Its sidebar requires a testable product, stage/platform labeling, excludes products believed not to be alpha/beta, and asks posters to test another product. Do not relabel this released site “beta” to qualify. The draft below is held unless moderators explicitly accept this use. [Full sidebar](https://www.reddit.com/r/alphaandbetausers/about.json).

SideProject welcomes project feedback and specifies project name plus description for project links. Webdev's technical Saturday allowance still excludes commercial promotion. Neither permission nor membership makes those communities proof of investor demand. Use a plain domain rather than shortened/referral links; recheck sidebar, pinned guidance, rules and account eligibility before publication.

## People and contact routes

### Investor research leads

These public comments identify useful research perspectives. **No general PM invitation or current availability was verified for any of these five people. They are a research watchlist, not a send list.** Their expressed preferences are public statements, not proof that they belong to our exact cohort. Do not mass-tag them, scrape their identities or message them simply because they commented.

| Public handle | Observed context | What to learn if they volunteer | Contact status |
|---|---|---|---|
| [u/ado136](https://www.reddit.com/user/ado136/) | Names FAST Graphs as central to their research in the [tools thread](https://www.reddit.com/r/ValueInvesting/comments/1w0yyv9/share_your_favorite_stock_analyzing_tool/) | Which specific historical task, if any, benefits from a second tool? | No PM permission; possible satisfied-user comparison |
| [u/Amazing_Main5874](https://www.reddit.com/user/Amazing_Main5874/) | Asks about free research tools and describes a broader comparison workflow in the same thread | Is a focused one-company historical view useful, or does it omit the task they need? | No PM permission; qualify before including |
| [u/SaltBat6229](https://www.reddit.com/user/SaltBat6229/) | Prefers Stock Analysis in the [StockNest discussion](https://www.reddit.com/r/ValueInvesting/comments/1trya9n/i_built_a_free_stock_fundamental_analysis_app_no/) | What earns trust and keeps an existing tool in their workflow? | No PM permission; useful counterevidence to free-first positioning |
| [u/mrmrmrj](https://www.reddit.com/user/mrmrmrj/) | Wants valuation history rather than generic accounting graphs in that discussion | Does our retrospective P/E/earnings view answer any of the job, or are estimates/bands essential? | No PM permission; requested features exceed current scope |
| [u/al3shan](https://www.reddit.com/user/al3shan/) | Wants quick growth-assumption testing and discusses historical P/E in [this thread](https://www.reddit.com/r/ValueInvesting/comments/1ubw142/how_do_i_quickly_check_if_a_stock_is_expensive_or/) | Is historical context helpful alongside a valuation model? | No PM permission; the main forecast/DCF job is not served here |

Prefer qualified people who voluntarily respond to the approved introduction, an explicitly permitted recruitment post, or an existing consensual conversation. A person asking for another creator to DM them is not giving us permission. Public research questions must also fit community rules; do not disguise a survey as ordinary discussion.

### Earlier generic testers

The earlier five candidates remain optional usability reserves. They are not established investor participants and are removed from the scheduled acquisition list.

| Candidate | Existing invitation | Role now |
|---|---|---|
| [u/Capable-Property-539](https://www.reddit.com/user/Capable-Property-539/) | [Testing offer accepts DMs](https://www.reddit.com/r/alphaandbetausers/comments/1vuco5a/happy_to_beta_test_your_product_ill_use_it_and/) | One targeted UI test only if a real usability blocker needs investigation; investor status unverified |
| [u/bananajoin](https://www.reddit.com/user/bananajoin/) | [Older web-testing offer accepts DMs](https://www.reddit.com/r/alphaandbetausers/comments/1v6blsr/free_beta_tester_here_ill_test_your_app_and_give/) | Reserve browser tester; recheck activity and invitation |
| [u/pickmycostume](https://www.reddit.com/user/pickmycostume/) | [Invites projects in comments](https://www.reddit.com/r/alphaandbetausers/comments/1wpbljm/drop_your_app_or_site_and_ill_test_it_i_had_ai/) | Public UI feedback only if still invited and appropriate |
| [u/yakaspectrum](https://www.reddit.com/user/yakaspectrum/) | [Invites projects in comments](https://www.reddit.com/r/alphaandbetausers/comments/1weh9d9/drop_your_project_ill_test_10_of_them_and_give/) | Reserve public UI feedback |
| [u/principalla](https://www.reddit.com/user/principalla/) | [Invites projects in comments](https://www.reddit.com/r/alphaandbetausers/comments/1v7bbsl/10_years_building_apps_show_me_what_youre_working/) | Reserve public UI feedback |

Public invitation pages show some testing replies, but profile feeds were inaccessible and current October 9 activity is unverified. Recheck before contact. General testing invitations are not invitations to repeated sales pitches. If a tester also qualifies as an investor, record that qualification explicitly before counting them in the primary cohort.

## Posts and messages

### ValueInvesting moderator draft

> Hi moderators — I built Stock Value Lens, a free historical US-listed stock research site: https://stockvaluelens.com/
>
> Charts and CSV/PNG exports require no registration or freemium tier. I would like to use the one-time free-service introduction to explain a specific use: inspecting historical price alongside annual EPS and cash flow before reading the filings more deeply.
>
> The post would disclose ownership, annual/retrospective P/E timing and coverage limits, and invite public feedback on usefulness in a research workflow. No DM or contact-information solicitation.
>
> Does that fit the allowance, including the sidebar's software-distribution wording, and which flair should I use?

### ValueInvesting introduction

**Title:** A free historical earnings and cash-flow check before deeper stock research

> When researching a company, I want to inspect how its annual earnings and cash flow have developed alongside its stock price before going deeper into the filings.
>
> I built Stock Value Lens for that step: https://stockvaluelens.com/
>
> It has historical weekly prices, annual EPS and derived free cash flow per share where available, filing links, approximate P/E history, and chart CSV/PNG exports. No account or subscription is required.
>
> Important limitation: P/E uses annual EPS retrospectively from fiscal-period end. It is not TTM, forward P/E or a point-in-time backtest. Coverage, dates and price/share-basis consistency vary by company; check those before interpreting a chart.
>
> If you already do fundamental stock research, try a company you're investigating. Does this view help you identify something to examine in the filings, or is your current tool already better for that step? I'd welcome concrete examples in the comments.

Use once, only after rule/eligibility clarification. Add a real labeled example if available. Rewrite the draft in your own voice. Do not imply intrinsic fair value or recommend a security. An approved introduction in an existing relevant tools thread would be an alternative to this post, not an additional distribution allowance.

### Conditional SideProject post

**Title:** Stock Value Lens — historical stock research for builders who also analyze companies

> I built Stock Value Lens: https://stockvaluelens.com/ — historical weekly prices, annual EPS/cash-flow views and chart exports without signup.
>
> I'm trying to understand one audience: people who already research individual US-listed companies and use financial history before going deeper into filings.
>
> If that's you, think of your last research task. Does this historical view help with a step you currently do elsewhere? What would you keep using your existing tool for?
>
> The P/E view is annual-EPS-based and retrospective, not TTM/forward P/E or a backtest. Company coverage and data dates vary. I'm the builder; a real workflow example or a reason you wouldn't use it is more useful than a general design compliment.

Hold unless more qualified participants are needed or a specific usability barrier emerges. Screen respondents before counting their behavior as investor-demand evidence. No automatic follow-up launch post is scheduled.

### Conditional Alphaandbetausers recruitment

**Title:** [Web, released tool — moderator-approved testing] Investors wanted for a historical stock research workflow test

> I built Stock Value Lens: https://stockvaluelens.com/ — historical US-listed stock charts and exports without signup.
>
> I'm looking for people who have researched an individual stock in the last month and expect to research another soon. This is a released site; I'm testing its usefulness in that existing workflow.
>
> Choose a company you're researching. Inspect annual EPS/cash flow against historical price, then tell me whether this helps identify a question for deeper research or duplicates what your current tool already does.
>
> P/E is annual-EPS-based and retrospective, not TTM/forward P/E. Coverage, dates and adjustment limits vary.
>
> Public feedback is welcome. No holdings, balances, purchase or favorable review needed.

**Do not use this draft until moderators accept a released-tool study and specify title labeling.** Replace the proposed label with their actual instruction; “moderator-approved” is not true until approval is obtained. If they decline or do not clarify, skip the channel. Honor the request to test someone else's product if using it, without promising a positive review or treating reciprocity as retention.

### PM for a qualified volunteer

Use only after an individual invites a PM or agrees to continue privately, in a context where that solicitation is allowed. ValueInvesting prohibits requesting DMs/contact information in its posts and comments; keep feedback there public unless the individual independently initiates private contact.

> Thanks for agreeing to discuss your research workflow. I'm the builder of Stock Value Lens: https://stockvaluelens.com/
>
> Before trying it, what was the last company-research question you used historical earnings or cash flow to answer, and which tool did you use?
>
> On your next suitable research task, could you try this view and tell me what it adds or misses? The P/E is annual-EPS-based and retrospective; company dates and coverage vary.
>
> No portfolio details or investing decision needed. If you're willing, I can check back once after two weeks to ask whether you chose to use it again. Saying no is fine.

For a watchlist person who later consents, personalize the opening accurately:

| Person | Opening after consent |
|---|---|
| ado136 | “You mentioned FAST Graphs is central to your research. I'd like to understand whether this adds a useful historical check alongside it.” |
| Amazing_Main5874 | “You mentioned looking for useful free research tools. I'd like to test whether a focused historical view serves any part of your actual workflow.” |
| SaltBat6229 | “You said you preferred your existing Stock Analysis workflow. I'd like to understand what a second tool would need to do to earn a place.” |
| mrmrmrj | “You asked for valuation context rather than more accounting graphs. I'd like to learn which parts of that job this historical view still misses.” |
| al3shan | “You discussed historical P/E alongside growth assumptions. This tool does not provide a DCF; I'd like to test whether its historical context is useful alongside your model.” |

Do not write “thanks for agreeing” when no consent exists. No direct investor PM is ready to send solely on the evidence found here.

### Optional usability PM

Only if a repeated interface blocker appears, and Capable-Property-539's testing invitation remains open:

> Hi — I saw your workflow-testing offer. I built Stock Value Lens: https://stockvaluelens.com/ — a free historical stock research site, no signup.
>
> Would you be willing to check whether the path from company search to the CSV export is clear? I'm testing that interface step, not asking for an investing opinion. A note on the first confusing action would help. Completely fine if your testing offer has closed.

Treat that result as usability evidence unless the person also meets the investor criteria.

## Validation study

Aim for **ten qualified investors**, with a clear record of how they joined. That is a practical learning sample, not a representative market survey or a statistical proof of fit. General QA testers, the owner and visits from curiosity do not fill the cohort.

1. **Understand the existing job before showing the site.** Ask about the most recent real research occasion, current tools, frequency and friction. Look for a concrete unmet step; do not lead with “would you use a free website?”
2. **Try a real task.** Let them select a company and research question. Observe whether they can inspect relevant history, understand dates/basis and identify a useful next question. Exporting is optional unless part of their actual workflow. A forced download only proves task completion.
3. **Compare with the current alternative.** Ask what this adds, what is missing, and what they would continue doing elsewhere. If they willingly repeat the task in both tools, record observed effort without claiming a general speed advantage.
4. **Observe another research occasion.** Over the following 7–21 days, look for use on another company or a new question. A prompted retest of a fix is not organic return. Extend the window to 30 days for users whose research cadence is slower, and record people who had no new occasion.
5. **Make a decision from behavior.** Find the segment/job with repeated utility. Fix repeated blockers and run another small cohort before increasing distribution.

| Measure | Operational definition | What it establishes |
|---|---|---|
| Qualification | Recent individual-stock research and relevant history use; another occasion expected | Audience fit, not demand by itself |
| First useful session | User identifies a real research observation or next filing question and understands the series limits | Initial usefulness |
| Second useful session | Return for a distinct self-chosen research task, without a reminder to use the site | Early repeat-use signal |
| Alternative displaced or complemented | User can name the step this replaces or adds to their existing process | A reason for the product to exist |
| Export used downstream | Chart observations actually used in research notes/model, rather than downloaded on instruction | Secondary utility |
| Trust blocker | Coverage, source, basis or freshness issue prevents actual use | A product constraint requiring investigation |

Use **counts and denominators**: “3 of 10 qualified participants returned for a different task,” plus how many had a new research occasion and how that return was established. Report missing follow-ups as unknown, not automatically retained or satisfied. Analyze general tester and investor results separately.

No event analytics or repeat-visitor identification was verified. Start with consented study records and clearly label self-reported returns. Where a user voluntarily shares a second task/result, record that separately from direct observation or existing analytics. Pageviews cannot establish that the same qualified investor returned. Do not add tracking code as part of this document revision.

Proposed decision rules, deliberately provisional:

- **Continue the narrow experiment** if, in a cohort of ten, at least five get a concrete first-session benefit and at least three return for a new research task, with a specific reason for choosing this view. This supports another test, not a claim of product-market fit.
- **Fix the workflow first** if relevant investors want the job but cannot trust the data/basis or complete the task. A UI fix alone does not resolve financial-data trust.
- **Narrow or change positioning** if participants need forecasts, live quotes, full statements or backtesting more than historical context.
- **Pause broad promotion** if most relevant users say their existing workflow is sufficient, or repeat use does not appear after genuine new research occasions.
- **If fewer than ten qualify**, report the actual count and qualitative findings. Do not backfill with general builders or apply these numerical thresholds as if the sample were complete.

Ask “what would you use if this disappeared?” after real use. An existing substitute is useful evidence. Avoid interpreting polite praise, promised future use, five-star review swaps or a small “very disappointed” survey as proof.

## Frequency and calendar

The frequency follows learning capacity and permission, not a target number of impressions.

| Action | Frequency |
|---|---|
| Reading relevant investor discussions | Two or three 20–30-minute sessions per week; focus on recurring research problems |
| ValueInvesting promotion | One introduction total after clarification; answer relevant questions in the same thread |
| Additional qualified recruitment | At most one conditional SideProject or approved Alphaandbetausers post in the first month if the cohort is short; do not automatically use both |
| Generic tester recruitment | Zero scheduled mass outreach; one targeted usability request only if a real blocker requires it |
| New investor PMs | No cold watchlist campaign. At most one new consented conversation per day and three per week, only while more qualified participants are needed |
| Follow-up | One agreed research check after about two weeks; no follow-up to an unanswered initial invitation |
| Broader expansion | Reconsider after the repeat-use review; never repeat the ValueInvesting introduction |

Those PM numbers are proposed workload caps, not Reddit's quota or protection against spam enforcement. [Reddit chat limits](https://support.reddithelp.com/hc/en-us/articles/360060638392-Why-can-t-I-start-a-chat-or-send-an-image), [spam policy](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam). Follow-ups should ask about what actually happened, not remind people to create a retention event. Stop on refusal, removal or closed invitations.

| Window beginning October 9 | Work | Completion evidence |
|---|---|---|
| Oct 9–15 | Verify a demonstration company; read rules/sidebar; send moderator draft yourself if proceeding; learn the existing task from willing qualified investors | Clear research job, accurate example and permitted route |
| Oct 16–22, conditional | One ValueInvesting introduction; qualify willing respondents and capture their baseline/first use | Actual qualified participants and usefulness, not total clicks |
| Oct 23–29 | Diagnose blockers and examine second research occasions; use one additional recruitment route only if needed and permitted | Repeat-task evidence, trust issues and reasons current tools win |
| Oct 30–Nov 7 | Review results available so far; stop unnecessary recruitment | Actual cohort counts and a continue/fix/reposition decision |
| Rolling thereafter | Complete each participant's 14–30-day window from their own first use | Late recruits get a full observation window; no premature month-end retention claim |

Keep at least 72 hours between permitted public product-distribution attempts. Do not repost to maintain reach; a substantive change still needs community permission. All remaining posts are contingent on what the study needs, and a narrow positive result does not authorize violating a no-promotion rule.

Record participant code, public source/consent, qualification, research task, alternative, first benefit, return occasion/date/evidence, blocker and next agreed action. Keep private messages and personal details out of public Git commits; summarize findings anonymously. Do not ask for testimonials or investment returns as the success measure.

## Cached activity and content evidence

Live 24-hour/seven-day post totals could not be verified because Reddit browser access encountered a verification challenge. The earlier chronological samples are preserved here to satisfy the activity comparison; they indicate posting density and discussion, not the size of our qualified market.

| Community | Cached UTC sample in 2026 | Posts | Span | Median comments |
|---|---|---:|---:|---:|
| [ValueInvesting](https://www.reddit.com/r/ValueInvesting/new.json?limit=20) | Aug 31 14:45–Sep 1 09:34 | 20 | 18.82 hours | 13.5 |
| [SideProject](https://www.reddit.com/r/SideProject/new.json?limit=20) | Oct 4 08:24–09:54 | 20 | 1.49 hours | 1 |
| [alphaandbetausers](https://www.reddit.com/r/alphaandbetausers/new.json?limit=20) | Oct 3 17:59–22:37 | 20 | 4.63 hours | 0 |
| [webdev](https://www.reddit.com/r/webdev/new.json?limit=20) | Sep 26 19:00–Sep 27 07:00 | 20 | 12.00 hours | 6 |

Exact membership provenance, 80 New-post records and 80 abbreviated Best-feed records remain in the [dated evidence file](Stock_Value_Lens_Reddit_Research_2026-10-09.json). Snapshots span different dates; comment counts include author replies. No daily/weekly extrapolation or conversion forecast is made.

The following Best audit remains a dated **format reference**. Best is a ranked logged-out feed, not the 20 most-upvoted posts; pinned highlights were excluded. Selected marketing details were inspected, not every comment in all 80 posts. A surviving promotional post does not override rules. Use patterns only when they fit the investor job and a permitted route.

## Best feed audit

Each table preserves the order of the first 20 non-highlight posts. Subject labels are abbreviated descriptions. **Text** means a text preview; **Demo** means visible image/video media; **Link** means an outbound reference visible in the feed. These categories do not certify ownership, promotion permission, absence of other links or commercial status.

### ValueInvesting

Source: [indexed Best feed](https://www.reddit.com/r/ValueInvesting/best/), crawler age reported as last week at retrieval.

| Position | Subject | Preview |
|---:|---|---|
| 1 | Yearly stock purchases | Text |
| 2 | Alphabet advertising risk | Text |
| 3 | Nike investment thoughts | Text |
| 4 | Nike price collapse | Text |
| 5 | Nike insider buying | Text |
| 6 | Recovery timing risk | Text |
| 7 | IPO cancellation news | Link |
| 8 | AI cash flow economics | Text |
| 9 | QQQ performance comparison | Text |
| 10 | Canadian FCF screen | Link |
| 11 | Buy and hold testing | Text |
| 12 | Buffett retirement news | Link |
| 13 | Housing contrarian case | Text |
| 14 | Waiting for corrections | Text |
| 15 | Duolingo thesis | Link |
| 16 | Indonesia market crash | Link |
| 17 | Idle cash management | Text |
| 18 | Company discovery methods | Text |
| 19 | Filtering investment noise | Text |
| 20 | Long horizon Nike | Text |

### SideProject

Source: [indexed Best feed](https://www.reddit.com/r/SideProject/best/), crawler age reported as two weeks ago at retrieval.

| Position | Subject | Preview |
|---:|---|---|
| 1 | Job search launch update | Demo |
| 2 | Walking fog map | Demo |
| 3 | Interactive reading app | Demo |
| 4 | Form filler experiment | Demo |
| 5 | Drawing QR codes | Demo |
| 6 | Project evolution demo | Demo |
| 7 | Bird hobby milestone | Link |
| 8 | Zero revenue joke | Demo |
| 9 | Click recording guides | Demo |
| 10 | Plexo download manager | Demo |
| 11 | App security discussion | Text |
| 12 | Using your own app | Text |
| 13 | Robot brain demo | Demo |
| 14 | Programmer roof demo | Demo |
| 15 | Device safe areas | Demo |
| 16 | Builder motivation | Text |
| 17 | Camera feature update | Demo |
| 18 | Airgeek product demo | Demo |
| 19 | Nail sorting game | Demo |
| 20 | Product Hunt launch | Demo |

### alphaandbetausers

Source: [indexed Best feed](https://www.reddit.com/r/alphaandbetausers/best/), crawler age reported as last week at retrieval.

| Position | Subject | Preview |
|---:|---|---|
| 1 | DesignWerks website offer | Link |
| 2 | Costume picker testing | Link |
| 3 | Objection handling trainer | Text |
| 4 | Written testing offer | Link |
| 5 | Fishing game testers | Link |
| 6 | Viravo beta | Link |
| 7 | Data deletion tool | Link |
| 8 | Aura messenger testing | Link |
| 9 | Raplika student feedback | Link |
| 10 | Ploy workflow discussion | Text |
| 11 | Founder testing offer | Text |
| 12 | Freelancer cash flow | Text |
| 13 | Feedback exchange | Link |
| 14 | QueuePilot beta | Link |
| 15 | Business Machine testers | Link |
| 16 | FIRE portfolio brief | Text |
| 17 | MTC audio player | Link |
| 18 | CardKoala testers | Link |
| 19 | Ogle beta | Link |
| 20 | Halo beta | Link |

### webdev

Source: [indexed Best feed](https://www.reddit.com/r/webdev/best/), crawler age reported as yesterday at retrieval.

| Position | Subject | Preview |
|---:|---|---|
| 1 | Static generator comparison | Text |
| 2 | Mobile design problem | Demo |
| 3 | Source date question | Text |
| 4 | AI deployment tradeoffs | Text |
| 5 | Numeric IP tip | Link |
| 6 | Animation handoff question | Text |
| 7 | Page Rage demo | Demo |
| 8 | REST architecture question | Text |
| 9 | AI skills discussion | Demo |
| 10 | Client coding problem | Text |
| 11 | Free hosting proposal | Text |
| 12 | Programming motivation | Text |
| 13 | Accessibility learning | Text |
| 14 | Developer skills article | Link |
| 15 | Ownership article | Link |
| 16 | Example domain change | Demo |
| 17 | PayPal accessibility | Text |
| 18 | Frontend industry essay | Link |
| 19 | Learning before AI | Text |
| 20 | Autocomplete question | Text |

### Patterns to use

- **ValueInvesting:** mostly substantive questions and stock reasoning. External links occur in the previews, including a data screen, but authorship/approval cannot be inferred. Present the investor use case and limitations before the site link.
- **SideProject:** 16 of 20 sampled previews show media. A concise visual demonstration with a concrete problem is the strongest format hypothesis.
- **Alphaandbetausers:** 15 of 20 sampled previews contain an outbound reference. Precise tasks, tester eligibility and platform labels are common.
- **Webdev:** questions and technical discussions dominate. A hobby demo is visible, but project-sharing restrictions still govern our post.

Marketing methods verified in selected details include disclosed creator links in post bodies, links in explicitly invited testing comments, and brand mentions without a visible preview link. No systematic benefit from placing links in comments rather than bodies was established.

Copy the useful structure—clear audience, real demonstration, honest limitations and specific feedback request. Do not copy exceptions to promotion rules or assume that slow moderation makes an attempt low-risk.
