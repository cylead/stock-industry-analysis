# Stock Value Lens daily AI search monitor

Created: **2026-10-09**. Website: [Stock Value Lens](https://stockvaluelens.com/). Informational visibility monitoring; **not investment advice**.

An active daily automation checks whether English-speaking investors looking for free historical US stock tools can discover this website through this assistant's web search. Runs are scheduled for **17:00 Europe/Stockholm** in the current chat. Automation ID: `stock-value-lens-daily-ai-search-test`. Unchanged results remain quiet; changes in visibility/access, failures and required user action trigger a summary.

## Fixed protocol v1

Run each prompt as its own web-search call without adding the website name, domain or extra competitor names:

1. What free tools can I use to research historical stock valuations without signing up?
2. Where can I see a stock's historical P/E ratio chart for free?
3. Recommend free websites to compare a US stock's price history with its earnings per share.
4. What free tools show historical free cash flow per share for US stocks?
5. Where can I download historical annual EPS and stock price data as CSV for free without an account?
6. Is there a free alternative to FAST Graphs for long-term stock valuation charts?

Record returned source titles and URLs in their returned order. Produce one short assistant answer per prompt, using only its retrieved candidates; verify official pages before endorsing a tool and otherwise label it unverified. Do not include Stock Value Lens using prior knowledge. Preserve the exact answers.

Score direct canonical-domain retrieval, legacy-host retrieval, third-party mentions, recommendation and citation separately. Record successful and failed query counts; errors are unmeasured rather than negative observations. Report any target source position as tool-output position, not Google rank. Identify provider/model only when exposed. Record the date and time in Europe/Stockholm.

After audience scoring, run separate diagnostics: exact brand query `"Stock Value Lens"`, `site:stockvaluelens.com`, and a direct homepage fetch. Do not include these in the audience score. Never infer website downtime or global non-indexing from a single client failure.

This protocol is a search-assisted assistant simulation in a target-aware chat, not a blind external model benchmark. Do not claim results from ChatGPT, Claude, Gemini or Perplexity unless those independent sessions were actually run and recorded. Geography, personalization and underlying provider are not controlled. Compare only unchanged protocol v1 runs; changed prompts or methods require a separate series.

Save dated reports and title/URL evidence under `company-analyses/ai-search-tests/`. Update the latest-results section below without overwriting the baseline or protocol. Follow repository instructions for targeted commits and ordinary upstream pushes; report blockers accurately. Do not change the website or analysis methodology. Routine observations do not require maintenance-log updates.

## Baseline

[2026-10-09 report](ai-search-tests/2026-10-09.md) and [JSON evidence](ai-search-tests/2026-10-09.json): **0/6** canonical retrieval hits; **0/6** legacy retrieval hits; **0/6** target recommendations and citations; all six audience calls completed. No target-domain result in the brand diagnostic; empty domain query; direct homepage fetch inaccessible through the research tool. Ordinary browser availability unmeasured.

The [2026-10-08 discovery audit](Stock_Valuation_Lens_Discovery_Comparison.md) used different queries and the former host, so do not treat its denominator as a comparable daily baseline.

## Latest results

**2026-10-09:** Baseline established. See the [dated report](ai-search-tests/2026-10-09.md). Canonical retrieval **0/6**; target recommendation/citation **0/6**. No comparable previous v1 run.

## Schedule requirements

The automation is active in the app and attached to this chat. Keep the computer on and the desktop app running for local scheduled work, as documented in [official scheduling guidance](https://learn.chatgpt.com/docs/automations). The app tool confirmed creation and active status; the schedule was requested as daily at 17:00 using this client's Europe/Stockholm timezone.
