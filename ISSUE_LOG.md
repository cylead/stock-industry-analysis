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
