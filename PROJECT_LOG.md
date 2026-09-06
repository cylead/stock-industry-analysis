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
