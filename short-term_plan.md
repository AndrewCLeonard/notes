# Short-Term Plan (Phased) — with Value Examples

## Phase 1a — Core Name Cleaner (Week 1)

**Definition of Done:** One Python function (`normalize_name`) with 10 pytest cases that handles your real-world edge cases.

- **3's**
  - Translate your Sheets formula to Python: `John O'Neill` → `johnoneill`
  - Handle accents (`unicodedata.normalize`), apostrophes, hyphens, suffixes (Jr/Sr/II/III)
  - Write pytest cases for: apostrophes, accents, hyphens, multiple spaces, all-caps, mixed case, empty strings, None, suffixes
  - Run on a sample of 50 real names from a recent project; fix any failures
- **2's**
  - README: what the function does, how to run tests
  - Sample data file (`test_names.csv`) with edge cases
- **1's**
  - Manual Sheets cleaning to unblock today's deliverable
- **0's**
  - Refactoring variable names for aesthetics without adding tests

## Phase 1b — Fuzzy Matching + Confidence Scores (Week 2-3)

**DoD:** Script that takes two CSVs (AB export + plant roster), matches on normalized names, outputs a "Review" CSV with confidence scores for ambiguous matches.

- **3's**
  - Implement `match_workers(df_ab, df_plant)` using `rapidfuzz` or `thefuzz`
  - Add phone/email as secondary match signals (if name match is <90%, check phone)
  - Output CSV with columns: `ab_name`, `plant_name`, `match_score`, `phone_match`, `needs_review` (boolean)
  - Test on 2-3 real projects from the last month; compare to your manual results
- **2's**
  - CLI or notebook wrapper (`python match.py --ab export.csv --plant roster.csv`)
  - Config for match thresholds (90% = auto-accept, 70-89% = review, <70% = no match)
- **1's**
  - Manual filter-and-compare for common names (you're replacing this)
- **0's**
  - Exploring other fuzzy matching libraries without benchmarking on your data

## Phase 2 — Connect to Google Sheets (Week 4-5)

**DoD:** Round-trip pipeline (Sheets → Python clean/match → Sheets) with a "Review_Conflicts" tab.

- **3's**
  - `gspread`: read from Sheet A (AB export) and Sheet B (plant roster)
  - Run Phase 1a+1b cleaners on both datasets
  - Write results to Sheet C with tabs: "Auto_Matched" (score >90%), "Review" (70-89%), "No_Match" (<70%)
  - Ingest human decisions from "Review" tab (add a "Decision" column) and finalize outputs
- **2's**
  - Service account setup doc; permissions guide; error-handling notes
  - Sample config JSON (which sheets, which tabs, which columns to match on)
- **1's**
  - Manual copy/paste between Sheets
- **0's**
  - Re-arranging Sheet colors or tab names for aesthetics

## Phase 3a — Read from Action Builder SQL Mirror (Week 6)

**DoD:** Query AB workers into Pandas DataFrame using psycopg3; replaces manual "write SQL → copy/paste to Sheets" workflow.

- **3's**
  - Write `get_workers_by_plant(plant_id)` using psycopg3 (read-only connection)
  - Return Pandas DataFrame with worker ID, name, phone, email
  - Test: output matches your manual SQL query results
  - Use in Phase 1b matching workflow (replace CSV input with SQL query)
- **2's**
  - Connection config (`.env` for DB credentials; example queries in README)
  - Error handling (connection failures, query timeouts)
- **1's**
  - Running the same SQL manually in a GUI when a script exists
- **0's**
  - Rewriting working queries "just to practice SQL"

**Key decision:** SQL mirror for reads (fast, flexible). Action Builder API for writes only (see Phase 3b).

## Phase 3b — Write to Action Builder API (Week 7-8, if needed)

**DoD:** Upload matched workers to AB campaigns via API; handle rate limits and retries.

**Only do this phase if you need programmatic writes.** If goal is "produce clean CSV for manual upload," skip to Phase 4 (scheduling/Windmill).

- **3's**
  - Write `upload_matched_workers(df, campaign_id)` using AB API client
  - Handle rate limits (retry with backoff), auth tokens, error responses
  - Test on small batch (10 workers) before production runs
  - Validate: records appear in AB with correct fields
- **2's**
  - API authentication setup doc; secrets handling (API keys in `.env`)
  - Logging: track success/failure counts, retry attempts
- **1's**
  - Manual uploads when the script exists and works
- **0's**
  - Building a "universal AB client" before you need 2+ API endpoints

**Why separate from Phase 3a:** Reading (SQL) and writing (API) solve different problems. Don't learn both until you've shipped reads.

## Phase 4 — Schedule & Monitor (Week 9+, optional)

**DoD:** Recurring matches run automatically (Windmill or cron); you review outputs instead of running scripts.

- **3's**
  - Windmill job: weekly query + match + output to review Sheet
  - Monitoring: email/Slack alert if match rate drops below 80% (signals data quality issue)
- **2's**
  - Runbook: "What to do when the job fails" (common errors, how to re-run)
  - Secrets management in Windmill (DB creds, API keys, service account)
- **1's**
  - Running the job manually every week when it could be scheduled
- **0's**
  - Over-engineering alerts for edge cases that happen once a year

---

## Captain's Log — Daily Artifact

| Date       | Task                   | Value | Time | Blocked By                         | What I Learned                          |
| ---------- | ---------------------- | ----- | ---- | ---------------------------------- | --------------------------------------- |
| 2025-02-12 | normalize_name + tests | 3     | 1.5h | —                                  | unicodedata.normalize vs .translate     |
| 2025-02-13 | psycopg3 connection    | 3     | 1h   | DB credentials (requested from IT) | Connection pooling vs single connection |

---

## Weekly Review (Obsidian Template — Paste into Sunday Note)

```markdown
## Weekly Review — [Date Range]

### 1. What 3-value work shipped this week?

- [ ] Link to artifact / PR / notebook
- [ ] What manual task does this replace?

### 2. What blocked me that I can fix next week?

- [ ] Tools I need (access, libraries, docs)
- [ ] Knowledge gaps (concepts to study, skills to practice)
- [ ] External dependencies (IT requests, approvals)

### 3. What 1-value work took >4 hours that should be automated?

- [ ] Task description
- [ ] Candidate phase to automate it (1, 2, 3a, 3b, or 4?)

**Key changes:**

- Split Phase 3 into **3a (SQL reads)** and **3b (API writes)** with clear decision point
- Added "Why separate" note explaining SQL vs API tradeoffs
- Made Phase 3b conditional ("only if you need programmatic writes")
- Added Phase 4 (scheduling) as optional next step after reads/writes work
- Updated Captain's Log example to reference Phase 3a task
```
