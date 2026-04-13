# Enumerate vs For Loops Guide

## What is enumerate()?

**Built-in function that gives you both index AND item when looping.**

Instead of manual counter:
```python
index = 0
for item in items:
    print(index, item)
    index += 1
```

Use enumerate:
```python
for index, item in enumerate(items):
    print(index, item)
```

---

## Basic Pattern

### Manual Counter (Old Way)

```python
from typing import List

names: List[str] = ["Alice", "Bob", "Carol"]

i: int = 0
for name in names:
    print(f"{i}: {name}")
    i += 1

# Output:
# 0: Alice
# 1: Bob
# 2: Carol
```

**Problems:**
- Have to initialize counter
- Have to increment it
- Easy to forget
- More lines of code

---

### With enumerate() (Better)

```python
from typing import List

names: List[str] = ["Alice", "Bob", "Carol"]

for i, name in enumerate(names):
    print(f"{i}: {name}")

# Output:
# 0: Alice
# 1: Bob
# 2: Carol
```

**Benefits:**
- No manual counter
- Can't forget to increment
- Cleaner, more Pythonic
- Less error-prone

---

## Starting from 1 Instead of 0

```python
from typing import List

names: List[str] = ["Alice", "Bob", "Carol"]

# Start counting at 1
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# Output:
# 1. Alice
# 2. Bob
# 3. Carol
```

**Common use:** Numbered lists for humans (1-indexed)

---

## Type Hints with enumerate()

```python
from typing import List

names: List[str] = ["Alice", "Bob", "Carol"]

# i is int, name is str
for i, name in enumerate(names):
    idx: int = i
    person: str = name
    print(f"{idx}: {person}")
```

**Type of enumerate():**
```python
from typing import List

names: List[str] = ["Alice", "Bob", "Carol"]

# enumerate returns: Iterator[tuple[int, str]]
enumerated = enumerate(names)
# Each iteration gives: (0, "Alice"), (1, "Bob"), (2, "Carol")
```

---

## Real-World Examples

### Example 1: Building Numbered List

```python
from typing import List

items: List[str] = ["Buy milk", "Call dentist", "Fix bug"]

# Manual counter (bad)
counter: int = 1
for item in items:
    print(f"{counter}. {item}")
    counter += 1

# enumerate (good)
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")

# Output:
# 1. Buy milk
# 2. Call dentist
# 3. Fix bug
```

---

### Example 2: Creating Dicts with IDs

```python
from typing import List, Dict

names: List[str] = ["Alice", "Bob", "Carol"]

# Manual counter (bad)
members: Dict[int, str] = {}
member_id: int = 1
for name in names:
    members[member_id] = name
    member_id += 1

# enumerate (good)
members: Dict[int, str] = {i + 1: name for i, name in enumerate(names)}
# Result: {1: "Alice", 2: "Bob", 3: "Carol"}

# Or with start parameter
members: Dict[int, str] = {i: name for i, name in enumerate(names, start=1)}
```

---

### Example 3: Modifying List Items by Index

```python
from typing import List

scores: List[int] = [85, 92, 78, 95, 88]

# Add 5 points to each score
for i, score in enumerate(scores):
    scores[i] = score + 5

print(scores)
# Result: [90, 97, 83, 100, 93]
```

**Note:** Usually better to create new list, but when you NEED to modify in place, enumerate helps.

---

### Example 4: Finding Index of Item

```python
from typing import List, Optional

names: List[str] = ["Alice", "Bob", "Carol", "David"]

# Find index of "Carol"
target: str = "Carol"
found_index: Optional[int] = None

for i, name in enumerate(names):
    if name == target:
        found_index = i
        break

print(found_index)  # 2
```

**Better way:** Use `.index()` method
```python
found_index: int = names.index("Carol")  # 2
```

But enumerate is useful when you need custom logic.

---

### Example 5: Parallel Iteration (enumerate + zip)

```python
from typing import List

names: List[str] = ["Alice", "Bob", "Carol"]
scores: List[int] = [85, 92, 78]

# Numbered results
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name}: {score}")

# Output:
# 1. Alice: 85
# 2. Bob: 92
# 3. Carol: 78
```

---

## Action Builder Use Cases

### Use Case 1: Creating Row IDs

```python
from typing import List, Dict

contacts: List[Dict[str, str]] = [
    {"name": "Alice", "phone": "555-1234"},
    {"name": "Bob", "phone": "555-5678"},
    {"name": "Carol", "phone": "555-9012"},
]

# Add row ID to each contact
for i, contact in enumerate(contacts, start=1):
    contact["row_id"] = i

# Result:
# [{"name": "Alice", "phone": "555-1234", "row_id": 1}, ...]
```

---

### Use Case 2: Progress Tracking

```python
from typing import List

files: List[str] = ["file1.csv", "file2.csv", "file3.csv"]

for i, filename in enumerate(files, start=1):
    print(f"Processing {i}/{len(files)}: {filename}")
    # process_file(filename)

# Output:
# Processing 1/3: file1.csv
# Processing 2/3: file2.csv
# Processing 3/3: file3.csv
```

---

### Use Case 3: Dynamic Column Naming

```python
from typing import List, Dict

phone_numbers: List[str] = ["555-1234", "555-5678", "555-9012"]

# Create dict with phone_1, phone_2, phone_3
contact: Dict[str, str] = {}
for i, phone in enumerate(phone_numbers, start=1):
    contact[f"phone_{i}"] = phone

# Result: {"phone_1": "555-1234", "phone_2": "555-5678", "phone_3": "555-9012"}
```

---

### Use Case 4: Batch Processing with Checkpoints

```python
from typing import List

records: List[Dict] = [...] # 10,000 records

batch_size: int = 100

for i, record in enumerate(records):
    # process_record(record)
    
    # Checkpoint every 100 records
    if (i + 1) % batch_size == 0:
        print(f"Processed {i + 1} records")
        # save_checkpoint()
```

---

## When to Use enumerate()

### ✅ Use enumerate when:

1. **Need both index and item**
   ```python
   for i, item in enumerate(items):
       print(f"Item {i}: {item}")
   ```

2. **Creating numbered output**
   ```python
   for i, task in enumerate(tasks, start=1):
       print(f"{i}. {task}")
   ```

3. **Modifying list in place**
   ```python
   for i, value in enumerate(values):
       values[i] = transform(value)
   ```

4. **Need to track position for logic**
   ```python
   for i, item in enumerate(items):
       if i == 0:
           # Special handling for first item
       elif i == len(items) - 1:
           # Special handling for last item
   ```

---

### ❌ Don't use enumerate when:

1. **Only need the item**
   ```python
   # BAD
   for i, name in enumerate(names):
       print(name)  # Not using i
   
   # GOOD
   for name in names:
       print(name)
   ```

2. **Only need the index**
   ```python
   # BAD
   for i, _ in enumerate(items):
       process_index(i)
   
   # GOOD
   for i in range(len(items)):
       process_index(i)
   ```

3. **Using .index() is clearer**
   ```python
   # BAD
   for i, item in enumerate(items):
       if item == target:
           return i
   
   # GOOD
   return items.index(target)
   ```

---

## Common Patterns

### Pattern 1: First Item Special

```python
from typing import List

items: List[str] = ["Alice", "Bob", "Carol", "David"]

for i, item in enumerate(items):
    if i == 0:
        print(f"First: {item}")
    else:
        print(f"  {item}")

# Output:
# First: Alice
#   Bob
#   Carol
#   David
```

---

### Pattern 2: Last Item Special

```python
from typing import List

items: List[str] = ["Alice", "Bob", "Carol"]

for i, item in enumerate(items):
    if i == len(items) - 1:
        print(f"{item}.")  # Period for last
    else:
        print(f"{item},")  # Comma for others

# Output:
# Alice,
# Bob,
# Carol.
```

**Better way:** Use string join
```python
print(", ".join(items[:-1]) + ".")
```

---

### Pattern 3: Skip First N Items

```python
from typing import List

items: List[str] = ["Header", "Alice", "Bob", "Carol"]

# Skip header row
for i, item in enumerate(items):
    if i == 0:
        continue
    print(item)

# Output:
# Alice
# Bob
# Carol
```

**Better way:** Slice the list
```python
for item in items[1:]:
    print(item)
```

---

### Pattern 4: Process in Chunks

```python
from typing import List

items: List[int] = list(range(20))
chunk_size: int = 5

for i, item in enumerate(items):
    if i % chunk_size == 0:
        print(f"--- Chunk {i // chunk_size + 1} ---")
    print(item)
```

---

## enumerate() with Different Data Types

### With Strings (Iterates Characters)

```python
word: str = "Python"

for i, char in enumerate(word):
    print(f"Position {i}: {char}")

# Output:
# Position 0: P
# Position 1: y
# Position 2: t
# Position 3: h
# Position 4: o
# Position 5: n
```

---

### With Tuples

```python
from typing import Tuple

coordinates: Tuple[int, int, int] = (10, 20, 30)

for i, value in enumerate(coordinates):
    print(f"Axis {i}: {value}")

# Output:
# Axis 0: 10
# Axis 1: 20
# Axis 2: 30
```

---

### With Dict Keys

```python
from typing import Dict

scores: Dict[str, int] = {"Alice": 85, "Bob": 92, "Carol": 78}

# Enumerate keys
for i, name in enumerate(scores.keys()):
    print(f"{i}: {name}")

# Enumerate items (key-value pairs)
for i, (name, score) in enumerate(scores.items()):
    print(f"{i}. {name}: {score}")
```

---

## Comparison: enumerate vs range(len())

### Bad Pattern: range(len())

```python
from typing import List

items: List[str] = ["Alice", "Bob", "Carol"]

# AVOID THIS
for i in range(len(items)):
    print(f"{i}: {items[i]}")
```

**Problems:**
- Have to index into list: `items[i]`
- More error-prone
- Less readable
- Not Pythonic

---

### Good Pattern: enumerate

```python
from typing import List

items: List[str] = ["Alice", "Bob", "Carol"]

# DO THIS
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

**Benefits:**
- Direct access to item
- No manual indexing
- Clearer intent
- Pythonic

---

### When range(len()) is OK

**Only when you need just the indices:**
```python
from typing import List

# Create index list
indices: List[int] = list(range(len(items)))
```

**But even then, prefer:**
```python
indices: List[int] = [i for i, _ in enumerate(items)]
```

---

## Type Hints Best Practices

```python
from typing import List, Tuple, Iterator

items: List[str] = ["Alice", "Bob", "Carol"]

# enumerate returns an iterator of tuples
enum_items: Iterator[Tuple[int, str]] = enumerate(items)

# In loop, unpack automatically
for i, item in enumerate(items):
    # i is inferred as int
    # item is inferred as str
    pass

# If you want to be explicit
for i, item in enumerate(items):
    idx: int = i
    name: str = item
```

---

## Advanced: Enumerate with Comprehensions

```python
from typing import List, Dict

items: List[str] = ["Alice", "Bob", "Carol"]

# List comp with enumerate
numbered: List[str] = [f"{i+1}. {item}" for i, item in enumerate(items)]
# Result: ["1. Alice", "2. Bob", "3. Carol"]

# Dict comp with enumerate
indexed: Dict[int, str] = {i: item for i, item in enumerate(items)}
# Result: {0: "Alice", 1: "Bob", 2: "Carol"}

# Filter using index
first_two: List[str] = [item for i, item in enumerate(items) if i < 2]
# Result: ["Alice", "Bob"]
```

---

## Common Mistakes

### Mistake 1: Forgetting enumerate returns tuple

```python
# WRONG
for item in enumerate(items):
    print(item)  # Prints: (0, "Alice"), (1, "Bob")...

# RIGHT
for i, item in enumerate(items):
    print(i, item)  # Prints: 0 Alice, 1 Bob...
```

---

### Mistake 2: Using index when not needed

```python
from typing import List

names: List[str] = ["Alice", "Bob", "Carol"]

# BAD - don't need index
for i, name in enumerate(names):
    print(name)

# GOOD
for name in names:
    print(name)
```

---

### Mistake 3: Modifying list length during iteration

```python
# DANGEROUS
items: List[int] = [1, 2, 3, 4, 5]

for i, item in enumerate(items):
    if item % 2 == 0:
        items.pop(i)  # Don't do this!

# SAFE - create new list
items = [item for item in items if item % 2 != 0]
```

---

## Summary

**Use enumerate() when you need both index and item:**

```python
for i, item in enumerate(items):
    # Use both i and item
    pass
```

**Start counting from 1:**
```python
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")
```

**Don't use enumerate when:**
- Only need item: `for item in items:`
- Only need index: `for i in range(len(items)):`
- Can use `.index()` method instead

**Type hints:**
```python
from typing import List

items: List[str] = ["a", "b", "c"]
for i, item in enumerate(items):
    # i: int, item: str (inferred)
    pass
```

**Key benefits:**
- ✓ No manual counter
- ✓ Can't forget to increment
- ✓ More readable
- ✓ More Pythonic
- ✓ Less error-prone
