# Issue Log

This log records noteworthy project issues from 2026-08-27 onward, including how they were investigated, resolved, and prevented from recurring. Entries are ordered newest first; earlier repository history has not been reconstructed.

## Update criteria

Add an entry when an issue requires meaningful investigation or judgment and affects correctness, methodology, reproducibility, output compatibility, or workflow. Do not record trivial errors with an immediate, obvious fix.

Use sequential IDs beginning with `ISSUE-001`. Create an entry as soon as a qualifying issue is recognized, update that same entry as the investigation progresses, and do not create duplicate entries for the same issue. Use only `Open` or `Resolved` for status. In an open issue, use `Pending` for fields that are not yet known; replace every `Pending` value when the issue is resolved.

## Entry template

```markdown
## ISSUE-NNN — Short title

- **Status:** Open | Resolved
- **Opened:** YYYY-MM-DD
- **Resolved:** YYYY-MM-DD | Pending
- **Affected area:** File, workflow, methodology, or output affected.
- **Problem and impact:** What failed or could fail, and why it matters.
- **Root cause or hypothesis:** Confirmed cause, or the current hypothesis while open.
- **Chosen solution:** Implemented solution, or `Pending` while open.
- **Rationale:** Why this solution was selected, or `Pending` while open.
- **Alternatives considered:** Rejected options and why, or `Pending` while open.
- **Follow-up/prevention:** Remaining work or controls that reduce recurrence, or `None`.
```

## Recorded issues

## ISSUE-003 — Ecosystem overlay duplicated Five Forces mechanisms

- **Status:** Resolved
- **Opened:** 2026-09-15
- **Resolved:** 2026-09-15
- **Affected area:** `SKILL.md` analytical sequence, canonical rows, Section 3, synthesis, implications, catalysts, lifecycle linkage, and completion checks.
- **Problem and impact:** The standalone ecosystem-control assessment repeated mechanisms already assessed through entry barriers, switching costs, distribution access, supplier power, substitutes, and rivalry. Its aggregate verdict and trend could double-count the same evidence and create inconsistent conclusions, while repeat purchasing could be misattributed to brand instead of contracts, habit, network effects, or other mechanisms.
- **Root cause or hypothesis:** Ecosystem control was added as a strategic overlay with its own eight tests and summary verdict even though its component mechanisms already had causal homes in the chain map, brand assessment, profitability analysis, and Five Forces.
- **Chosen solution:** Removed the standalone ecosystem table, score-like verdict, and control trend; reduced the canonical output to 48 rows; retained descriptive economic-control evidence in the chain map; and added explicit causal routing for participant reinforcement, governance/access/data/workflow, complementor dependence/multi-homing/external bottlenecks, and integration/value capture. Renamed the retention test and tightened brand attribution.
- **Rationale:** Routing each fact to the mechanism that affects entry, buyer or supplier leverage, substitution, rivalry, profitability, or value capture preserves useful evidence while producing one coherent force assessment and preventing duplicate scoring.
- **Alternatives considered:** Keeping the overlay but weakening its verdict would preserve duplication and ambiguity. Keeping the eight evidence rows without ratings would still expand the canonical schema and encourage repeated analysis. Removing ecosystem-related evidence entirely would discard economically relevant mechanisms.
- **Follow-up/prevention:** The completion check fixes the 48-row identities, requires chain → brand ordering, and checks causal consistency and double-counting; the internal mistakes check rejects network-effect claims based only on size or partner counts and duplicate use of brand, switching, distribution, data, or network mechanisms across force ratings.

## ISSUE-002 — Report schema mixed taxonomy, internal QA, and subject types

- **Status:** Resolved
- **Opened:** 2026-09-14
- **Resolved:** 2026-09-14
- **Affected area:** `SKILL.md` force taxonomy, required output order, company/industry adaptation, catalyst scope, and lifecycle guidance.
- **Problem and impact:** The buyer-power taxonomy placed intermediary influence under price sensitivity; canonical force definitions appeared after the output specification at the document's top heading level; and the required schema exposed an internal mistakes checklist while forcing company and stock labels onto private-company and pure-industry reports. The schema also encouraged repeated implications and under-specified how representative profitability and lifecycle evidence should be handled.
- **Root cause or hypothesis:** Successive methodology additions preserved earlier numbering and templates without a focused structural consolidation, so internal validation, reference material, and reader-facing output requirements became interleaved.
- **Chosen solution:** Placed canonical force definitions inside the Five Forces output section with correct heading hierarchy, moved intermediary influence to buyer negotiating leverage, made terminology and representative-participant rules subject-specific, converted the mistakes list to an internal completion control, consolidated implications, made catalysts request-driven, and clarified profitability and lifecycle treatment.
- **Rationale:** The revised structure keeps the full analytical coverage and evidence standards while reducing ambiguous execution, duplicated prose, irrelevant stock language, and unsupported aggregation for pure industries.
- **Alternatives considered:** Keeping the eleven-section schema and only renaming headings would not remove the reader-facing self-audit or resolve conditional sections. Splitting company and industry analysis into separate skills would reduce ambiguity but duplicate most methodology and increase maintenance cost.
- **Follow-up/prevention:** The completion check now verifies applicable-section order, subject-appropriate terminology, representative-participant treatment, canonical row identities, and conditional catalyst inclusion. Existing reports are migrated only when rerun.

## ISSUE-001 — Missing evidence and mandatory proxies were ambiguous

- **Status:** Resolved
- **Opened:** 2026-09-06
- **Resolved:** 2026-09-06
- **Affected area:** `SKILL.md` evidence conventions, participant proportions, ratings, and profitability baseline.
- **Problem and impact:** The skill used “Not found in public filings” for all evidence gaps while requiring a best proxy, a majority group, and five annual values. Literal execution could imply that inaccessible filings were inspected or encourage unsupported proportions, ratings, and averages.
- **Root cause or hypothesis:** Coverage requirements did not distinguish complete analysis of a row from availability of its requested data. Missing disclosure, source-access failure, and economic inapplicability shared an unsuitable fallback.
- **Chosen solution:** Kept every required row while adding distinct inspected-source, access-failure, and inapplicability labels; required evidence for proxies and proportions; allowed “Not assessable” for unsupported judgments; and required five comparable annual values for a five-year average. Added explicit handling of economically unsuitable capital-return metrics and public-data gaps.
- **Rationale:** Complete analytical coverage should expose evidence limitations, not imply certainty or force invented data. Explicit exceptions preserve the report structure while making provenance and calculations reviewable.
- **Alternatives considered:** Retaining one generic missing-data phrase would conceal whether sources were inspected. Mandatory proxies or default Medium ratings would imply unsupported precision. Omitting affected rows would break the required analytical coverage.
- **Follow-up/prevention:** Validation confirmed all canonical table content, 56 analytical rows, ten sections, and catalyst requirements were preserved; the skill validator and local link checks passed. Instruction walkthroughs covered a standard listed company, non-US issuer, insurer, private company, and industry, plus source-access failures, incomplete history, unsupported proportions, conflicting evidence, and unavailable upstream access. These were static checks, not live report benchmarks; future reports use the revised completion review.
