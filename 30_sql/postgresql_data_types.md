# PostgreSQL Data Types

Created: 2026-04-07
_For: Daily work + technical interview prep_

---

## Documentation Links

- **Full type reference**: <https://www.postgresql.org/docs/current/datatype.html>
- **Type conversion**: <https://www.postgresql.org/docs/current/typeconv.html>
- **Cast functions**: <https://www.postgresql.org/docs/current/functions-formatting.html>

---

## Casting — The Two Patterns

```sql
-- PostgreSQL shorthand (most common in practice)
value::target_type

-- ANSI SQL standard (works in any database)
CAST(value AS target_type)
```

These are identical in behavior. Use `::` day-to-day, know `CAST()` for interviews since it's database-agnostic.

```sql
-- Examples
created_at::date              -- timestamp → date (drops time)
'2024-01-01'::date            -- string → date
id::text                      -- integer → string
'42'::integer                 -- string → integer
price::numeric(10,2)          -- cast with precision
```

---

## Numeric Types

| Type               | Storage  | Range                               | Use When              |
| ------------------ | -------- | ----------------------------------- | --------------------- |
| `SMALLINT`         | 2 bytes  | -32,768 to 32,767                   | Small counts, flags   |
| `INTEGER` / `INT`  | 4 bytes  | -2.1B to 2.1B                       | Most IDs and counts   |
| `BIGINT`           | 8 bytes  | -9.2 quintillion to 9.2 quintillion | Large IDs, row counts |
| `NUMERIC(p,s)`     | variable | user-defined                        | Money, exact decimals |
| `DECIMAL(p,s)`     | variable | same as NUMERIC                     | Alias for NUMERIC     |
| `REAL`             | 4 bytes  | 6 decimal digits                    | Scientific data       |
| `DOUBLE PRECISION` | 8 bytes  | 15 decimal digits                   | Scientific data       |

**Interview note:** `FLOAT` is imprecise — never use it for money. Use `NUMERIC` or store as integer cents.

```sql
-- Money: store as cents (integer) or use NUMERIC
price NUMERIC(10, 2)   -- up to 99,999,999.99
```

---

## String Types

| Type                   | Description                      | Use When                        |
| ---------------------- | -------------------------------- | ------------------------------- |
| `VARCHAR(n)`           | Variable length, max n chars     | When you know max length        |
| `CHARACTER VARYING(n)` | Same as VARCHAR(n)               | Same                            |
| `TEXT`                 | Unlimited length                 | Most string columns in practice |
| `CHAR(n)`              | Fixed length, padded with spaces | Rare — legacy systems           |

**Interview note:** In PostgreSQL, `TEXT` and `VARCHAR` have identical performance. There's no reason to use `CHAR(n)` in modern schemas. You'll see `VARCHAR` in older codebases.

---

## Date & Time Types

| Type          | Storage  | Format                   | Use When                  |
| ------------- | -------- | ------------------------ | ------------------------- |
| `DATE`        | 4 bytes  | `YYYY-MM-DD`             | Date only, no time        |
| `TIME`        | 8 bytes  | `HH:MM:SS`               | Time only, no date        |
| `TIMESTAMP`   | 8 bytes  | `YYYY-MM-DD HH:MM:SS`    | Date + time, no timezone  |
| `TIMESTAMPTZ` | 8 bytes  | `YYYY-MM-DD HH:MM:SS+TZ` | Date + time with timezone |
| `INTERVAL`    | 16 bytes | `1 year 2 months`        | Duration/difference       |

**Interview note:** Always use `TIMESTAMPTZ` over `TIMESTAMP` for production systems — it stores UTC and converts to local timezone on retrieval. `TIMESTAMP` has no timezone awareness and causes bugs in distributed systems.

```sql
-- Common date operations
NOW()                          -- current timestamp with timezone
CURRENT_DATE                   -- today's date
created_at::date               -- strip time from timestamp
AGE(timestamp)                 -- interval from timestamp to now
DATE_TRUNC('month', created_at) -- truncate to month boundary
EXTRACT(year FROM created_at)  -- pull out year as number
```

---

## Boolean

| Type      | Values                    | Storage |
| --------- | ------------------------- | ------- |
| `BOOLEAN` | `TRUE` / `FALSE` / `NULL` | 1 byte  |

```sql
is_active BOOLEAN DEFAULT TRUE

-- Comparisons
WHERE is_active = TRUE
WHERE is_active            -- shorthand, same as = TRUE
WHERE NOT is_active        -- same as = FALSE
```

**Interview note:** NULL is not FALSE. `WHERE is_active` will not return NULL rows. Use `WHERE is_active IS NOT FALSE` if you want NULLs included.

---

## NULL Behavior — Critical for Interviews

NULL is not a value — it's the absence of a value. This causes counterintuitive behavior:

```sql
NULL = NULL      -- NULL (not TRUE)
NULL != NULL     -- NULL (not TRUE)
NULL = 195       -- NULL (not FALSE, not TRUE)
NULL > 0         -- NULL

-- Correct NULL checks
WHERE column IS NULL
WHERE column IS NOT NULL

-- Safe equality check (treats NULL as comparable)
WHERE column IS DISTINCT FROM other_column
WHERE column IS NOT DISTINCT FROM other_column
```

**Interview note:** This is why the LEFT JOIN/WHERE trap works the way it does. Filtering `WHERE joined_table.column = value` drops NULL rows because `NULL = value` is NULL, not true.

---

## JSON Types (PostgreSQL-specific)

| Type    | Description                          | Use When                |
| ------- | ------------------------------------ | ----------------------- |
| `JSON`  | Stores text, validates JSON syntax   | Rarely — use JSONB      |
| `JSONB` | Binary JSON, indexed, faster queries | Production JSON columns |

```sql
-- Extracting from JSONB
properties->>'key'              -- returns text
properties->'key'               -- returns JSON
properties#>>'{nested,key}'     -- nested path, returns text

-- Checking existence
properties ? 'key'              -- does key exist?
```

**Note for your work:** Your ClickHouse schema uses `JSONExtractString()`. PostgreSQL uses `->>'key'` notation instead. Different syntax, same concept.

---

## Array Types (PostgreSQL-specific)

```sql
-- Define an array column
tags TEXT[]

-- Array literal
ARRAY['cat', 'dog', 'bird']

-- Array operations
WHERE 'cat' = ANY(tags)          -- value in array
WHERE tags @> ARRAY['cat']       -- array contains value
UNNEST(tags)                     -- explode array to rows (like ARRAY JOIN in ClickHouse)

-- Common use: IN with dynamic list
WHERE id = ANY(ARRAY[1, 2, 3])   -- equivalent to IN (1, 2, 3)
```

---

## UUID

```sql
UUID    -- 128-bit identifier, e.g. '550e8400-e29b-41d4-a716-446655440000'
```

```sql
-- Generate a UUID
gen_random_uuid()

-- Cast string to UUID
'550e8400-e29b-41d4-a716-446655440000'::uuid

-- Common gotcha: UUIDs can't use ILIKE — cast first
WHERE id::text ILIKE '%ae4e42ab%'
```

---

## Type Conversion Reference

| From        | To        | Syntax                                |
| ----------- | --------- | ------------------------------------- |
| `TIMESTAMP` | `DATE`    | `ts::date`                            |
| `DATE`      | `TEXT`    | `dt::text`                            |
| `INTEGER`   | `TEXT`    | `id::text`                            |
| `TEXT`      | `INTEGER` | `'42'::integer`                       |
| `TEXT`      | `DATE`    | `'2024-01-01'::date`                  |
| `TEXT`      | `NUMERIC` | `'3.14'::numeric`                     |
| `UUID`      | `TEXT`    | `uuid_col::text`                      |
| `BOOLEAN`   | `INTEGER` | `bool_col::integer` (TRUE=1, FALSE=0) |

---

## Interview Cheat Sheet

| Question type                | Key points                                                                      |
| ---------------------------- | ------------------------------------------------------------------------------- |
| "What type for money?"       | `NUMERIC(p,s)` — never FLOAT                                                    |
| "TIMESTAMP vs TIMESTAMPTZ?"  | TIMESTAMPTZ stores UTC, converts on retrieval. Use it for production.           |
| "VARCHAR vs TEXT?"           | Same performance in PostgreSQL. TEXT is simpler.                                |
| "What is NULL?"              | Absence of value — not zero, not empty string. NULL = NULL is NULL, not TRUE.   |
| "How do you check for NULL?" | `IS NULL` / `IS NOT NULL` — never `= NULL`                                      |
| "What's CAST()?"             | Converts a value to a different type. `CAST(x AS type)` or `x::type`            |
| "INT vs BIGINT?"             | INT = 4 bytes (~2B max). BIGINT = 8 bytes. Use BIGINT for IDs in large systems. |
