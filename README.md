# tushare-skills

A task-oriented Tushare skill repository focused on **real user workflows**, not just endpoint listings.

This repository is the **full working version** of the upgraded Tushare skill package, including:
- the main `tushare/SKILL.md`
- supporting references for task routing, examples, workflow playbooks, output templates, FAQ, and regression checks
- continuity and validation notes under `tushare/research/`

---

## What this repository is

`tushare-skills` is a practical Tushare skill repository built around **real finance research tasks in Chinese natural language**.

Instead of treating Tushare as a long API catalog, this repository organizes the skill around questions users actually ask, such as:
- 看看这只股票最近怎么样
- 查下财报趋势
- 最近哪个板块最强
- 北向资金最近在买什么
- 帮我筛一批股票
- 导出一份行情数据
- 给我做个研究简报

The goal is to make Tushare usable as a **workflow skill**, not just a reference document.

---

## Relationship to the upstream PR

A conservative upstream PR has already been submitted to:
- `waditu-tushare/skills`

That upstream PR focuses on updating the **main `tushare/SKILL.md` only**, so it is easier for the maintainers to review and accept.

This repository keeps the **full validated package** locally and on GitHub, including:
- references
- research / trial notes
- fix plans
- retest summaries
- final verdict

In short:
- **upstream PR** = lightweight, easier-to-review contribution
- **this repository** = full skill package with supporting materials and validation history

---

## Current maturity

Current stage assessment:

> **Mature enough for real long-term use**

Internal working verdict:

> **9.2 / 10**

Why:
- main workflows have been restructured around tasks instead of endpoint dumps
- regression design was completed
- real smoke tests were run
- real business trials were run across multiple task types
- boundary / ambiguity / failure cases were tested
- first-round fixes were applied and retested

This repository is no longer just a draft skill.
It is an actively validated workflow package.

---

## What has been validated

### Real task categories validated
- single-stock price analysis
- financial trend reading
- valuation snapshot
- northbound fund-flow interpretation
- sector rotation lookup
- multi-asset comparison
- candidate screening
- CSV export workflow
- ambiguity handling
- non-trading-day empty-result handling
- permission-boundary handling
- ultra-short high-frequency user phrasing

### Real interface paths validated
Examples include:
- `trade_cal`
- `stock_basic`
- `daily`
- `daily_basic`
- `fina_indicator`
- `moneyflow_hsgt`
- `index_daily`
- `cn_cpi`
- `hsgt_top10`

A real permission boundary was also observed on:
- `anns_d`

So this repository includes both success-path validation and failure-path handling.

---

## Repository structure

```text
tushare/
  SKILL.md
  references/
    endpoint-map.md
    examples.md
    workflow-playbooks.md
    output-templates.md
    faq.md
    regression-checklist.md
  research/
    tushare-data-implementation-summary-2026-03-23.md
    tushare-data-real-trial-report-2026-03-23.md
    tushare-data-fix-plan-2026-03-23.md
    tushare-data-fix-round1-summary-2026-03-23.md
    tushare-data-boundary-trial-summary-2026-03-23.md
    tushare-data-verdict-2026-03-23.md
```

### Roles of each layer
- `SKILL.md` → main task-oriented skill definition
- `references/` → reusable support files for execution, output, FAQ, examples, and regression
- `research/` → continuity and validation history

---

## How to use

### 1. Environment
You need:
- Python
- `tushare`
- a valid `TUSHARE_TOKEN`

Install:

```bash
pip install tushare -i https://pypi.tuna.tsinghua.edu.cn/simple
```

Set token:

```bash
export TUSHARE_TOKEN=your_token
```

---

### 2. Main entry
Start from:
- `tushare/SKILL.md`

That is the main skill definition.

---

### 3. When you need more detail
Use:
- `references/examples.md` for real user phrasing
- `references/workflow-playbooks.md` for execution rules
- `references/output-templates.md` for result shapes
- `references/faq.md` for pitfalls and boundary handling
- `references/regression-checklist.md` for validation and testing

---

### 4. If you want the reasoning history
Read:
- `research/` files

These explain:
- why the skill was restructured
- what was tested in real runs
- what failed
- what was fixed
- the current maturity verdict

---

## Current limitations

This repository is mature, but not “finished forever.”

Still worth improving over time:
- richer finance trend modes (single-quarter / cumulative / YoY / TTM)
- stronger valuation context (historical percentile / peer comparison)
- more research-grade screening defaults
- one more full-scale export validation beyond sample export
- more issue-driven iteration from real long-term usage

---

## Security / secret handling

This repository should not contain:
- raw API tokens
- private keys
- reusable secrets

Current review result:
- no obvious API key or private key leakage was found in the tracked working files during local scanning before writing this README

Still, when adding future notes or examples:
- never commit real `TUSHARE_TOKEN`
- never commit SSH private keys
- never paste live GitHub tokens into research notes

---

## Suggested working mode going forward

Recommended maintenance loop:
1. use the skill in real tasks
2. capture concrete failures or friction points
3. update the relevant workflow / FAQ / examples
4. retest the affected cases
5. record the change in `research/` if it affects future continuity

This repository should evolve from **real usage**, not from endlessly expanding endpoint lists.

---

## Summary

`tushare-skills` is the full, validated, task-oriented Tushare skill package.

It exists to preserve not only the skill itself, but also the execution logic, test evidence, fixes, and continuity needed to make the skill genuinely useful over time.
