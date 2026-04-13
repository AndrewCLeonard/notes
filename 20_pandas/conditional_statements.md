# Pandas Conditional Assignment — the IF formula equivalent

## Single condition (simple IF)

`df.loc[condition, 'column'] = value`

## Multiple conditions (nested IF) — apply in reverse priority, last wins

```python
df['column'] = None # reset
df.loc[condition_2, 'column'] = value # lower priority
df.loc[condition_1, 'column'] = value # higher priority, overwrites where both match
```

## Key rule: `loc[]` is surgical — only touches matching rows
