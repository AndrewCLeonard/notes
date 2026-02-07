# Understanding Type Checking

## Setting Up Type Checking in VS Code

Add this to Workspace settings, best for a repo:

```json
{
  "python.analysis.typeCheckingMode": "basic"
}
```

Or change in User settings `ctrl + ,`, "type checking mode"

## Type Hints vs. Type Coersion

### Definitions

### Type Hints

[Type Hints Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

#### Example

```python
def replace_accents(s: str) -> str:
```

#### Explanation

| code       | purpose          | effect |
| ---------- | ---------------- | ------ |
| `(s: str)` | type hint        |        |
| `-> str`   | return type hint |        |
|            |                  |        |
