# The LEFT JOIN / WHERE Trap

Created: 2026-04-07

---

## The Problem

When you LEFT JOIN a table and then filter on that table's columns in WHERE, you silently convert the LEFT JOIN to an INNER JOIN — dropping all rows where the join found no match.

```sql
-- LOOKS like a LEFT JOIN, BEHAVES like an INNER JOIN
SELECT *
FROM entities e
LEFT JOIN taggable_logbook tl ON tl.taggable_id = e.id
LEFT JOIN tags t ON t.id = tl.tag_id
LEFT JOIN tag_categories tc ON tc.id = t.tag_category_id
WHERE tc.id = 195  -- ← kills the LEFT JOIN
```

Any entity with no matching tag gets NULL for `tc.id`.
`NULL = 195` evaluates to false (not NULL, not true — false).
That row gets dropped — same as INNER JOIN.

---

## The Fix

Move the condition from WHERE into the JOIN's ON clause:

```sql
-- TRUE LEFT JOIN — entities with no tag are included (NULL for tag columns)
SELECT *
FROM entities e
LEFT JOIN taggable_logbook tl ON tl.taggable_id = e.id
LEFT JOIN tags t ON t.id = tl.tag_id
LEFT JOIN tag_categories tc ON tc.id = t.tag_category_id
    AND tc.id = 195  -- ← condition is now part of the join, not the filter
```

Now entities with no matching tag category still appear — `tc.id` is NULL for them, but the row isn't dropped.

---

## The Mental Test

Ask yourself before every JOIN:

> _"Do I want rows where this join finds nothing?"_

| Answer                       | Join Type  | Condition goes in         |
| ---------------------------- | ---------- | ------------------------- |
| Yes — include unmatched rows | LEFT JOIN  | ON clause                 |
| No — only matched rows       | INNER JOIN | ON or WHERE (same result) |

---

## Real-World Example From Production Queries

```sql
-- WRONG: tl.deleted_at IS NULL in WHERE drops unmatched entities
FROM entities e
LEFT JOIN taggable_logbook tl ON tl.taggable_id = e.id
WHERE tl.deleted_at IS NULL

-- CORRECT: filter stays with the optional table
FROM entities e
LEFT JOIN taggable_logbook tl ON tl.taggable_id = e.id
    AND tl.deleted_at IS NULL
```

---

## Key Principle

**LEFT JOIN conditions on the optional table → ON clause.**
**Everything else → WHERE.**

The WHERE clause filters the _result set_.
The ON clause defines _how tables relate_.

---

## Generic Examples

### The Tables

#### customers

| id  | name  |
| --- | ----- |
| 1   | Alice |
| 2   | Bob   |
| 3   | Carol |

#### orders

| id  | customer_id | amount |
| --- | ----------- | ------ |
| 1   | 1           | 50     |
| 2   | 1           | 75     |
| 3   | 2           | 100    |

Carol (id=3) has no orders.

---

### Example 1 — The Trap

Goal: Show all customers, including those with no orders.

```sql
-- WRONG: Carol is dropped because o.amount is NULL
SELECT c.name, o.amount
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.amount > 25
```

Result:

| name  | amount |
| ----- | ------ |
| Alice | 50     |
| Alice | 75     |
| Bob   | 100    |

Carol is gone. `NULL > 25` is false.

---

### Example 2 — The Fix

```sql
-- CORRECT: Carol is included with NULL for amount
SELECT c.name, o.amount
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
    AND o.amount > 25
```

Result:

| name  | amount |
| ----- | ------ |
| Alice | 50     |
| Alice | 75     |
| Bob   | 100    |
| Carol | NULL   |

Carol appears — the join simply found no qualifying row for her.

---

### Example 3 — When INNER JOIN is correct

Goal: Show only customers who have placed orders over $25. You don't want Carol.

```sql
-- CORRECT: INNER JOIN, condition in WHERE is fine
SELECT c.name, o.amount
FROM customers c
JOIN orders o ON o.customer_id = c.id
WHERE o.amount > 25
```

Result:

| name  | amount |
| ----- | ------ |
| Alice | 50     |
| Alice | 75     |
| Bob   | 100    |

This is intentional — no LEFT JOIN needed because you don't want unmatched rows.

---

### Example 4 — Chained LEFT JOINs

The trap compounds when you chain multiple LEFT JOINs. Filtering on any table in the chain in WHERE drops rows.

order_items

| id  | order_id | product |
| --- | -------- | ------- |
| 1   | 1        | Widget  |
| 2   | 2        | Gadget  |

```sql
-- WRONG: filters on order_items in WHERE
-- drops customers with no orders AND orders with no items
SELECT c.name, o.amount, oi.product
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
LEFT JOIN order_items oi ON oi.order_id = o.id
WHERE oi.product = 'Widget'  -- drops Bob, Carol, and Alice's Gadget order
```

```sql
-- CORRECT: condition in ON clause
SELECT c.name, o.amount, oi.product
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
LEFT JOIN order_items oi ON oi.order_id = o.id
    AND oi.product = 'Widget'
```

---

## Anki Cards

See: `left_join_where_trap_anki.md`
