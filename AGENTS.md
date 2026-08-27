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

## Version-control completion

- Treat this file as standing authorization to make an ordinary commit and non-force push to the repository's configured upstream after each successful run that changes files.
- Before committing, inspect `git status` and the diff. Stage only files created or intentionally changed for the current request; never include unrelated user changes.
- Use a short, descriptive commit message. For reports, prefer `analysis: add <subject> five forces` or `analysis: update <subject> five forces`.
- Push the current branch to its configured upstream. If `origin` exists but the branch has no upstream, set it with an ordinary `git push -u origin HEAD`.
- Never force-push, rewrite published history, delete branches, or change the configured remote as part of this automation.
- If there are no changes, do not create an empty commit.
- If Git, a remote, authentication, permissions, or network access is unavailable, preserve the saved file and any local commit, report the exact blocker, and do not claim that the push succeeded.
