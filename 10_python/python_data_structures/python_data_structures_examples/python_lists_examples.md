# Python List Examples

## List of Lists As Table

|       | A   | B   | C   | D   |
| ----- | --- | --- | --- | --- |
| **1** | A1  | B1  | C1  | D1  |
| **2** | A2  | B2  | C2  | D2  |
| **3** | A3  | B3  | C3  | D3  |
| **4** | A4  | B4  | C4  | D4  |

## List of Lists As Code

```python
grid = [
    ["A1", "B1", "C1", "D1"],
    ["A2", "B2", "C2", "D2"],
    ["A3", "B3", "C3", "D3"],
    ["A4", "B4", "C4", "D4"],
]
```

## Rule

REMEMBER: Zero-Indexed!
`grid[row_index][column_index]`

## List of Lists showing Access Mapping

|       | 0            | 1            | 2            | 3            |
| ----- | ------------ | ------------ | ------------ | ------------ |
| **0** | `grid[0][0]` | `grid[0][1]` | `grid[0][2]` | `grid[0][3]` |
| **1** | `grid[1][0]` | `grid[1][1]` | `grid[1][2]` | `grid[1][3]` |
| **2** | `grid[2][0]` | `grid[2][1]` | `grid[2][2]` | `grid[2][3]` |
| **3** | `grid[3][0]` | `grid[3][1]` | `grid[3][2]` | `grid[3][3]` |

## List of Lists Including a Header Row

down the line, this will allow you to reinterpret each data row as a record

```python
table = [
    ["A",  "B",  "C",  "D"],   # header row
    ["A1", "B1", "C1", "D1"],
    ["A2", "B2", "C2", "D2"],
    ["A3", "B3", "C3", "D3"],
    ["A4", "B4", "C4", "D4"],
]
```
