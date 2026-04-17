# Google Sheets Formulas → Pandas

## The Mental Model Shift

In Sheets, every cell has its own formula that runs independently.
In Pandas, one statement acts on an entire column at once.

---

## COUNTIF

Sheets:

```text
=COUNTIF(A:A, A2)
```

Pandas:

```python
df['count'] = df['col'].map(df['col'].value_counts())
```

How it works:

- `value_counts()` returns a Series where index = value, value = count
- `map()` looks up each row's value in that Series and returns the count
- Think of `value_counts()` as building the lookup table, `map()` as doing the lookup

Count with a condition (COUNTIF with criteria):

```python
# Sheets: =COUNTIF(B:B, "Active")
df['col'].value_counts()['Active']

# Count per group, add back as column
df['active_count'] = df['col'].map(df[df['col'] == 'Active']['col'].value_counts())
```

---

## VLOOKUP / XLOOKUP

Sheets:

```text
=VLOOKUP(A2, Sheet2!A:B, 2, FALSE)
=XLOOKUP(A2, Sheet2!A:A, Sheet2!B:B)
```

Pandas — two approaches depending on the situation:

### Option 1: `.map()` — simple 1:1 lookup, adding one column

```python
# Build lookup Series from reference table
lookup = reference_df.set_index('key_col')['value_col']

# Apply to main df
df['new_col'] = df['lookup_key'].map(lookup)
```

Example:

```python
# Add department name from a reference table
dept_lookup = dept_df.set_index('dept_id')['dept_name']
df['dept_name'] = df['dept_id'].map(dept_lookup)
```

### Option 2: `.merge()` — adding multiple columns at once

```python
df = df.merge(
    reference_df[['key_col', 'col_1', 'col_2']],
    on='key_col',
    how='left'
)
```

### When to use which

| Situation                                   | Use                                 |
| ------------------------------------------- | ----------------------------------- |
| Adding one column from a reference table    | `.map()`                            |
| Adding multiple columns at once             | `.merge()`                          |
| Key column has same name in both DataFrames | `.merge(on='key')`                  |
| Key column has different names              | `.merge(left_on='a', right_on='b')` |

---

## IF

Sheets:

```text
=IF(A2="Active", "Yes", "No")
```

Pandas — `loc[]` for assignment, `np.where()` for inline:

### `loc[]` — assign to a column conditionally (most common)

```python
# Single condition
df.loc[df['status'] == 'Active', 'is_active'] = 'Yes'
df.loc[df['status'] != 'Active', 'is_active'] = 'No'
```

### `np.where()` — inline IF, returns values directly

```python
import numpy as np

df['is_active'] = np.where(df['status'] == 'Active', 'Yes', 'No')
```

This is the closest 1:1 equivalent to `=IF()`.

### Nested IF — apply `loc[]` in reverse priority order

```python
# Sheets: =IF(A2="A", "High", IF(A2="B", "Medium", "Low"))

df['priority'] = 'Low'                                      # default
df.loc[df['grade'] == 'B', 'priority'] = 'Medium'          # overrides default
df.loc[df['grade'] == 'A', 'priority'] = 'High'            # overrides medium
```

Last condition wins — apply least important first, most important last.

---

## COUNTA

Sheets:

```text
=COUNTA(A:A)
```

Pandas:

```python
# Count non-null values in a column
df['col'].count()

# Count all rows including nulls
len(df)

# Count nulls specifically
df['col'].isna().sum()

# Count non-nulls specifically
df['col'].notna().sum()
```

---

## SUMIF

Sheets:

```text
=SUMIF(A:A, "West", B:B)
```

Pandas:

```python
# Sum of col_b where col_a == "West"
df[df['region'] == 'West']['sales'].sum()

# Sum by group (all groups at once)
df.groupby('region')['sales'].sum()

# Add group sum back as a column
df['region_total'] = df['region'].map(df.groupby('region')['sales'].sum())
```

---

## LET

Sheets:

```text
=LET(name, value, formula_using_name)
```

Pandas equivalent — just use a variable:

```python
# Sheets LET assigns a name to avoid repeating a calculation
# In Python, variables do this naturally

condition = df['status'] == 'Active'   # name the condition once
df.loc[condition, 'flag'] = True       # reuse it
count = condition.sum()                # reuse again
```

---

## ISNUMBER / ISBLANK / ISTEXT

Sheets:

```text
=ISBLANK(A2)
=ISNUMBER(A2)
```

Pandas:

```python
df['col'].isna()       # equivalent to ISBLANK
df['col'].notna()      # equivalent to NOT(ISBLANK)
df['col'].dtype        # check column type
pd.to_numeric(df['col'], errors='coerce').notna()  # equivalent to ISNUMBER
```

---

## CONCATENATE / TEXTJOIN

Sheets:

```text
=A2&" "&B2
=TEXTJOIN(" ", TRUE, A2, B2)
```

Pandas:

```python
# Simple concatenation
df['full_name'] = df['first_name'] + ' ' + df['last_name']

# With NaN handling (TEXTJOIN equivalent — skips blanks)
df['full_name'] = df['first_name'].str.cat(df['last_name'], sep=' ', na_rep='').str.strip()
```

---

## TRIM / LOWER / UPPER / PROPER

Sheets:

```text
=TRIM(A2)
=LOWER(A2)
=UPPER(A2)
=PROPER(A2)
```

Pandas:

```python
df['col'].str.strip()    # TRIM
df['col'].str.lower()    # LOWER
df['col'].str.upper()    # UPPER
df['col'].str.title()    # PROPER
```

Chain them:

```python
df['col'].str.strip().str.lower()
```

---

## LEFT / RIGHT / MID

Sheets:

```text
=LEFT(A2, 3)
=RIGHT(A2, 4)
=MID(A2, 2, 5)
```

Pandas:

```python
df['col'].str[:3]      # LEFT 3 characters
df['col'].str[-4:]     # RIGHT 4 characters
df['col'].str[1:6]     # MID — start at index 1, take 5 characters
```

---

## SUBSTITUTE / REPLACE

Sheets:

```text
=SUBSTITUTE(A2, "old", "new")
```

Pandas:

```python
# Literal replacement
df['col'].str.replace('old', 'new')

# Regex replacement
df['col'].str.replace(r'\s+', ' ', regex=True)
```

---

## Quick Reference

| Sheets                    | Pandas                                       |
| ------------------------- | -------------------------------------------- |
| `COUNTIF(A:A, A2)`        | `df['col'].map(df['col'].value_counts())`    |
| `VLOOKUP(A2, ref, 2, 0)`  | `df['key'].map(ref.set_index('key')['val'])` |
| `XLOOKUP` (multiple cols) | `df.merge(ref, on='key', how='left')`        |
| `IF(cond, a, b)`          | `np.where(condition, a, b)`                  |
| `IF` for assignment       | `df.loc[condition, 'col'] = value`           |
| `NESTED IF`               | `loc[]` in reverse priority order            |
| `COUNTA(A:A)`             | `df['col'].count()`                          |
| `SUMIF(A:A, x, B:B)`      | `df[df['col']==x]['val'].sum()`              |
| `ISBLANK(A2)`             | `df['col'].isna()`                           |
| `TRIM(A2)`                | `df['col'].str.strip()`                      |
| `LOWER(A2)`               | `df['col'].str.lower()`                      |
| `A2&" "&B2`               | `df['a'] + ' ' + df['b']`                    |
| `LEFT(A2, 3)`             | `df['col'].str[:3]`                          |
