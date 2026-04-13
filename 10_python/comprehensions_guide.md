# Python Comprehensions Guide

## What Are Comprehensions?

**One-line syntax for building lists, dicts, and sets from iterables.**

Instead of:
```python
results = []
for item in items:
    results.append(transform(item))
```

Write:
```python
results = [transform(item) for item in items]
```

---

## List Comprehensions

### Basic Pattern

```python
from typing import List

# Old way: loop + append
numbers: List[int] = []
for i in range(5):
    numbers.append(i * 2)
# Result: [0, 2, 4, 6, 8]

# Comprehension way
numbers: List[int] = [i * 2 for i in range(5)]
# Result: [0, 2, 4, 6, 8]
```

**Template:** `[expression for item in iterable]`

---

### With Type Hints

```python
from typing import List

# Input data
names: List[str] = ["alice", "bob", "carol"]

# Transform each item
uppercase: List[str] = [name.upper() for name in names]
# Result: ["ALICE", "BOB", "CAROL"]

lengths: List[int] = [len(name) for name in names]
# Result: [5, 3, 5]

# Using f-strings
greetings: List[str] = [f"Hello, {name}!" for name in names]
# Result: ["Hello, alice!", "Hello, bob!", "Hello, carol!"]
```

---

### Adding Conditions (Filtering)

```python
from typing import List

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Only even numbers
evens: List[int] = [n for n in numbers if n % 2 == 0]
# Result: [2, 4, 6, 8, 10]

# Only numbers > 5
big: List[int] = [n for n in numbers if n > 5]
# Result: [6, 7, 8, 9, 10]

# Squared evens
even_squares: List[int] = [n**2 for n in numbers if n % 2 == 0]
# Result: [4, 16, 36, 64, 100]
```

**Template:** `[expression for item in iterable if condition]`

---

### Multiple Conditions

```python
from typing import List

# Both conditions must be true (AND)
results: List[int] = [n for n in range(20) if n % 2 == 0 if n > 10]
# Result: [12, 14, 16, 18]

# Same as:
results: List[int] = [n for n in range(20) if n % 2 == 0 and n > 10]
```

---

### If/Else in Comprehension (Ternary)

```python
from typing import List

numbers: List[int] = [1, 2, 3, 4, 5]

# Label even/odd
labels: List[str] = ["even" if n % 2 == 0 else "odd" for n in numbers]
# Result: ["odd", "even", "odd", "even", "odd"]

# Double evens, keep odds
transformed: List[int] = [n * 2 if n % 2 == 0 else n for n in numbers]
# Result: [1, 4, 3, 8, 5]
```

**Template:** `[value_if_true if condition else value_if_false for item in iterable]`

**Note the order:** condition comes AFTER the expression when using if/else

---

### Real-World Examples (Action Builder)

```python
from typing import List

# Clean phone numbers
phones: List[str] = ["(555) 123-4567", "555.987.6543", "555-111-2222"]
cleaned: List[str] = [p.replace("(", "").replace(")", "").replace("-", "").replace(".", "").replace(" ", "") 
                      for p in phones]
# Result: ["5551234567", "5559876543", "5551112222"]

# Title case names
names: List[str] = ["ALICE SMITH", "bob jones", "CaRoL DaViS"]
proper: List[str] = [name.title() for name in names]
# Result: ["Alice Smith", "Bob Jones", "Carol Davis"]

# Extract first names
full_names: List[str] = ["Alice Smith", "Bob Jones", "Carol Davis"]
first_names: List[str] = [name.split()[0] for name in full_names]
# Result: ["Alice", "Bob", "Carol"]

# Filter out empty strings
values: List[str] = ["Alice", "", "Bob", "", "Carol"]
non_empty: List[str] = [v for v in values if v]
# Result: ["Alice", "Bob", "Carol"]

# Strip whitespace from all
dirty: List[str] = ["  Alice  ", " Bob", "Carol   "]
clean: List[str] = [s.strip() for s in dirty]
# Result: ["Alice", "Bob", "Carol"]
```

---

### Nested Comprehensions (2D Lists)

```python
from typing import List

# Create a grid
grid: List[List[int]] = [[i + j for j in range(3)] for i in range(3)]
# Result: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Flatten a 2D list
matrix: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat: List[int] = [num for row in matrix for num in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Read as: "for each row in matrix, for each num in that row, take num"
```

---

## Dictionary Comprehensions

### Basic Pattern

```python
from typing import Dict

# Old way: loop + dict assignment
squares: Dict[int, int] = {}
for i in range(5):
    squares[i] = i ** 2
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Comprehension way
squares: Dict[int, int] = {i: i**2 for i in range(5)}
# Result: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Template:** `{key_expr: value_expr for item in iterable}`

---

### From Two Lists (zip)

```python
from typing import Dict, List

names: List[str] = ["Alice", "Bob", "Carol"]
ages: List[int] = [25, 30, 28]

# Create dict from two lists
people: Dict[str, int] = {name: age for name, age in zip(names, ages)}
# Result: {"Alice": 25, "Bob": 30, "Carol": 28}
```

---

### With Filtering

```python
from typing import Dict

# Only even squares
even_squares: Dict[int, int] = {i: i**2 for i in range(10) if i % 2 == 0}
# Result: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Filter by value
scores: Dict[str, int] = {"Alice": 85, "Bob": 92, "Carol": 78, "David": 95}
high_scores: Dict[str, int] = {name: score for name, score in scores.items() if score >= 90}
# Result: {"Bob": 92, "David": 95}
```

---

### Transforming Keys or Values

```python
from typing import Dict

# Lowercase all keys
data: Dict[str, int] = {"ALICE": 25, "BOB": 30, "CAROL": 28}
normalized: Dict[str, int] = {k.lower(): v for k, v in data.items()}
# Result: {"alice": 25, "bob": 30, "carol": 28}

# Double all values
prices: Dict[str, float] = {"apple": 1.50, "banana": 0.75, "orange": 2.00}
doubled: Dict[str, float] = {k: v * 2 for k, v in prices.items()}
# Result: {"apple": 3.0, "banana": 1.5, "orange": 4.0}

# Transform both
inventory: Dict[str, int] = {"APPLE": 10, "BANANA": 5, "ORANGE": 8}
cleaned: Dict[str, str] = {k.title(): f"{v} units" for k, v in inventory.items()}
# Result: {"Apple": "10 units", "Banana": "5 units", "Orange": "8 units"}
```

---

### Swapping Keys and Values

```python
from typing import Dict

original: Dict[str, int] = {"Alice": 101, "Bob": 102, "Carol": 103}
swapped: Dict[int, str] = {v: k for k, v in original.items()}
# Result: {101: "Alice", 102: "Bob", 103: "Carol"}
```

**Warning:** Only works if values are unique (can be dict keys)

---

### Real-World Examples (Action Builder)

```python
from typing import Dict, List

# Phone lookup by name
contacts: List[tuple] = [("Alice", "555-1234"), ("Bob", "555-5678"), ("Carol", "555-9012")]
phone_book: Dict[str, str] = {name: phone for name, phone in contacts}
# Result: {"Alice": "555-1234", "Bob": "555-5678", "Carol": "555-9012"}

# Count occurrences
cities: List[str] = ["LA", "NYC", "LA", "SF", "LA", "NYC"]
counts: Dict[str, int] = {city: cities.count(city) for city in set(cities)}
# Result: {"LA": 3, "NYC": 2, "SF": 1}

# Create ID mapping
members: List[str] = ["Alice", "Bob", "Carol"]
member_ids: Dict[str, int] = {name: i + 1 for i, name in enumerate(members)}
# Result: {"Alice": 1, "Bob": 2, "Carol": 3}

# Filter out None values
data: Dict[str, str | None] = {"name": "Alice", "email": None, "phone": "555-1234", "fax": None}
clean: Dict[str, str] = {k: v for k, v in data.items() if v is not None}
# Result: {"name": "Alice", "phone": "555-1234"}
```

---

## Set Comprehensions

```python
from typing import Set

# Unique squares
squares: Set[int] = {i**2 for i in range(-5, 6)}
# Result: {0, 1, 4, 9, 16, 25}  (negatives create same squares)

# Unique lengths
words: list[str] = ["apple", "banana", "cat", "dog", "elephant"]
lengths: Set[int] = {len(word) for word in words}
# Result: {3, 5, 6, 8}
```

**Template:** `{expression for item in iterable}`

**Note:** Use `{}` like dict, but only expression (no key:value)

---

## When NOT to Use Comprehensions

### Too Complex (Use Loop Instead)

```python
# BAD: Hard to read
result = [process(item) if condition1(item) else fallback(item) 
          for item in data if filter1(item) and filter2(item)]

# GOOD: Clear loop
result = []
for item in data:
    if filter1(item) and filter2(item):
        if condition1(item):
            result.append(process(item))
        else:
            result.append(fallback(item))
```

**Rule of thumb:** If you need to explain it, use a loop.

---

### Side Effects (Use Loop Instead)

```python
# BAD: Comprehension for side effects
_ = [print(item) for item in items]  # Don't do this!

# GOOD: Loop for side effects
for item in items:
    print(item)
```

**Comprehensions are for transforming data, not performing actions.**

---

### Multiple Statements (Use Loop)

```python
# BAD: Can't do this in comprehension
# Need to both validate AND transform

# GOOD: Loop handles multiple steps
results = []
for item in items:
    if validate(item):
        cleaned = clean(item)
        transformed = transform(cleaned)
        results.append(transformed)
```

---

## Common Patterns

### Pattern 1: Clean and Filter

```python
from typing import List

# Remove empty, strip whitespace, title case
names: List[str] = ["  alice  ", "", "  BOB", "carol  ", ""]
cleaned: List[str] = [name.strip().title() for name in names if name.strip()]
# Result: ["Alice", "Bob", "Carol"]
```

---

### Pattern 2: Extract from Nested Data

```python
from typing import List, Dict

# Extract all emails from list of dicts
people: List[Dict[str, str]] = [
    {"name": "Alice", "email": "alice@ex.com"},
    {"name": "Bob", "email": "bob@ex.com"},
    {"name": "Carol", "email": "carol@ex.com"}
]

emails: List[str] = [person["email"] for person in people]
# Result: ["alice@ex.com", "bob@ex.com", "carol@ex.com"]

# With filtering
valid_emails: List[str] = [p["email"] for p in people if "@" in p["email"]]
```

---

### Pattern 3: Create Lookup Dict from List of Dicts

```python
from typing import Dict, List

contacts: List[Dict[str, str | int]] = [
    {"id": 101, "name": "Alice", "phone": "555-1234"},
    {"id": 102, "name": "Bob", "phone": "555-5678"},
]

# Dict by ID
by_id: Dict[int, Dict[str, str | int]] = {c["id"]: c for c in contacts}
# Result: {101: {...}, 102: {...}}

# Phone lookup by name
phones: Dict[str, str] = {c["name"]: c["phone"] for c in contacts}
# Result: {"Alice": "555-1234", "Bob": "555-5678"}
```

---

### Pattern 4: Conditional Transformation

```python
from typing import List

# Normalize: strip if string, keep as-is if not
values: List[str | int] = ["  text  ", 123, "  more  ", 456]
normalized: List[str | int] = [v.strip() if isinstance(v, str) else v for v in values]
# Result: ["text", 123, "more", 456]
```

---

## Comparison: Loop vs Comprehension

```python
from typing import List

numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Task: Get squares of even numbers

# LOOP VERSION
result: List[int] = []
for n in numbers:
    if n % 2 == 0:
        result.append(n ** 2)

# COMPREHENSION VERSION
result: List[int] = [n**2 for n in numbers if n % 2 == 0]

# Both give: [4, 16, 36, 64, 100]
```

**Comprehension is:**
- ✓ More concise
- ✓ Often faster
- ✓ More "Pythonic"

**But loop is better when:**
- Logic is complex
- Need multiple statements
- Performing side effects
- Debugging (easier to step through)

---

## Type Hint Patterns

```python
from typing import List, Dict, Set, Optional

# List comprehension
numbers: List[int] = [i for i in range(10)]

# Dict comprehension
mapping: Dict[str, int] = {str(i): i for i in range(5)}

# Set comprehension
unique: Set[int] = {i % 3 for i in range(10)}

# Optional values
nullable: List[Optional[str]] = [s if s else None for s in ["a", "", "b"]]

# Mixed types (union)
mixed: List[str | int] = [i if i % 2 == 0 else str(i) for i in range(5)]
```

---

## Practice Exercises

Try writing these as comprehensions:

```python
from typing import List, Dict

# 1. Square all numbers from 1 to 10
# Answer: [i**2 for i in range(1, 11)]

# 2. Get all words longer than 3 characters
words: List[str] = ["cat", "elephant", "dog", "bird"]
# Answer: [w for w in words if len(w) > 3]

# 3. Create dict: word -> length
# Answer: {w: len(w) for w in words}

# 4. Uppercase only words starting with 'c'
# Answer: [w.upper() if w[0].lower() == 'c' else w for w in words]

# 5. Flatten nested list
nested: List[List[int]] = [[1, 2], [3, 4], [5, 6]]
# Answer: [num for sublist in nested for num in sublist]
```

---

## Common Mistakes

### 1. Wrong condition placement

```python
# WRONG: Filter after transformation
[n**2 for n in numbers if n**2 > 50]  # Squares, then filters squares

# RIGHT: Filter then transform
[n**2 for n in numbers if n > 7]  # Filters numbers, then squares
```

---

### 2. Forgetting .items() for dicts

```python
data: Dict[str, int] = {"a": 1, "b": 2}

# WRONG: Only iterates keys
[k for k in data]  # ["a", "b"]

# RIGHT: Iterate key-value pairs
[v for k, v in data.items()]  # [1, 2]
```

---

### 3. Mutating during iteration

```python
# WRONG: Don't modify original during comprehension
items: List[int] = [1, 2, 3]
_ = [items.append(i * 2) for i in items]  # Dangerous!

# RIGHT: Create new list
doubled: List[int] = [i * 2 for i in items]
```

---

## Summary

**List comprehension:**
```python
[expression for item in iterable if condition]
```

**Dict comprehension:**
```python
{key_expr: value_expr for item in iterable if condition}
```

**Set comprehension:**
```python
{expression for item in iterable if condition}
```

**Key points:**
- Use for simple transformations
- Add `if` to filter
- Use loops for complex logic
- Always add type hints
- Readable > clever
