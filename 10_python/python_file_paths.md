# File Paths

## Summary

### 3 Options

1. `pathlib` 🏆 Use for all new code whenever possible
2. `os`
3. raw string literals

### Comparison

| method                                                                      | best for                                                                                 | use because                                                                             |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [`pathlib` ](https://docs.python.org/3/library/pathlib.html#concrete-paths) | constructing, joining, normalizing, manipulating filesystem paths.                       | cross-platform, cleaner code, works well with other tools, operator-based joining (`\`) |
| `os`                                                                        | older style, best for env variables, current working directory, but more stringy/verbose | legacy code                                                                             |
| string literals                                                             | writing string literals containing backslashes (Windows paths, regex patterns)           |                                                                                         |

### The Challenge

- switching between systems
- making code readable
- Windows paths commonly use backslashes (`\`)
- Unix-like systems uses forward slashes (`/`)

## `pathlib`

```python
from pathlib import Path

data_dir = Path.home() / "Documents" / "Data"
csv_path = data_dir / "people.csv"
```

## `os` / `os.path`

```python
import os

home = os.path.expanduser("~")
csv_path = os.path.join(home, "Documents", "Data", "people.csv")
```

## Raw String Literals (`r"..."`)

```python
r"C:\Users"
```

### What `r` Does

Prefixing with `r` creates a **raw string literal,** which tells Python **not to treat backslashes as escape characters** (e.g. `\n` or `\t`).

This makWithout the "r," the backslashes get treated as escape characters. This way, you can enter file names the same way in Windows-based or Unix-based systems (Linux, OSX, ZSH on Windows)

## Practical Decision Table

| Need                                    | Use                          | Why                           |
| --------------------------------------- | ---------------------------- | ----------------------------- |
| Build paths from parts                  | `pathlib.Path`               | portable + readable           |
| Join paths dynamically                  | `pathlib.Path`               | avoids slash/backslash issues |
| Pass a path to libraries                | `Path` (or `str(Path)`)      | modern + supported            |
| Read env vars / work with process       | `os`                         | that’s its job                |
| Maintain old code using `os.path`       | `os.path`                    | consistency                   |
| Hardcode a Windows path literal quickly | `r"..."` (or `Path(r"...")`) | avoids escaping               |

## Pattern to Anchor a Script's Location

Use this if you’re running scripts from different places and want it to “just work.”

```python
import pandas as pd
from pathlib import Path

HERE = Path(__file__).resolve().parent
csv_path = HERE / "titanic.csv"

titanic = pd.read_csv(csv_path)
```
