# Short-Term Plan (Phased) — with Value Examples

## Phase 1 — Work locally with CSVs

**Definition of Done:** One script/notebook turns raw CSV → cleaned CSV with tests.

- **3’s**
  - Write `clean_names`, `clean_phone`, `clean_email` with `pytest` cases
  - Build `check_contact_uniqueness(df)` (flags dup/ambiguous) + tests
  - Produce a simple CLI/notebook that runs end-to-end on a sample file
- **2’s**
  - README: how to run; sample data folder; `run.sh` or Makefile
  - VS Code launch config; `.env.example`
- **1’s**
  - Manual spreadsheet fixes to unblock today’s deliverable
- **0’s**
  - Refactoring variable names for an hour without adding tests or features

## Phase 2 — Connect to Google Sheets

**DoD:** Round-trip pipeline (Sheets → Python clean → Sheets) with a review tab.

- **3’s**
  - gspread: read from a Sheet, write cleaned results + “Review_Conflicts” tab
  - Ingest human decisions back and finalize outputs
- **2’s**
  - Permissions/service account setup doc; sample config JSON; error-handling notes
- **1’s**
  - Manual copy/paste between Sheets
- **0’s**
  - Re-arranging Sheet colors or tab names for aesthetics

## Phase 3 — Connect to Action Builder (psycopg3) & Windmill

**DoD:** Query AB into pandas, run cleaners, write back (or emit upload file), optionally scheduled on Windmill.

- **3’s**
  - `psycopg3` connector module; parameterized queries; safe writes/updates
  - Job that runs your Phase-1/2 cleaners on live subsets
- **2’s**
  - Small design doc: tables touched, constraints, rollback plan
  - Windmill job setup instructions; secrets handling
- **1’s**
  - Running the same SQL manually in a GUI when a script exists
- **0’s**
  - Exploring “cool” platforms without a concrete job to run
