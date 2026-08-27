# Repository Instructions

## Analysis workflow

- For every company, stock, or industry Five Forces request, read and follow the complete root [`SKILL.md`](SKILL.md) before researching or drafting the report.
- Treat `SKILL.md` as the sole canonical methodology. Do not create or use alternate, legacy, or non-optimized skill files.

## Analysis outputs

- Save every completed company, stock, or industry analysis as a Markdown file before sending the final response.
- Store all generated reports in `company-analyses/`; never place generated reports in the repository root.
- For a listed company, use `<TICKER>_Five_Forces_Analysis.md`, with the ticker in uppercase. For a private company or industry without a ticker, use a concise underscore-separated subject name followed by `_Five_Forces_Analysis.md`.
- Update the existing report when rerunning the same subject instead of creating a duplicate.
- Preserve source links, include the research date or data cutoff near the top, and state that the report is not investment advice.
- In the final response, link to the saved Markdown report.

## Maintenance logs

- Before completing any repository change, assess whether [`PROJECT_LOG.md`](PROJECT_LOG.md) or [`ISSUE_LOG.md`](ISSUE_LOG.md) must be updated. Include required log updates in the same commit as the related change.
- Update `PROJECT_LOG.md` only when `SKILL.md` materially changes the analysis scope, methodology, evidence standards, research workflow, rating framework, or required output structure.
- Do not update `PROJECT_LOG.md` for routine analysis additions or refreshes, typo corrections, formatting changes, or link-only edits.
- Add an `ISSUE_LOG.md` entry when an issue requires meaningful investigation or judgment and affects correctness, methodology, reproducibility, output compatibility, or workflow. Do not log trivial errors with an immediate, obvious fix.
- Use the templates and conventions defined in each log. Keep entries newest first, use ISO dates (`YYYY-MM-DD`), and use only `Open` or `Resolved` for issue status.
- Assign issue IDs sequentially, update the existing entry as an issue progresses, and never duplicate an issue. Use `Pending` for unknown fields while an issue is open, and replace every `Pending` value when it is resolved.

## Version-control completion

- Treat this file as standing authorization to make an ordinary commit and non-force push to the repository's configured upstream after each successful run that changes files.
- Before committing, inspect `git status` and the diff. Stage only files created or intentionally changed for the current request; never include unrelated user changes.
- Use a short, descriptive commit message. For reports, prefer `analysis: add <subject> five forces` or `analysis: update <subject> five forces`.
- Push the current branch to its configured upstream. If `origin` exists but the branch has no upstream, set it with an ordinary `git push -u origin HEAD`.
- Never force-push, rewrite published history, delete branches, or change the configured remote as part of this automation.
- If there are no changes, do not create an empty commit.
- If Git, a remote, authentication, permissions, or network access is unavailable, preserve the saved file and any local commit, report the exact blocker, and do not claim that the push succeeded.
