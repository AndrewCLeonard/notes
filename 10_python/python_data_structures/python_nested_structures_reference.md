# 🧠 Python Nested Structures Study Roadmap

## Types of Structures

| Structure Type             | Example                                           | Description                                   |
| -------------------------- | ------------------------------------------------- | --------------------------------------------- |
| List of Lists              | `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`               | A table/grid — each list is a row             |
| List of Dictionaries       | `[{'name': 'Alice'}, {'name': 'Bob'}]`            | Rows of named properties (like database rows) |
| Dictionary of Lists        | `{'names': ['Alice', 'Bob'], 'scores': [85, 90]}` | Column-style storage                          |
| Dictionary of Dictionaries | `{'student1': {'name': 'Alice', 'score': 85}}`    | Labeled records for fast lookup               |

## Accessing Values

- List of Lists: `grid[row][column]`
- List of Dicts: `list_of_dicts[index]['key']`
- Dict of Lists: `dict_of_lists['key'][index]`
- Dict of Dicts: `dict_of_dicts['outer_key']['inner_key']`

## Modifying Values

- Direct changes using index or keys:
  - `list_of_lists[1][2] = 99`
  - `list_of_dicts[0]['name'] = 'Charlie'`
  - `dict_of_lists['scores'][1] += 5`
  - `dict_of_dicts['student1']['score'] = 95`

## Looping Over Structures

- List of Lists:

```python
for row in grid:
    for item in row:
        print(item)
```

- List of Dicts:

```python
for record in list_of_dicts:
    print(record['name'])
```

- Dict of Lists:

```python
for key, value_list in dict_of_lists.items():
    print(key, value_list)
```

- Dict of Dicts:

```python
for outer_key, inner_dict in dict_of_dicts.items():
    print(outer_key, inner_dict['name'])
```

## Creating Structures Using Loops

- List of Lists:

```python
grid = []
for _ in range(3):
    grid.append([' ', ' ', ' '])
```

- List of Dicts:

```python
people = []
for i in range(3):
    people.append({'id': i, 'name': f'Person{i}'})
```

- Dict of Lists:

```python
data = {'names': [], 'scores': []}
for name, score in [('Alice', 85), ('Bob', 90)]:
    data['names'].append(name)
    data['scores'].append(score)
```

- Dict of Dicts:

```python
students = {}
for i in range(1, 4):
    students[f'student{i}'] = {'name': f'Name{i}', 'score': 80 + i}
```

## When to Use Each Structure

| Use Case                  | Best Structure             |
| ------------------------- | -------------------------- |
| Simple grid (row/column)  | List of Lists              |
| Row-by-row labeled data   | List of Dictionaries       |
| Column-based storage      | Dictionary of Lists        |
| Fast lookup by name or ID | Dictionary of Dictionaries |

## Notes

- Lists: ordered, mutable, indexable.
- Dictionaries: unordered before Python 3.7, ordered afterward; keys must be unique.
- Consider **order**, **labels**, **fast lookup**, or **row access** when choosing a structure.
