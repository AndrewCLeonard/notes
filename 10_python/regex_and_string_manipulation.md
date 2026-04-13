# Regex and String Manipulation: Python, Pandas, and Google Sheets Equivalents

## Imports — Always Required

```python
import re          # Python's built-in regex module — needed for re.sub(), re.search(), re.match()
import pandas as pd  # .str accessor methods handle regex without importing re directly
```

**Gotcha:** Pandas `.str` methods use regex internally — you do NOT need `import re` for those.
You only need `import re` when calling `re.sub()`, `re.search()`, `re.match()`, or `re.findall()` directly on plain Python strings.

---

## Raw Strings — Always Use for Regex Patterns

```python
# Wrong — Python tries to interpret \s, \d as escape sequences
pattern = "\s+"

# Right — raw string, backslashes are literal
pattern = r"\s+"
```

**Rule:** Always prefix regex patterns with `r""`. No exceptions.

---

## Google Sheets → Python/Pandas Equivalents

### `REGEXREPLACE` → `str.replace()` or `re.sub()`

Sheets:

```excel
=REGEXREPLACE(A2, "\s+", "")
```

Pandas (on a Series — most common in data work):

```python
df["col"].str.replace(r"\s+", "", regex=True)
```

Plain Python (on a single string):

```python
import re
re.sub(r"\s+", "", my_string)
```

**Gotcha:** `.replace()` on a plain Python string does LITERAL replacement, not regex:

```python
# This looks for the literal characters \s+, not whitespace
"hello world".replace(r"\s+", "")  # does nothing useful

# This correctly removes whitespace
re.sub(r"\s+", "", "hello world")   # "helloworld"
```

---

### `REGEXMATCH` → `str.contains()` or `re.search()`

Sheets:

```excel
=REGEXMATCH(A2, "^\d{3}-\d{4}$")
```

Pandas (returns boolean Series — use for filtering):

```python
df["col"].str.contains(r"^\d{3}-\d{4}$", regex=True)

# Filter rows where column matches pattern
df[df["col"].str.contains(r"^\d{3}-\d{4}$", regex=True, na=False)]
```

**Gotcha:** `str.contains()` returns `NaN` for null values by default, which breaks boolean filtering.
Always pass `na=False` to treat nulls as non-matching:

```python
df["col"].str.contains(r"pattern", regex=True, na=False)
```

Plain Python (returns a match object or None):

```python
import re
if re.search(r"^\d{3}-\d{4}$", my_string):
    print("match found")
```

---

### `REGEXEXTRACT` → `str.extract()` or `re.search().group()`

Sheets:

```excel
=REGEXEXTRACT(A2, "Shift\s(.*)")
```

Pandas (returns a DataFrame with one column per capture group):

```python
df["shift_cleaned"] = df["shift"].str.extract(r"Shift\s(.*)")
```

**Gotcha:** `str.extract()` only returns the FIRST match. If you need all matches, use `str.extractall()`.

**Gotcha:** `str.extract()` requires a capture group — the part in parentheses `()`. Without it you get an error:

```python
# Wrong — no capture group
df["col"].str.extract(r"Shift\s.*")

# Right — capture group added
df["col"].str.extract(r"Shift\s(.*)")
```

Plain Python:

```python
import re
match = re.search(r"Shift\s(.*)", my_string)
if match:
    print(match.group(1))  # group(1) is the first capture group
```

---

## Removing Characters — Common Patterns

```python
# Remove all non-alpha characters (letters only)
df["col"].str.replace(r"[^a-z]", "", regex=True)  # lowercase first

# Remove all non-alphanumeric characters
df["col"].str.replace(r"[^a-z0-9]", "", regex=True)

# Remove whitespace only
df["col"].str.replace(r"\s+", "", regex=True)
# OR for simple single spaces on a plain string:
my_string.replace(" ", "")  # no regex needed for literal replacement

# Remove trailing .0 from floats converted to strings
df["col"].str.replace(r"\.0$", "", regex=True)

# Keep only letters, hyphens, and apostrophes (name cleaning)
df["col"].str.replace(r"[^a-z'-]", "", regex=True)
```

**Gotcha:** `-` inside a character class `[]` must be at the start or end to be treated as a literal hyphen.
Otherwise it defines a range (e.g. `[a-z]`):

```python
r"[^a-z'-]"   # safe — hyphen at the end
r"[^-a-z']"   # safe — hyphen at the start
r"[^a-z'-]"   # safe — what you're already doing
```

---

## Pandas `.str` Methods Quick Reference

| Method                                    | What it does                                | Regex?   |
| ----------------------------------------- | ------------------------------------------- | -------- |
| `str.replace(pat, repl, regex=True)`      | Replace pattern with string                 | Yes      |
| `str.contains(pat, regex=True, na=False)` | Returns boolean — does it match?            | Yes      |
| `str.extract(r"(pattern)")`               | Extract first match, requires capture group | Yes      |
| `str.extractall(r"(pattern)")`            | Extract all matches                         | Yes      |
| `str.strip()`                             | Remove leading/trailing whitespace          | No       |
| `str.lower()` / `str.upper()`             | Change case                                 | No       |
| `str.split(pat)`                          | Split string into list                      | Optional |
| `str.cat(other, sep=" ")`                 | Concatenate two Series                      | No       |

**Gotcha:** Every `.str` method call requires the `.str` accessor — even mid-chain:

```python
# Wrong
df["col"].str.strip().lower()

# Right
df["col"].str.strip().str.lower()
```

---

## Plain Python `re` Module Quick Reference

```python
import re

# re.sub() — replace pattern (equivalent to REGEXREPLACE)
re.sub(r"\s+", "", my_string)

# re.search() — find first match anywhere in string (equivalent to REGEXMATCH)
match = re.search(r"\d+", my_string)
if match:
    print(match.group(0))  # group(0) is the full match

# re.match() — match only at the START of string
match = re.match(r"\d+", my_string)

# re.findall() — return list of all matches
matches = re.findall(r"\d+", my_string)

# re.compile() — compile a pattern for reuse (performance optimization)
pattern = re.compile(r"\d+")
pattern.findall(my_string)
```

---

## When to Use What

| Situation                                     | Use                                                |
| --------------------------------------------- | -------------------------------------------------- |
| Cleaning a DataFrame column                   | `df["col"].str.replace()`                          |
| Filtering rows by pattern                     | `df["col"].str.contains(na=False)`                 |
| Extracting a substring into a new column      | `df["col"].str.extract()`                          |
| Working with a single Python string           | `re.sub()`, `re.search()`                          |
| Removing literal characters (no regex needed) | `my_string.replace(" ", "")`                       |
| Cleaning column names (plain list of strings) | `re.sub()` or `.replace()` in a list comprehension |
