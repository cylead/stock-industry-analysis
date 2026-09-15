# Project Log

This log records material changes to the analysis skill from 2026-08-27 onward. Entries are ordered newest first; earlier repository history has not been reconstructed.

## Update criteria

Add an entry when `SKILL.md` materially changes the analysis scope, methodology, evidence standards, research workflow, rating framework, or required output structure. Do not add entries for routine report additions or refreshes, typo corrections, formatting changes, or link-only edits.

## Entry template

```markdown
## YYYY-MM-DD — Short title

- **Change:** What changed in the analysis skill.
- **Significance:** Why the change is material.
- **Affected behavior:** Which analysis behavior or output changed.
- **Compatibility/action:** Migration, compatibility, or follow-up required; use `None` when no action is needed.
```

## 2026-09-15 — Standalone ecosystem overlay removed

- **Change:** Removed the eight-row ecosystem-control assessment, verdict, and trend from `SKILL.md`, reducing required output from 56 to 48 canonical analytical rows: chain 6, brand 4, and Five Forces 38 (8/6/9/3/12). Former ecosystem evidence is now routed by causal mechanism into the chain map, brand assessment, relevant Five Forces rows, profitability implications, and structural synthesis.
- **Significance:** Eliminates a parallel aggregate assessment that overlapped with Five Forces mechanisms while retaining evidence about network effects, governance, access, distribution, data, switching, complementor dependence, integration, and value capture.
- **Affected behavior:** Future analyses follow industry chain → brand power → Five Forces, treat chain-map economic control as descriptive evidence rather than an ecosystem score, attribute repeat purchasing specifically to brand before calling it brand power, and avoid double-counting routed mechanisms.
- **Compatibility/action:** Existing reports remain unchanged until rerun. New and refreshed reports use 48 canonical rows and no standalone ecosystem table, verdict, or control trend, so consumers expecting the former 56-row schema must adapt.

## 2026-09-14 — Subject-adaptive report structure and internal quality checks

- **Change:** Reorganized the Five Forces definitions into the required sub-point section, moved intermediary influence from buyer price sensitivity to negotiating leverage, and made company, private-company, and pure-industry terminology and representative-participant treatment explicit. Removed the reader-facing mistakes self-certification, made short-term catalyst mapping conditional on a user request, consolidated investment implications, clarified the five-year missing-data fallback, and expanded the usual lifecycle target to 400–650 words.
- **Significance:** Corrects a taxonomy error and removes structural instructions that encouraged duplicated implications, meta-reporting, forced stock language, and synthetic industry-level profitability or lifecycle conclusions.
- **Affected behavior:** Future analyses retain all 56 canonical analytical rows and the chain → brand → ecosystem → Five Forces sequence. Applicable report sections are numbered consecutively; internal quality checks are not reproduced in the artifact; pure-industry reports identify representative participants and keep their profitability and lifecycle assessments distinct; short-term catalyst tables appear only when requested for a directly traded company or identified proxy.
- **Compatibility/action:** Existing reports remain unchanged until rerun. Consumers should no longer require a mistakes-to-avoid section or a not-applicable catalyst section, and section numbering may differ depending on whether catalyst analysis was requested.

## 2026-09-06 — Enterprise lifecycle, investment risks, and valuation fit

- **Change:** Added a required final Section 11, targeting 250–400 words, connecting enterprise lifecycle to material investment risks, capital allocation, suitable valuation metrics or methods, and observable transition indicators. Added stage- and business-specific valuation guidance and updated the purpose, synthesis rules, metric-use exception, and completion check.
- **Significance:** Extends structural business analysis to lifecycle-dependent risks and valuation-tool selection while distinguishing method suitability from calculating current multiples or estimating fair value. Requires evidence for stage judgments and distinguishes cyclicality, segment differences, and uncertain renewal.
- **Affected behavior:** Future analyses and reruns use eleven sections, retain catalysts in Section 10, and conclude with a brief lifecycle assessment and four-component table. The existing analytical rows and Section 4 profitability baseline remain intact; directly relevant growth, cash-flow, and reinvestment evidence is permitted in Section 11. Private-company disclosure gaps and differences among representative industry participants remain explicit.
- **Compatibility/action:** Existing reports remain unchanged until rerun. Consumers of newly generated reports must accept the appended Section 11 and no longer assume catalysts are last. Current multiples, fair values, price targets, and recommendations still require a separate user request.

## 2026-09-06 — GPT-6 research workflow and evidence handling

- **Change:** Consolidated repeated instructions, permitted independent source retrievals in parallel, and added evidence working notes, cutoff verification, non-US/private-company/industry source routing, and a research stopping condition. Distinguished absent disclosure, inaccessible sources, inapplicability, and unsupported assessments; clarified confidence, pressure/trend direction, proxy provenance, and comparable five-year calculations.
- **Significance:** Makes literal instruction following more reliable without requiring unsupported numbers or ratings to satisfy complete coverage. Documents the existing GPT-6/high runtime baseline and keeps execution within the active mode and permissions.
- **Affected behavior:** Future analyses retain all ten sections and 56 analytical rows, use direct supporting links and explicit gaps, and finish with a focused coverage/evidence/calculation review. Rows without a defensible assessment are labeled “Not assessable”; economically unsuitable capital-return metrics can use a clearly labeled disclosed alternative, and five-year averages require five comparable observations.
- **Compatibility/action:** Existing reports remain unchanged until rerun. Consumers must tolerate explicit missing-assessment labels and unavailable metrics instead of assuming every rating or annual value is populated. No runtime configuration change or report regeneration is required.

## 2026-09-06 — Industry-chain, brand-power, and ecosystem analysis sequence

- **Change:** Made the assessment sequence explicit as industry chain → brand power → ecosystem control → Five Forces while preserving source-first evidence collection. Added a four-test brand-power table between the chain map and ecosystem assessment in Section 3, with corresponding completion and synthesis requirements.
- **Significance:** Enables evidence reuse while requiring support for each distinct mechanism and preventing brand strength, channel ownership, and ecosystem control from being conflated or double-counted.
- **Affected behavior:** Future analyses and reruns assess customer preference, realized price premiums, retention, and channel bargaining power against relevant peers before assessing ecosystem control and applying the findings to Five Forces. The ten-section structure and existing chain, ecosystem, and Five Forces rows remain intact.
- **Compatibility/action:** Existing reports remain unchanged until rerun; no report regeneration is required for this update.

## 2026-09-05 — Short-term volatility catalyst mapping

- **Change:** Added a required final section that maps evidence-based Increase and Decrease news scenarios for listed stocks over a 1–5-trading-day horizon.
- **Significance:** Extends the methodology from structural business analysis to conditional identification of potential short-term volatility sources while avoiding price targets and deterministic forecasts.
- **Affected behavior:** Future listed-company analyses and reruns must rank 3–5 scenarios in each direction by qualitative sensitivity, explain the repricing mechanism, identify confirming indicators, cite supporting evidence, and distinguish sensitivity from confidence.
- **Compatibility/action:** Existing reports remain unchanged until rerun; private-company and pure-industry reports mark the section not applicable when no directly traded stock exists.

## 2026-08-27 — Project and issue logging introduced

- **Change:** Added project and issue logs with repository rules defining when and how they are maintained.
- **Significance:** Establishes a durable record of future material skill changes and noteworthy issue-resolution decisions.
- **Affected behavior:** Repository maintenance only; the analysis methodology and report output are unchanged.
- **Compatibility/action:** None.
