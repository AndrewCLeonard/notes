# Python Data Structures

## Python Core Collection Types

| Type    | Syntax          | Mutable? | Ordered?                  | Unique Items? | Indexable? | Example            |
| ------- | --------------- | -------- | ------------------------- | ------------- | ---------- | ------------------ |
| `list`  | `[]`            | ✅ Yes   | ✅ Yes (since Python 3.7) | ❌ No         | ✅ Yes     | `['a', 'b', 'c']`  |
| `tuple` | `()`            | ❌ No    | ✅ Yes                    | ❌ No         | ✅ Yes     | `('a', 'b', 'c')`  |
| `dict`  | `{key: value}`  | ✅ Yes   | ✅ Yes (since Python 3.7) | ✅ Yes (keys) | ❌ No      | `{'a': 1, 'b': 2}` |
| `set`   | `{}` or `set()` | ✅ Yes   | ❌ No                     | ✅ Yes        | ❌ No      | `{'a', 'b', 'c'}`  |

### Notes

- `set()` is preferred over `{}` when creating an empty set (since `{}` creates an empty dict).
- Keys in dictionaries must be **immutable** (e.g. strings, numbers, tuples).
- Sets and dicts are great for **fast lookup** (via hashing), but not for preserving item order before Python 3.7.

## Common Methods by Collection Type

| Method          | List | Tuple | Dict (values) | Set | Notes                                 |
| --------------- | ---- | ----- | ------------- | --- | ------------------------------------- |
| `.append(x)`    | ✅   | ❌    | ❌            | ❌  | Add to end of list                    |
| `.insert(i, x)` | ✅   | ❌    | ❌            | ❌  | Insert at specific index              |
| `.remove(x)`    | ✅   | ❌    | ❌            | ✅  | Remove item (raises error if missing) |
| `.pop()`        | ✅   | ❌    | ✅ (key req.) | ✅  | Remove & return item                  |
| `.clear()`      | ✅   | ❌    | ✅            | ✅  | Empties the collection                |
| `.copy()`       | ✅   | ✅\*  | ✅            | ✅  | Tuple copies with slicing             |
| `.update()`     | ❌   | ❌    | ✅            | ✅  | Add multiple items or merge data      |
| `.add(x)`       | ❌   | ❌    | ❌            | ✅  | Add new item to set                   |
| `.get(k)`       | ❌   | ❌    | ✅            | ❌  | Safe dictionary key access            |
| `.keys()`       | ❌   | ❌    | ✅            | ❌  | Returns key view                      |
| `.values()`     | ❌   | ❌    | ✅            | ❌  | Returns value view                    |
| `.items()`      | ❌   | ❌    | ✅            | ❌  | Returns key-value pairs               |
