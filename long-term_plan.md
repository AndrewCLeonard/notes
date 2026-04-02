# My Values

I am extending my spreadsheet fluency into Python, not starting over.

**Constraints:**

- All learning must directly replace an existing manual workflow or reduce operational risk.
- I prioritize correctness, reuse, and clarity over speed or novelty.

> 3 = Mission-critical to growth (builds reusable skills/assets)  
> 2 = High-value enablers (support systems that accelerate 3's)  
> 1 = Current state (to be automated)  
> 0 = Avoidance / drift (busywork, rabbit holes)

## 3 — Mission-Critical (with Automation Examples)

- **Python fluency (Pandas, regex, reusable functions)**  
  → Replaces: manual find/replace across 50 spreadsheets; formula-based name cleaning
- **Fuzzy matching (rapidfuzz, thefuzz)**  
  → Replaces: 2-hour manual review of "is John Smith = Jon Smyth?"; common-name disambiguation
- **SQL depth (joins, window functions, EXPLAIN)**  
  → Replaces: exporting to Sheets to do VLOOKUP logic; multi-step aggregation queries
- **APIs/connectors (gspread, psycopg3, AB API)**  
  → Replaces: copy/paste between systems; manual data entry from SQL results
- **Testing/reproducibility (pytest, regression datasets)**  
  → Replaces: "did I break something?" paranoia; re-testing cleaners by hand each time
- **Shipping artifacts (CLI, notebooks others can run)**  
  → Replaces: "can you run this for me?" requests; me as the bottleneck
- **Git: branching, PRs, merging, conflict resolution**  
  → Enables team work, rollback, and version control for query library

## 2 — High-Value Enablers

- Project scaffolding (READMEs, `.env`, Makefile, configs)
- Dev environment & workflow (venv/poetry, VS Code setup)
- Architecture/communication (UML, design docs)
- Light performance exploration (timing, profiling)
- Git: repo hygiene (`.gitignore`, commit conventions, CI hooks)

## 1 — Current State (To Be Automated)

- Spreadsheet cleaning → target for Phase 1 scripts
- Manual data entry / copy-paste → target for Phase 2/3 pipelines
- Ad-hoc dashboards → candidate for scheduled jobs
- Row-by-row match review → target for fuzzy matching + confidence scores

## 0 — Avoidance / Drift

- Endless formatting or reorganizing notes without output
- Tool shopping/tinkering without a concrete need
- Premature optimization / yak-shaving
- Reading tutorials without implementing
- Bikeshedding commit messages or variable names

## Coding Slang

- **yak-shaving:** getting stuck doing a long chain of side-tasks before the _real_ task (e.g., "to write tests I need a linter → to set up the linter I need a config → to…"). useful awareness; try to time-box or defer.
- **bikeshedding:** spending lots of time on trivial choices (like colors, naming) because they're easy to argue about, while hard/important work gets sidelined. notice it and move on.
