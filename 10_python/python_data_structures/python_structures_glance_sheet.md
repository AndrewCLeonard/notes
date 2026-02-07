# 🧠 Python Structures Glance Sheet

## Structures

- List of Lists: `[[1,2],[3,4]]`
- List of Dicts: `[{'name':'A'},{'name':'B'}]`
- Dict of Lists: `{'names':['A','B']}`
- Dict of Dicts: `{'id1':{'name':'A'}}`

## Access

- List of Lists: `grid[0][1]`
- List of Dicts: `list_of_dicts[0]['name']`
- Dict of Lists: `dict_of_lists['names'][1]`
- Dict of Dicts: `dict_of_dicts['id1']['name']`

## Modify

- List of Lists: `grid[0][1] = 'X'`
- List of Dicts: `list_of_dicts[0]['score'] = 90`
- Dict of Lists: `dict_of_lists['scores'][0] += 5`
- Dict of Dicts: `dict_of_dicts['id1']['age'] = 30`

## Looping

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
for key, values in dict_of_lists.items():
    print(key, values)
```

- Dict of Dicts:

```python
for outer, inner in dict_of_dicts.items():
    print(outer, inner['name'])
```

## Quick Use Rules

| Use Case                | Structure                  |
| ----------------------- | -------------------------- |
| Grid of numbers         | List of Lists              |
| Row-by-row labeled data | List of Dictionaries       |
| Column-organized data   | Dictionary of Lists        |
| Fast lookup by label    | Dictionary of Dictionaries |

## Notes

- Lists = ordered
- Dicts = fast lookup
- Sets = uniqueness, no order
