# Stock Industry Analysis

An evidence-driven Codex skill for analyzing public and private companies and industries with Porter Five Forces, industry-chain mapping, brand-power and ecosystem-control assessment, and public sources.

The skill focuses on business quality and industry structure. It does not provide an automatic buy/sell recommendation, price target, or valuation.

## What it produces

- Company and industry definition
- Industry-chain, brand-power, and ecosystem-control assessment
- Five-year profitability baseline
- Every required Porter Five Forces sub-point
- Force-level ratings, trends, confidence, and stock-relevant implications
- Evidence-based Increase and Decrease news catalysts for potential 1–5-trading-day volatility in listed stocks
- Source links and an explicit completion check

Completed reports are saved in [`company-analyses/`](company-analyses/). The default report retains ten sections and all 56 analytical rows; unsupported or inapplicable assessments remain visible with explicit explanations. The final chat response is concise and links to the full saved report.

## Use with Codex

Install this repository with Codex's Skill Installer, or place the repository directory at `~/.agents/skills/stock-industry-analysis`. Restart Codex if the skill does not appear immediately.

Invoke it explicitly with a request such as:

```text
$stock-industry-analysis analyze Costco and save the completed report.
```

Codex can also select the skill automatically when a request matches the description in [`SKILL.md`](SKILL.md).

## GPT-6 setup

The local configuration inspected on 2026-09-06 uses this baseline:

```toml
model = "gpt-6-astra"
model_reasoning_effort = "high"
```

This is the existing setup, not a benchmarked optimum. Runtime configuration selects the model and reasoning effort; `SKILL.md` defines the analysis behavior. The GPT-6 adaptation preserves those settings and adds no repository runtime override. See [Codex configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic) for configuration locations and precedence.

The instructions follow [OpenAI's GPT-6 guidance](https://developers.openai.com/api/docs/guides/latest-model) by clarifying decisions and completion criteria, reducing repeated instructions, and keeping verification proportional to the work. The analytical methodology stays in the root skill.

Research requires tools that can search and inspect public sources, including the latest available filings and relevant recent developments. Non-US issuers use applicable annual/interim disclosures; private-company and industry reports use accessible public evidence. Verify publication dates and source contents against the research cutoff. Codex documents `web_search = "live"` for current retrieval; search settings remain controlled by the runtime and its permissions, not by this skill.

## Repository workflow

Repository-specific instructions live in [`AGENTS.md`](AGENTS.md). In execution mode, each completed analysis must be saved under `company-analyses/`, committed, and pushed to the configured upstream within the active permissions. Plan mode remains read-only. If Git, a remote, authentication, permissions, or network access is unavailable, the local result is preserved and the exact blocker is reported.

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

Missing disclosure, inaccessible sources, and inapplicable metrics are distinguished in the report. Proxies require evidence; missing financial history is not filled with invented values. If source access prevents current research, Codex reports the limitation rather than presenting unverified research as complete. Existing reports retain their historical methodology until rerun.

This repository is for informational and educational purposes only and is not investment advice.

## License

Released under the [MIT License](LICENSE).
