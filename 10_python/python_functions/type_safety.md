# Python Type Safety Guide (mypy)

## Why Type Hints?

**Type hints catch bugs before runtime.**

Without type hints:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers("5", "10")  # Returns "510" (string concat) - BUG!
```

With type hints:

```python
def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers("5", "10")  # mypy error: Expected int, got str
```

**Benefits:**

- Catch type errors before running code
- Better IDE autocomplete
- Self-documenting code
- Easier refactoring
- Helps collaborators understand your code

---

## Setting Up Type Checking

### VS Code Type Checking (Built-in)

**Workspace Settings (Recommended for projects):**

Add to `.vscode/settings.json`:

```json
{
  "python.analysis.typeCheckingMode": "basic"
}
```

**User Settings (Global):**

- `Ctrl+,` (or `Cmd+,` on Mac)
- Search "type checking mode"
- Select "basic" or "strict"

**Type checking modes:**

- `off` - No type checking
- `basic` - Catches obvious errors (recommended for learning)
- `strict` - Maximum type safety (for production code)

---

### mypy (External Type Checker)

**Install:**

```bash
pip install mypy
```

**Run on your code:**

```bash
mypy your_script.py
mypy .  # Check all Python files in directory
```

**VS Code mypy integration:**

1. Install Python extension
2. Settings → Python › Linting: Mypy Enabled → ✓
3. Type errors show as you type

**Difference: VS Code Pylance vs mypy**

- **Pylance** (VS Code built-in): Fast, real-time, good for learning
- **mypy**: More thorough, industry standard, catches edge cases
- **Recommendation**: Use both (Pylance while coding, mypy before commit)

---

## Basic Type Annotations

### Variables

```python
# Explicit type annotation
name: str = "Alice"
age: int = 25
height: float = 5.7
is_member: bool = True

# Type is inferred (still checked by mypy)
name = "Alice"  # mypy knows this is str
age = 25  # mypy knows this is int
```

**Best practice:** Annotate when type isn't obvious from value

```python
# Don't need annotation (obvious)
count = 0

# Do need annotation (not obvious)
result: list[str] = get_data()
```

---

### Functions

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def process_data(data: list[str]) -> None:
    # Function returns nothing (None)
    for item in data:
        print(item)
```

**Template:**

```python
def function_name(param: Type) -> ReturnType:
    ...
```

---

## Common Types

### Built-in Types

```python
# Primitives
number: int = 42
price: float = 19.99
name: str = "Alice"
is_valid: bool = True

# None type
result: None = None

# Any type (avoid when possible)
from typing import Any
unknown: Any = "could be anything"
```

---

### Collection Types

```python
from typing import List, Dict, Set, Tuple

# List (homogeneous - all same type)
names: list[str] = ["Alice", "Bob", "Carol"]
numbers: list[int] = [1, 2, 3, 4, 5]

# Dict
scores: dict[str, int] = {"Alice": 85, "Bob": 92}
config: dict[str, str] = {"host": "localhost", "port": "8080"}

# Set
unique_ids: set[int] = {1, 2, 3, 4, 5}

# Tuple (fixed length, can be heterogeneous)
coordinate: tuple[int, int] = (10, 20)
person: tuple[str, int, bool] = ("Alice", 25, True)

# Tuple (variable length, homogeneous)
numbers: tuple[int, ...] = (1, 2, 3, 4, 5)
```

**Python 3.9+:** Use lowercase `list`, `dict`, `set`, `tuple`
**Python 3.8 and earlier:** Import from `typing`: `List`, `Dict`, `Set`, `Tuple`

---

### Optional (Value or None)

```python
from typing import Optional

# Can be str or None
name: Optional[str] = None
name = "Alice"  # OK
name = None  # OK

# Modern syntax (Python 3.10+)
name: str | None = None

# Function that might return None
def find_user(user_id: int) -> Optional[dict]:
    if user_id in database:
        return database[user_id]
    return None
```

**Use when:** Value might not exist (database lookups, optional parameters)

---

### Union Types (Multiple Possible Types)

```python
from typing import Union

# Can be int or str
id_value: Union[int, str] = 123
id_value = "ABC123"  # Both OK

# Modern syntax (Python 3.10+)
id_value: int | str = 123

# Function accepting multiple types
def format_id(value: int | str) -> str:
    return str(value).zfill(10)
```

---

## Action Builder Patterns

### Pattern 1: Contact Data

```python
from typing import Optional

class Contact:
    def __init__(
        self,
        name: str,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        address: Optional[str] = None
    ) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

# Usage
contact = Contact("Alice", phone="555-1234")
```

---

### Pattern 2: Data Cleaning Functions

```python
def clean_phone(phone: str | None) -> str | None:
    """Remove formatting from phone number."""
    if phone is None:
        return None

    # Remove all non-digits
    cleaned = "".join(c for c in phone if c.isdigit())

    # Return None if no digits found
    return cleaned if cleaned else None

# Type-safe usage
phone: str | None = "(555) 123-4567"
result: str | None = clean_phone(phone)
```

---

### Pattern 3: List Processing

```python
from typing import List

def filter_valid_emails(emails: list[str]) -> list[str]:
    """Return only emails containing '@'."""
    return [email for email in emails if "@" in email]

def extract_names(records: list[dict[str, str]]) -> list[str]:
    """Extract name field from list of dicts."""
    return [record["name"] for record in records]

# Usage
emails: list[str] = ["alice@ex.com", "invalid", "bob@ex.com"]
valid: list[str] = filter_valid_emails(emails)
```

---

### Pattern 4: Dict Transformations

```python
def create_lookup(
    records: list[dict[str, str | int]]
) -> dict[int, dict[str, str | int]]:
    """Create lookup dict by ID."""
    return {record["id"]: record for record in records}

# Usage
contacts: list[dict[str, str | int]] = [
    {"id": 1, "name": "Alice", "phone": "555-1234"},
    {"id": 2, "name": "Bob", "phone": "555-5678"},
]

lookup: dict[int, dict[str, str | int]] = create_lookup(contacts)
```

---

## TypedDict for Structured Dicts

```python
from typing import TypedDict

# Define structure of dict
class ContactDict(TypedDict):
    id: int
    name: str
    phone: str
    email: str | None

# Type-safe dict
contact: ContactDict = {
    "id": 1,
    "name": "Alice",
    "phone": "555-1234",
    "email": None
}

# mypy catches missing/extra keys
bad_contact: ContactDict = {
    "id": 1,
    "name": "Alice"
    # Error: Missing required key "phone"
}

# Function using TypedDict
def format_contact(contact: ContactDict) -> str:
    return f"{contact['name']}: {contact['phone']}"
```

**Use when:** Working with structured dicts (like JSON data, API responses)

---

## Generic Types

### Lists of Specific Types

```python
# List of strings
names: list[str] = ["Alice", "Bob", "Carol"]

# List of ints
numbers: list[int] = [1, 2, 3, 4, 5]

# List of dicts
contacts: list[dict[str, str]] = [
    {"name": "Alice", "phone": "555-1234"},
    {"name": "Bob", "phone": "555-5678"},
]

# Nested lists
grid: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

---

### Dict with Specific Key/Value Types

```python
# String keys, int values
scores: dict[str, int] = {"Alice": 85, "Bob": 92}

# Int keys, string values
id_to_name: dict[int, str] = {1: "Alice", 2: "Bob"}

# String keys, union values
config: dict[str, str | int | bool] = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
}
```

---

## Function Signatures

### Basic Functions

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str, excited: bool = False) -> str:
    greeting = f"Hello, {name}"
    return greeting + "!" if excited else greeting

def process_list(items: list[str]) -> None:
    for item in items:
        print(item)
```

---

### Functions Returning Multiple Types

```python
def divide(a: int, b: int) -> float | None:
    if b == 0:
        return None
    return a / b

# Usage requires None check
result: float | None = divide(10, 2)
if result is not None:
    print(f"Result: {result}")
```

---

### Functions with Callbacks

```python
from typing import Callable

def apply_to_all(
    items: list[int],
    func: Callable[[int], int]
) -> list[int]:
    return [func(item) for item in items]

# Usage
def double(x: int) -> int:
    return x * 2

numbers: list[int] = [1, 2, 3, 4, 5]
doubled: list[int] = apply_to_all(numbers, double)
```

**Callable[[InputType], ReturnType]** = function signature

---

## Type Checking Patterns

### Pattern 1: Type Guards

```python
from typing import Union

def process_value(value: int | str) -> str:
    # Type guard narrows type
    if isinstance(value, int):
        # mypy knows value is int here
        return str(value * 2)
    else:
        # mypy knows value is str here
        return value.upper()
```

---

### Pattern 2: Asserting Non-None

```python
def get_name(user_id: int) -> str:
    name: str | None = database.get(user_id)

    # Assert not None (use carefully!)
    assert name is not None, f"User {user_id} not found"

    # mypy knows name is str here (not None)
    return name.upper()
```

**Warning:** Only use `assert` when you're certain value exists

---

### Pattern 3: Narrowing with if/else

```python
from typing import Optional

def format_phone(phone: str | None) -> str:
    if phone is None:
        return "No phone"

    # mypy knows phone is str here (not None)
    return phone.replace("-", "")
```

---

## Common mypy Errors

### Error 1: Type Mismatch

```python
def add(a: int, b: int) -> int:
    return a + b

result = add("5", "10")
# Error: Argument 1 has incompatible type "str"; expected "int"
```

**Fix:** Use correct type

```python
result = add(5, 10)
```

---

### Error 2: Missing Return

```python
def get_name(user_id: int) -> str:
    if user_id in database:
        return database[user_id]
    # Error: Missing return statement
```

**Fix:** Handle all paths

```python
def get_name(user_id: int) -> str:
    if user_id in database:
        return database[user_id]
    return "Unknown"
```

---

### Error 3: Incompatible Return Type

```python
def get_score() -> int:
    return "95"  # Error: Incompatible return type
```

**Fix:** Return correct type

```python
def get_score() -> int:
    return 95
```

---

### Error 4: None Not Compatible

```python
def find_user(user_id: int) -> dict:
    if user_id not in database:
        return None  # Error: Return type is "dict", not "None"
    return database[user_id]
```

**Fix:** Use Optional

```python
def find_user(user_id: int) -> dict | None:
    if user_id not in database:
        return None
    return database[user_id]
```

---

## Advanced Patterns

### Pattern 1: Type Aliases

```python
from typing import TypeAlias

# Create readable type alias
ContactRecord: TypeAlias = dict[str, str | int | None]
ContactList: TypeAlias = list[ContactRecord]

# Use in functions
def process_contacts(contacts: ContactList) -> None:
    for contact in contacts:
        print(contact["name"])
```

---

### Pattern 2: Literal Types

```python
from typing import Literal

def set_status(status: Literal["active", "inactive", "pending"]) -> None:
    print(f"Status set to: {status}")

# OK
set_status("active")

# Error: Argument must be "active", "inactive", or "pending"
set_status("cancelled")
```

---

### Pattern 3: Protocol (Structural Typing)

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

def render(item: Drawable) -> None:
    item.draw()

# Any class with draw() method works
class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing square")

render(Circle())  # OK
render(Square())  # OK
```

---

## Pandas Type Hints

```python
import pandas as pd
from pandas import DataFrame, Series

def clean_names(df: DataFrame) -> DataFrame:
    """Strip and title case name column."""
    df["Name"] = df["Name"].str.strip().str.title()
    return df

def get_high_scores(df: DataFrame) -> Series:
    """Return scores above 90."""
    return df[df["Score"] > 90]["Score"]

# Usage
df: DataFrame = pd.read_csv("data.csv")
cleaned: DataFrame = clean_names(df)
high: Series = get_high_scores(cleaned)
```

**Note:** Pandas types are less strict than pure Python types

---

## Configuration

### mypy.ini File

Create `mypy.ini` in project root:

```ini
[mypy]
# Strictness
strict = True
warn_return_any = True
warn_unused_configs = True

# Imports
ignore_missing_imports = True

# Per-module config
[mypy-pandas.*]
ignore_missing_imports = True

[mypy-rapidfuzz.*]
ignore_missing_imports = True
```

---

### pyproject.toml (Modern)

```toml
[tool.mypy]
strict = true
warn_return_any = true
warn_unused_configs = true
ignore_missing_imports = true

[[tool.mypy.overrides]]
module = ["pandas.*", "rapidfuzz.*"]
ignore_missing_imports = true
```

---

## Best Practices

### 1. Start with Function Signatures

```python
# Annotate this first
def process_data(data: list[str]) -> dict[str, int]:
    ...
```

**Why:** Function boundaries are most important

---

### 2. Don't Over-Annotate

```python
# BAD: Obvious from context
x: int = 5
name: str = "Alice"

# GOOD: Type inferred
x = 5
name = "Alice"

# GOOD: Not obvious, annotate
result: list[str] = get_data()
```

---

### 3. Use Optional for Nullable Values

```python
# GOOD
def find_user(user_id: int) -> dict | None:
    ...

# BAD (implicit None not caught by mypy)
def find_user(user_id: int) -> dict:
    return None  # Runtime error later!
```

---

### 4. Prefer Specific Types Over Any

```python
# BAD
from typing import Any
data: Any = get_data()

# GOOD
data: list[dict[str, str]] = get_data()
```

**Exception:** Third-party libraries without type stubs

---

### 5. Use TypedDict for Structured Dicts

```python
from typing import TypedDict

# GOOD: Structure defined
class UserDict(TypedDict):
    name: str
    age: int
    email: str | None

# BAD: Unstructured
user: dict = {"name": "Alice", "age": 25}
```

---

## Gradual Typing

**You don't have to type everything at once.**

### Phase 1: Critical Functions

```python
# Type your main functions first
def process_contacts(data: list[dict]) -> list[dict]:
    ...
```

### Phase 2: Public API

```python
# Type all functions others will call
def clean_phone(phone: str | None) -> str | None:
    ...
```

### Phase 3: Internal Functions

```python
# Type helper functions
def _strip_whitespace(text: str) -> str:
    ...
```

### Phase 4: Variables

```python
# Add annotations where helpful
results: list[str] = []
```

---

## Quick Reference

### Common Types

```python
# Primitives
x: int = 5
y: float = 3.14
s: str = "text"
b: bool = True

# Collections
items: list[str] = ["a", "b"]
mapping: dict[str, int] = {"a": 1}
unique: set[int] = {1, 2, 3}
coord: tuple[int, int] = (10, 20)

# Optional
value: str | None = None

# Union
id: int | str = "ABC"

# Any (avoid)
from typing import Any
unknown: Any = something
```

---

### Function Annotations

```python
# Basic
def func(x: int) -> str:
    return str(x)

# Optional parameter
def greet(name: str, excited: bool = False) -> str:
    ...

# Returns None
def log(message: str) -> None:
    print(message)

# Multiple return types
def divide(a: int, b: int) -> float | None:
    ...
```

---

## Summary

**Type hints help you:**

- ✓ Catch bugs before runtime
- ✓ Get better IDE support
- ✓ Document code automatically
- ✓ Refactor with confidence

**Start small:**

1. Annotate function signatures
2. Add types to critical variables
3. Use Optional for nullable values
4. Run mypy regularly
5. Fix errors gradually

**Key tools:**

- `mypy` - Type checker
- `typing` module - Type annotations
- IDE integration - Real-time checking

**Remember:**

- Types are optional in Python
- Start gradually
- Focus on function boundaries
- Don't over-annotate obvious types
- Use mypy to verify
