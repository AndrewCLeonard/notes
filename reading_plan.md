# Reading Plan — Python, Pandas, SQL

## Priority 1: Python for Data Analysis (Wes McKinney, 3rd Edition)

**Why:** Written by the creator of Pandas; directly targets data cleaning and CSV/Sheets-like operations.

**Start here:**

- **Chapter 4: NumPy Basics** (arrays, vectorization) — skim if you're not doing math-heavy work
- **Chapter 5: Getting Started with Pandas** (Series, DataFrame, reading CSVs)
- **Chapter 7: Data Cleaning and Preparation** ← YOUR PRIORITY
  - Missing data handling
  - String manipulation (your name cleaning use case)
  - Removing duplicates
- **Chapter 8: Data Wrangling (Join, Combine, Reshape)** ← YOUR PRIORITY
  - Merging datasets (your AB + plant roster matching)
  - Concatenating (stacking multiple files)

**Timeline:** 2-3 weeks. Read chapters 5, 7, 8 first. Implement one example from each in your Phase 1 script.

**3rd edition is available online** — start there.

---

## Priority 2: Effective Pandas (Matt Harrison)

**Why:** Short, opinionated guide to **idiomatic Pandas** (not just "what works," but "what's clean and maintainable").

**Start here:**

- **First 100 pages** (method chaining, vectorized operations)
- Focus on: `.str` methods (your name cleaning), `.apply()` vs vectorization, avoiding loops

**Timeline:** 1 week. Read after McKinney chapters 5, 7, 8.

**Key lesson:** You'll learn to replace 20 lines of for-loops with 2 lines of method chaining.

---

## Priority 3: SQL for Data Analysis (Cathy Tanimura)

**Why:** Your AB SQL mirror is read-only, so you need advanced `SELECT` skills (joins, window functions, CTEs).

**Start here:**

- **Chapter 3: Joins** (INNER, LEFT, OUTER — your matching use case)
- **Chapter 4: Aggregations** (GROUP BY, HAVING)
- **Chapter 5: Window Functions** (RANK, ROW_NUMBER — for de-duping common names)

**Timeline:** 2 weeks. Do the exercises in a SQL notebook or against your AB mirror.

**Key lesson:** You'll learn to do "match the top-ranked result per group" in SQL instead of exporting to Sheets.

---

## Reference (Keep, Don't Read Cover-to-Cover)

### Learning Python (Lutz)

**Use case:** Look up concepts when you're stuck (e.g., "What's a generator?" "How do decorators work?").

**Don't:** Read it linearly. It's 1,600 pages and you don't need 80% of it.

---

### Automate the Boring Stuff (Sweigart)

**Use case:** Quick reference for file I/O, regexes, or Excel automation if McKinney doesn't cover it.

**Don't:** Re-read chapters on basic syntax. You're past that.

---

## Reading Workflow (6-8 Weeks)

**Weeks 1-3:** McKinney chapters 5, 7, 8  
→ Implement `normalize_name` and `match_workers` from what you learn

**Week 4:** Harrison, first 100 pages  
→ Refactor your Phase 1 code to use method chaining

**Weeks 5-6:** Tanimura chapters 3-5  
→ Write 3 SQL queries that replace your current "export to Sheets for VLOOKUP" workflow

**Weeks 7-8:** Catch-up / apply to real projects  
→ Ship Phase 1b using what you've learned
