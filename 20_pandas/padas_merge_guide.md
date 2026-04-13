# Pandas Merge Guide

## What is Merge?

**Merge combines two DataFrames based on matching keys.**

It’s the same concept as:

- **Google Sheets:** VLOOKUP, INDEX/MATCH
- **SQL:** JOIN (LEFT, INNER, RIGHT, OUTER)
- **Pandas:** `.merge()`

-----

## Basic Syntax

```python
result = df1.merge(df2, on='key_column', how='left')
```

**Parameters:**

- `df2` - DataFrame to merge into df1
- `on='key_column'` - Column name to match on (must exist in both DataFrames)
- `how='left'` - Type of join (left, right, inner, outer)

-----

## Complete Example: Basic Merge

### Setup

```python
import pandas as pd

# DataFrame 1: People
people = pd.DataFrame({
    'email': ['alice@ex.com', 'bob@ex.com', 'carol@ex.com'],
    'name': ['Alice', 'Bob', 'Carol'],
    'age': [25, 30, 35]
})

# DataFrame 2: Member Status
status = pd.DataFrame({
    'email': ['alice@ex.com', 'bob@ex.com', 'dave@ex.com'],
    'is_member': [True, True, False],
    'join_date': ['2024-01-15', '2024-02-20', '2024-03-10']
})
```

### Before Merge

**people:**

```
   email            name   age
0  alice@ex.com     Alice  25
1  bob@ex.com       Bob    30
2  carol@ex.com     Carol  35
```

**status:**

```
   email            is_member  join_date
0  alice@ex.com     True       2024-01-15
1  bob@ex.com       True       2024-02-20
2  dave@ex.com      False      2024-03-10
```

### After Merge (LEFT JOIN)

```python
result = people.merge(status, on='email', how='left')
```

**result:**

```
   email            name   age  is_member  join_date
0  alice@ex.com     Alice  25   True       2024-01-15
1  bob@ex.com       Bob    30   True       2024-02-20
2  carol@ex.com     Carol  35   NaN        NaN
```

**What happened:**

- Alice and Bob matched → got their member status
- Carol didn’t match → NaN for is_member and join_date
- Dave (in status but not people) → not included in result

-----

## The Four Join Types

### LEFT JOIN (`how='left'`)

**Keep all rows from LEFT DataFrame, add matching data from RIGHT**

```python
people.merge(status, on='email', how='left')
```

**Result: 3 rows** (all people)

- Alice: matched → has member status
- Bob: matched → has member status
- Carol: no match → NaN for status columns

**Use when:** You want to keep all your primary data and add supplementary info where available

**Real example:** All contacts (left) + member status (right) → keep all contacts, add status where it exists

-----

### INNER JOIN (`how='inner'`)

**Keep ONLY rows that match in BOTH DataFrames**

```python
people.merge(status, on='email', how='inner')
```

**Result: 2 rows** (only matches)

```
   email            name   age  is_member  join_date
0  alice@ex.com     Alice  25   True       2024-01-15
1  bob@ex.com       Bob    30   True       2024-02-20
```

Carol excluded (no match in status)
Dave excluded (no match in people)

**Use when:** You only want records that exist in both datasets

**Real example:** Contacts who are also in member database → exclude non-members and orphaned member records

-----

### RIGHT JOIN (`how='right'`)

**Keep all rows from RIGHT DataFrame, add matching data from LEFT**

```python
people.merge(status, on='email', how='right')
```

**Result: 3 rows** (all status records)

```
   email            name   age  is_member  join_date
0  alice@ex.com     Alice  25   True       2024-01-15
1  bob@ex.com       Bob    30   True       2024-02-20
2  dave@ex.com      NaN    NaN  False      2024-03-10
```

**Use when:** Rarely. Usually just swap the DataFrames and use left join instead.

-----

### OUTER JOIN (`how='outer'`)

**Keep ALL rows from BOTH DataFrames**

```python
people.merge(status, on='email', how='outer')
```

**Result: 4 rows** (everyone from both)

```
   email            name   age  is_member  join_date
0  alice@ex.com     Alice  25   True       2024-01-15
1  bob@ex.com       Bob    30   True       2024-02-20
2  carol@ex.com     Carol  35   NaN        NaN
3  dave@ex.com      NaN    NaN  False      2024-03-10
```

**Use when:** You want to see everything and identify what’s missing on each side

**Real example:** Reconcile two systems → see which records exist in one but not the other

-----

## Different Column Names

**What if the join key has different names in each DataFrame?**

### Setup

```python
contacts = pd.DataFrame({
    'email': ['alice@ex.com', 'bob@ex.com'],
    'phone': ['555-1234', '555-5678']
})

members = pd.DataFrame({
    'email_address': ['alice@ex.com', 'carol@ex.com'],
    'member_id': [101, 102]
})
```

### Solution: Use `left_on` and `right_on`

```python
result = contacts.merge(
    members,
    left_on='email',
    right_on='email_address',
    how='left'
)
```

**Result:**

```
   email            phone     email_address    member_id
0  alice@ex.com     555-1234  alice@ex.com     101.0
1  bob@ex.com       555-5678  NaN              NaN
```

**Note:** Both email columns are kept. You’ll usually want to drop one:

```python
result = contacts.merge(
    members,
    left_on='email',
    right_on='email_address',
    how='left'
).drop(columns=['email_address'])
```

-----

## Multiple Join Keys

**Match on MORE than one column**

### Setup

```python
sales_2024 = pd.DataFrame({
    'region': ['West', 'West', 'East'],
    'product': ['A', 'B', 'A'],
    'sales': [100, 150, 200]
})

targets = pd.DataFrame({
    'region': ['West', 'West', 'East'],
    'product': ['A', 'B', 'A'],
    'target': [120, 140, 180]
})
```

### Merge on Both Columns

```python
result = sales_2024.merge(
    targets,
    on=['region', 'product'],
    how='left'
)
```

**Result:**

```
   region  product  sales  target
0  West    A        100    120
1  West    B        150    140
2  East    A        200    180
```

**Matches when BOTH region AND product match.**

-----

## The Indicator Column

**Track which DataFrame each row came from**

### Why Use It

Find records that:

- Matched in both DataFrames
- Only exist in left DataFrame
- Only exist in right DataFrame

### Syntax

```python
result = people.merge(
    status,
    on='email',
    how='outer',
    indicator=True
)
```

**Result includes `_merge` column:**

```
   email            name   age  is_member  join_date   _merge
0  alice@ex.com     Alice  25   True       2024-01-15  both
1  bob@ex.com       Bob    30   True       2024-02-20  both
2  carol@ex.com     Carol  35   NaN        NaN         left_only
3  dave@ex.com      NaN    NaN  False      2024-03-10  right_only
```

**_merge values:**

- `both` - Record exists in both DataFrames (matched)
- `left_only` - Record only in left DataFrame (no match found)
- `right_only` - Record only in right DataFrame (orphaned)

### Use Cases

**Find unmatched records:**

```python
# Contacts with no member status
no_status = result[result['_merge'] == 'left_only']

# Member records with no contact info
orphaned = result[result['_merge'] == 'right_only']

# Count match rate
result['_merge'].value_counts()
```

**Custom indicator name:**

```python
result = people.merge(status, on='email', how='outer', indicator='source')
# Creates 'source' column instead of '_merge'
```

-----

## Common Problems & Solutions

### Problem 1: Duplicate Column Names

**What happens:**

```python
df1 = pd.DataFrame({
    'email': ['alice@ex.com'],
    'name': ['Alice Smith']
})

df2 = pd.DataFrame({
    'email': ['alice@ex.com'],
    'name': ['Alice S.']  # Different name value!
})

result = df1.merge(df2, on='email')
```

**Result:**

```
   email            name_x        name_y
0  alice@ex.com     Alice Smith   Alice S.
```

**Pandas adds `_x` and `_y` suffixes automatically.**

**Solutions:**

**Option 1: Drop duplicate column before merge**

```python
df2 = df2.drop(columns=['name'])
result = df1.merge(df2, on='email')
```

**Option 2: Rename before merge**

```python
df2 = df2.rename(columns={'name': 'alt_name'})
result = df1.merge(df2, on='email')
```

**Option 3: Custom suffixes**

```python
result = df1.merge(df2, on='email', suffixes=('_contact', '_member'))
# Creates: name_contact, name_member
```

-----

### Problem 2: Row Explosion (Cartesian Product)

**What causes it:**
Duplicate keys in BOTH DataFrames multiply rows.

**Example:**

```python
df1 = pd.DataFrame({
    'id': [1, 1, 2],  # Two rows with id=1
    'value_a': ['x', 'y', 'z']
})

df2 = pd.DataFrame({
    'id': [1, 1, 2],  # Two rows with id=1
    'value_b': ['m', 'n', 'p']
})

result = df1.merge(df2, on='id')
```

**Result: 5 rows** (not 3!)

```
   id  value_a  value_b
0  1   x        m       ← df1 row 1 × df2 row 1
1  1   x        n       ← df1 row 1 × df2 row 2
2  1   y        m       ← df1 row 2 × df2 row 1
3  1   y        n       ← df1 row 2 × df2 row 2
4  2   z        p       ← df2 row 3 × df2 row 3
```

**2 rows with id=1 in df1 × 2 rows with id=1 in df2 = 4 rows**

**Prevention:**

**Check for duplicates BEFORE merging:**

```python
# Check left DataFrame
df1['id'].value_counts()

# Check right DataFrame
df2['id'].value_counts()

# Find duplicates
df1[df1.duplicated(subset='id', keep=False)]
```

**If duplicates exist, decide:**

- Remove duplicates: `df1.drop_duplicates(subset='id')`
- Keep first: `df1.drop_duplicates(subset='id', keep='first')`
- Group and aggregate first: `df1.groupby('id').first().reset_index()`

**Always check row count after merge:**

```python
print(f"Before: {len(df1)} rows")
result = df1.merge(df2, on='id', how='left')
print(f"After: {len(result)} rows")

# If After > Before, you have row explosion
```

-----

### Problem 3: Key Formatting Mismatch

**What causes it:**
Keys look the same but don’t match due to:

- Extra spaces: `'alice@ex.com'` vs `' alice@ex.com '`
- Different case: `'Alice'` vs `'alice'`
- Different formats: `'555-1234'` vs `'5551234'`

**Example:**

```python
df1 = pd.DataFrame({
    'email': ['alice@ex.com', 'bob@ex.com']
})

df2 = pd.DataFrame({
    'email': [' Alice@Ex.com ', ' Bob@Ex.com ']  # Spaces + caps!
})

result = df1.merge(df2, on='email', how='left', indicator=True)
```

**Result: No matches!**

```
   email            _merge
0  alice@ex.com     left_only
1  bob@ex.com       left_only
```

**Solution: Clean keys before merging**

```python
# Strip whitespace and lowercase
df1['email'] = df1['email'].str.strip().str.lower()
df2['email'] = df2['email'].str.strip().str.lower()

# Now merge
result = df1.merge(df2, on='email', how='left')
# ✓ Matches work!
```

**Standard cleaning pattern:**

```python
def clean_key(series):
    """Standardize key column for merging"""
    return series.str.strip().str.lower()

df1['email'] = clean_key(df1['email'])
df2['email'] = clean_key(df2['email'])
```

-----

## Action Builder Workflow Example

**Real scenario: Merge contact list with member database**

### Step 1: Load Data

```python
import pandas as pd

# Load contact list from local organizing drive
contacts = pd.read_csv('local_123_contacts.csv')
# 5,000 rows: name, email, phone, address

# Load member status from national database
members = pd.read_csv('member_status_export.csv')
# 3,000 rows: email, member_id, join_date, dues_current
```

### Step 2: Inspect Join Keys

```python
# Check for duplicates in contacts
print("Contacts with duplicate emails:")
print(contacts['email'].value_counts().head())

# Check for duplicates in members
print("Members with duplicate emails:")
print(members['email'].value_counts().head())

# Check for null emails
print(f"Contacts missing email: {contacts['email'].isna().sum()}")
print(f"Members missing email: {members['email'].isna().sum()}")
```

### Step 3: Clean Join Keys

```python
# Standardize email format
contacts['email'] = contacts['email'].str.strip().str.lower()
members['email'] = members['email'].str.strip().str.lower()

# Remove rows with null emails (can't match on null)
contacts = contacts.dropna(subset=['email'])
members = members.dropna(subset=['email'])
```

### Step 4: Merge with Indicator

```python
# Left join: keep all contacts, add member info where available
result = contacts.merge(
    members[['email', 'member_id', 'join_date', 'dues_current']],
    on='email',
    how='left',
    indicator=True
)

print(f"Original contacts: {len(contacts)}")
print(f"After merge: {len(result)}")
print("\nMatch breakdown:")
print(result['_merge'].value_counts())
```

**Output:**

```
Original contacts: 4,987
After merge: 4,987

Match breakdown:
left_only    2,145  (contacts not in member database)
both         2,842  (contacts who are members)
```

### Step 5: Analyze Results

```python
# Who are the non-members? (recruitment targets)
non_members = result[result['_merge'] == 'left_only']
print(f"Non-members to recruit: {len(non_members)}")

# Who are current members with lapsed dues?
lapsed = result[
    (result['_merge'] == 'both') & 
    (result['dues_current'] == False)
]
print(f"Members with lapsed dues: {len(lapsed)}")

# Export for outreach
non_members[['name', 'email', 'phone']].to_csv('recruitment_list.csv', index=False)
lapsed[['name', 'email', 'member_id']].to_csv('dues_followup_list.csv', index=False)
```

### Step 6: Data Quality Check

```python
# Check for row explosion (shouldn't happen with clean email keys)
if len(result) > len(contacts):
    print("WARNING: Row explosion detected!")
    print("Checking for duplicate emails...")
    
    # Find duplicates
    dupes = result[result.duplicated(subset='email', keep=False)]
    print(f"Found {len(dupes)} duplicate rows")
    print(dupes[['name', 'email', 'member_id']].head(10))
```

-----

## Merge Checklist

Before every merge, run through this:

### 1. Inspect Keys

```python
# Check for duplicates
df1['key'].value_counts()
df2['key'].value_counts()

# Check for nulls
df1['key'].isna().sum()
df2['key'].isna().sum()
```

### 2. Clean Keys

```python
# Strip whitespace and standardize case
df1['key'] = df1['key'].str.strip().str.lower()
df2['key'] = df2['key'].str.strip().str.lower()
```

### 3. Merge with Indicator

```python
result = df1.merge(df2, on='key', how='left', indicator=True)
```

### 4. Verify Results

```python
# Check row count
print(f"Before: {len(df1)}, After: {len(result)}")

# Check match rate
print(result['_merge'].value_counts())

# Spot check unmatched
print(result[result['_merge'] == 'left_only'].head())
```

### 5. Handle Issues

- Row explosion? → Remove duplicates or aggregate first
- Low match rate? → Check key formatting
- Unexpected columns? → Drop or rename duplicates

-----

## Quick Reference

### Basic Merge

```python
result = df1.merge(df2, on='key', how='left')
```

### Different Column Names

```python
result = df1.merge(df2, left_on='col1', right_on='col2', how='left')
```

### Multiple Keys

```python
result = df1.merge(df2, on=['key1', 'key2'], how='left')
```

### With Indicator

```python
result = df1.merge(df2, on='key', how='left', indicator=True)
```

### Check Match Rate

```python
result['_merge'].value_counts()
```

### Find Unmatched

```python
unmatched = result[result['_merge'] == 'left_only']
```

-----

## Join Type Decision Tree

**Do you want to keep all rows from the left DataFrame?**

- Yes → `how='left'`
- No → Continue

**Do you only want rows that match in BOTH DataFrames?**

- Yes → `how='inner'`
- No → Continue

**Do you want ALL rows from BOTH DataFrames?**

- Yes → `how='outer'`
- No → `how='right'` (or swap DataFrames and use left)

**90% of the time, you want `how='left'`**

-----

## Common Patterns

### Add Lookup Column

```python
# Add quality scores to contacts
contacts = contacts.merge(
    quality_scores[['phone', 'quality_rating']],
    on='phone',
    how='left'
)
```

### Filter to Matches Only

```python
# Only contacts who are also members
matched = contacts.merge(members, on='email', how='inner')
```

### Find Missing Records

```python
# Contacts not in member database
result = contacts.merge(members, on='email', how='left', indicator=True)
missing = result[result['_merge'] == 'left_only']
```

### Enrich with Multiple Sources

```python
# Add member status, then add phone scores
contacts = contacts.merge(members, on='email', how='left')
contacts = contacts.merge(phone_scores, on='phone', how='left')
```

-----

## Tips & Best Practices

1. **Always use `indicator=True` during development** - remove it in production
1. **Check row count before and after** - catch explosions early
1. **Clean keys before merging** - strip, lowercase, standardize format
1. **Use left join by default** - most common use case
1. **Select specific columns from right DataFrame** - avoid duplicate column names
1. **Test on small sample first** - verify logic before running on full dataset
1. **Save intermediate results** - easier to debug multi-step merges

-----

## When NOT to Use Merge

**Use `.join()` instead when:**

- Joining on index (not a column)
- Quick index-based joins

**Use `pd.concat()` instead when:**

- Stacking DataFrames vertically (adding rows)
- Combining DataFrames with same columns
- No key-based matching needed

**Use `.map()` instead when:**

- Simple 1:1 lookup (like VLOOKUP for single value)
- Creating a new column from dictionary

-----

## Related Operations

### Concat (Stacking Rows)

```python
# Combine multiple DataFrames vertically
combined = pd.concat([df1, df2, df3], ignore_index=True)
```

### Join (Index-based)

```python
# Join on index instead of column
result = df1.join(df2, how='left')
```

### Map (Simple Lookup)

```python
# Add single value from dictionary
status_map = {'A': 'Active', 'I': 'Inactive'}
df['status_name'] = df['status_code'].map(status_map)
```