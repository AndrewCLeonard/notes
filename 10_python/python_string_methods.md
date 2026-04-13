# Python String Methods — Quick Reference

_For data cleaning, list formatting, and text manipulation_
_Created: 2026-04-04_

---

## Methods Used in the ID Formatter

### `.strip()`

Removes leading and trailing whitespace (spaces, newlines, tabs).

```python
"  hello  ".strip()        # "hello"
"  hello  ".lstrip()       # "hello  " (left only)
"  hello  ".rstrip()       # "  hello" (right only)
"\n12345\n".strip()        # "12345"
```

**When you'll use it:** Any time you paste raw text that may have leading/trailing whitespace. Almost always pair with `.split()`.

---

### `.split()`

Splits a string into a list on a delimiter. Defaults to any whitespace (spaces, newlines, tabs).

```python
"12345\n67890\n11111".split()          # ['12345', '67890', '11111']
"12345,67890,11111".split(',')         # ['12345', '67890', '11111']
"first last".split()                   # ['first', 'last']
"a, b, c".split(', ')                 # ['a', 'b', 'c']
```

**When you'll use it:** Parsing raw exports, splitting full names, converting delimited strings to lists.

---

### `', '.join()`

Joins a list of strings into a single string with a delimiter between each item.

```python
', '.join(['12345', '67890', '11111'])   # "12345, 67890, 11111"
' | '.join(['Smith', 'John', '897'])     # "Smith | John | 897"
'\n'.join(['line1', 'line2', 'line3'])   # multiline string
```

**Note:** All items in the list must be strings. Use `str(x)` if mixing types.

```python
ids = [12345, 67890, 11111]  # integers
', '.join(str(i) for i in ids)  # "12345, 67890, 11111"
```

**When you'll use it:** Formatting ID lists for SQL `IN` clauses, building composite keys, joining name parts.

---

## Related Methods Worth Knowing

### `.replace()`

Replaces all occurrences of a substring with another.

```python
"Smith, John".replace(', ', ' ')        # "Smith John"
"  extra   spaces  ".replace('  ', ' ') # "  extra spaces " (only replaces pairs)
"N/A".replace('N/A', '')                # ""
```

**When you'll use it:** Light text cleaning before processing. Note: not regex-based — exact string match only.

---

### `.upper()` / `.lower()` / `.title()`

Case conversion.

```python
"john smith".title()    # "John Smith"
"JOHN".lower()          # "john"
"john".upper()          # "JOHN"
```

**When you'll use it:** Normalizing names before fuzzy matching or comparison.

---

### `.startswith()` / `.endswith()`

Returns `True`/`False` — useful for filtering.

```python
"2026-04-04".startswith("2026")    # True
"report.csv".endswith(".csv")      # True

# Can check multiple options with a tuple
"file.xlsx".endswith(('.xlsx', '.csv', '.xls'))  # True
```

**When you'll use it:** Filtering file lists, checking date prefixes, validating formats.

---

### `.strip()` with a character argument

Strips specific characters, not just whitespace.

```python
"***hello***".strip('*')     # "hello"
"/path/to/dir/".strip('/')   # "path/to/dir"
```

---

### `in` operator

Checks if a substring exists in a string. Not a method but essential.

```python
"smith" in "john smith"      # True
"@" in "user@email.com"      # True
"xyz" in "john smith"        # False
```

**When you'll use it:** Quick membership checks before more expensive operations.

---

## The ID List Formatter — Full Pattern

```python
# Paste raw newline-separated IDs between the triple quotes
ids = """12345
67890
11111
22222"""

# Strip whitespace, split on newlines, join with comma
formatted = ', '.join(ids.strip().split('\n'))
print(formatted)
# Output: 12345, 67890, 11111, 22222

# Ready to paste into SQL:
# WHERE e.id IN (12345, 67890, 11111, 22222)
```

---

## Chaining Methods

Python string methods can be chained — each returns a string (or list) that the next method operates on.

```python
"  John Smith  ".strip().lower().replace(' ', '_')
# "john_smith"

"12345\n67890\n".strip().split('\n')
# ['12345', '67890']
```

Read left to right — each method transforms the output of the previous one.

---

## Quick Reference Table

| Method                  | Input  | Output  | Use Case           |
| ----------------------- | ------ | ------- | ------------------ |
| `.strip()`              | String | String  | Remove whitespace  |
| `.split(delim)`         | String | List    | String → list      |
| `delim.join(list)`      | List   | String  | List → string      |
| `.replace(old, new)`    | String | String  | Text substitution  |
| `.lower()` / `.upper()` | String | String  | Case normalization |
| `.title()`              | String | String  | Name formatting    |
| `.startswith(x)`        | String | Boolean | Prefix check       |
| `.endswith(x)`          | String | Boolean | Suffix check       |
| `x in string`           | String | Boolean | Substring check    |
