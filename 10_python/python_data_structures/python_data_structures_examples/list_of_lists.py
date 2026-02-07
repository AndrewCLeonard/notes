table = [
    ["A", "B", "C", "D"],  # header row
    ["A1", "B1", "C1", "D1"],
    ["A2", "B2", "C2", "D2"],
    ["A3", "B3", "C3", "D3"],
    ["A4", "B4", "C4", "D4"],
]

# print(table)

HEADER_ROW_INDEX = 0

D2 = table[2][3]  # remember that row 0 is a header row in this example
# print(D2)

# REMEMBER: table[row_index][column_index]
# for row in table[1:]:
    # print(row)

# To get just the data rows without changing the data
table_data = table[1:]

print(table_data)

