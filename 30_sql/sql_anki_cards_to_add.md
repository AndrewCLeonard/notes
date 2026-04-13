# Anki Cards — LEFT JOIN / WHERE Trap

_Created: 2026-04-07_
_Deck: SQL_

---

**Card 1**
Q: What happens when you filter on a LEFT JOIN'd table's column in the WHERE clause?
A: The LEFT JOIN silently becomes an INNER JOIN. Rows where the join found no match are dropped because the filter column is NULL, and NULL = anything evaluates to false.

---

**Card 2**
Q: Where should conditions on a LEFT JOIN'd table go, and why?
A: In the ON clause. This keeps the LEFT JOIN behavior intact — unmatched rows are still included, with NULL for the joined table's columns. Putting conditions in WHERE drops those rows.

---

**Card 3**
Q: What is the mental test to apply before every JOIN?
A: Ask: "Do I want rows where this join finds nothing?"

- Yes → LEFT JOIN, condition in ON clause
- No → INNER JOIN, condition in ON or WHERE

---

**Card 4**
Q: What does `NULL = 195` evaluate to in PostgreSQL?
A: False (not NULL, not true — false). This is why filtering on a LEFT JOIN'd column in WHERE drops unmatched rows — their value is NULL, which fails any equality check.

---

**Card 5**
Q: What is the difference between the ON clause and the WHERE clause?
A: ON defines how tables relate (join condition). WHERE filters the result set after joining. For LEFT JOINs, conditions on the optional table must go in ON — putting them in WHERE converts the LEFT JOIN to an INNER JOIN.

---

**Card 6**
Q: Fix this query so entities with no matching tag are still returned:

```sql
FROM entities e
LEFT JOIN taggable_logbook tl ON tl.taggable_id = e.id
WHERE tl.deleted_at IS NULL
```

A:

```sql
FROM entities e
LEFT JOIN taggable_logbook tl ON tl.taggable_id = e.id
    AND tl.deleted_at IS NULL
```

Move the condition from WHERE into the ON clause.
