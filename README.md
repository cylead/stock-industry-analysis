# Stock Industry Analysis

An evidence-driven Codex skill for analyzing public companies and industries with Porter Five Forces, industry-chain mapping, ecosystem-control assessment, and public filings.

The skill focuses on business quality and industry structure. It does not provide an automatic buy/sell recommendation, price target, or valuation.

## What it produces

- Company and industry definition
- Industry-chain and ecosystem-control assessment
- Five-year profitability baseline
- Every required Porter Five Forces sub-point
- Force-level ratings, trends, confidence, and stock-relevant implications
- Source links and an explicit completion check

Completed reports are saved in [`company-analyses/`](company-analyses/).

## Use with Codex

Install this repository with Codex's Skill Installer, or place the repository directory at `~/.agents/skills/stock-industry-analysis`. Restart Codex if the skill does not appear immediately.

Invoke it explicitly with a request such as:

```text
$stock-industry-analysis analyze Costco and save the completed report.
```

Codex can also select the skill automatically when a request matches the description in [`SKILL.md`](SKILL.md).

## Repository workflow

Repository-specific instructions live in [`AGENTS.md`](AGENTS.md). Each completed analysis must be saved under `company-analyses/`, committed, and pushed to the configured upstream. If no remote or authentication is available, the local result is preserved and the blocker is reported.

Material analysis-skill changes are recorded in [`PROJECT_LOG.md`](PROJECT_LOG.md). Noteworthy project issues, their solutions, and the reasons for choosing those solutions are recorded in [`ISSUE_LOG.md`](ISSUE_LOG.md).

## Repository structure

```text
.
├── AGENTS.md
├── ISSUE_LOG.md
├── PROJECT_LOG.md
├── SKILL.md
├── company-analyses/
├── LICENSE
└── README.md
```

## Research limitations

Reports are point-in-time research based on public sources. Financial data, competitive conditions, regulations, and source URLs can change. Check each report's research date and verify material facts before relying on it.

This repository is for informational and educational purposes only and is not investment advice.

## License

Released under the [MIT License](LICENSE).
