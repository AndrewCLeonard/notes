# FILTER vs CASE for Pivoting (Conditional Aggregation)

## The Problem

Convert long format to wide format:

**Input (long):**

```
owner_id  phone
1         555-1234
1         555-5678
2         555-1111
```

**Output (wide):**

```
owner_id  phone_1      phone_2      phone_3
1         555-1234     555-5678     NULL
2         555-1111     NULL         NULL
```

## Solution 1: FILTER (PostgreSQL)

```sql
WITH numbered AS (
  SELECT 
    owner_id, 
    phone,
    ROW_NUMBER() OVER (PARTITION BY owner_id ORDER BY phone) as rn
  FROM contacts
)
SELECT 
  owner_id,
  MAX(phone) FILTER (WHERE rn = 1) as phone_1,
  MAX(phone) FILTER (WHERE rn = 2) as phone_2,
  MAX(phone) FILTER (WHERE rn = 3) as phone_3
FROM numbered
GROUP BY owner_id;
```

## Solution 2: CASE (Works Everywhere)

```sql
WITH numbered AS (
  SELECT 
    owner_id, 
    phone,
    ROW_NUMBER() OVER (PARTITION BY owner_id ORDER BY phone) as rn
  FROM contacts
)
SELECT 
  owner_id,
  MAX(CASE WHEN rn = 1 THEN phone END) as phone_1,
  MAX(CASE WHEN rn = 2 THEN phone END) as phone_2,
  MAX(CASE WHEN rn = 3 THEN phone END) as phone_3
FROM numbered
GROUP BY owner_id;
```

## FILTER vs CASE

|Approach  |Syntax                                |Database Support|
|----------|--------------------------------------|----------------|
|**FILTER**|`MAX(phone) FILTER (WHERE rn = 1)`    |PostgreSQL only |
|**CASE**  |`MAX(CASE WHEN rn = 1 THEN phone END)`|All databases   |

**They produce identical results.** FILTER is cleaner syntax for PostgreSQL.

**For Action Builder (PostgreSQL): Use FILTER**

## Why MAX()?

After GROUP BY, you have multiple rows per owner that need to collapse:

```
owner_id=1, rn=1: phone='555-1234', NULL, NULL
owner_id=1, rn=2: NULL, phone='555-5678', NULL
owner_id=1, rn=3: NULL, NULL, phone='555-9999'
```

MAX() picks the non-NULL value from each column:

```
owner_id=1: '555-1234', '555-5678', '555-9999'
```

## Adding HAVING (Filter Groups)

**Use HAVING to filter groups AFTER aggregation:**

```sql
SELECT 
  owner_id,
  MAX(phone) FILTER (WHERE rn = 1) as phone_1,
  MAX(phone) FILTER (WHERE rn = 2) as phone_2,
  COUNT(*) as total_phones
FROM numbered
GROUP BY owner_id
HAVING COUNT(*) >= 2;  -- Only owners with 2+ phones
```

## WHERE vs HAVING

|Clause    |Filters                        |Execution Step   |
|----------|-------------------------------|-----------------|
|**WHERE** |Individual rows BEFORE grouping|Step 3 (FJWGHSOL)|
|**HAVING**|Groups AFTER aggregation       |Step 5 (FJWGHSOL)|

**Example:**

```sql
WHERE phone IS NOT NULL     -- Filters rows with no phone
HAVING COUNT(*) >= 2        -- Filters owners with <2 phones
```

## Complete Example with All Pieces

```sql
WITH numbered AS (
  SELECT 
    owner_id, 
    phone,
    ROW_NUMBER() OVER (PARTITION BY owner_id ORDER BY phone) as rn
  FROM contacts
  WHERE phone IS NOT NULL  -- WHERE: filter rows
)
SELECT 
  owner_id,
  MAX(phone) FILTER (WHERE rn = 1) as phone_1,
  MAX(phone) FILTER (WHERE rn = 2) as phone_2,
  MAX(phone) FILTER (WHERE rn = 3) as phone_3,
  COUNT(*) as total_phones
FROM numbered
GROUP BY owner_id
HAVING COUNT(*) >= 2;  -- HAVING: filter groups

-- Execution order: FROM → WHERE → window functions → GROUP BY → HAVING → SELECT
```