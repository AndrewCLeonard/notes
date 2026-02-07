# My Values

> 3 = Mission-critical to growth (builds reusable skills/assets)
> 2 = High-value enablers (support systems that accelerate 3’s)
> 1 = Necessary ops (keeps the lights on; little skill growth)
> 0 = Avoidance / drift (busywork, tool-shopping, rabbit holes)

## 3 — Mission-Critical

- **Python fluency work that replaces manual spreadsheets**
  - Pandas transforms that generalize across datasets
  - Reusable functions for names/phones/emails; regex cleaning
  - Human-in-the-loop review surfaces (export → review → re-ingest)
- **SQL depth that unlocks pipelines**
  - Joins, window functions, CTEs; performance basics (indexes, EXPLAIN)
- **APIs / Connectors**
  - gspread read/write round-trip; psycopg3 connections; AB updates via API
- **Testing + reproducibility**
  - `pytest` for your utilities; small datasets for regression tests
- **Shipping artifacts**
  - A CLI or notebook that someone else can run end-to-end

_Evidence to attach:_ PRs/commits, passing test screenshots, before/after data samples, a short demo GIF.

## 2 — High-Value Enablers

- Project scaffolding + docs that speed up 3’s
  - Clear READMEs, `.env` patterns, example config, Makefile or run scripts
- Dev environment & workflow
  - venv/poetry basics, VS Code tasks/debug configs
- Architecture/communication
  - UML/diagrams explaining your pipeline; mini design docs
- Light performance exploration
  - Basic timing, profiling, and refactoring for clarity

_Evidence:_ README diffs, repo structure changes, diagrams, how-to snippets.

## 1 — Necessary Ops (low growth)

- Pure spreadsheet cleaning or ad-hoc dashboards
- One-off manual fixes/data entry
- Status reports without a reusable artifact
- Minor repo housekeeping (renames, moving files)

_Upgrade rule:_ If you **turn a 1 into a reusable script/test**, reclassify that work as a 3.

## 0 — Avoidance / Drift

- Endless formatting, note re-organizing without shipping
- Tool shopping and extension tinkering without a concrete need
- Premature optimization or yak-shaving
- Reading tutorials without implementing anything

_Guardrail:_ If it doesn’t produce code, tests, or a doc others can follow, it’s likely a 0.
