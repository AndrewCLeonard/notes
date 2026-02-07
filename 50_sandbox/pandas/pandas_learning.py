import pandas as pd
from pathlib import Path

csv_path = Path('titanic.csv')
df = pd.read_csv(csv_path)
# print(df.head(10))
# print("shape:", df.shape)
# print("columns:", list(df.columns))
# print(df.dtypes)
# print(df.info)
ages = df["Age"].head(4)
# print(ages.head())

print(ages.head(10))


# print(ages.dtypes)


def ages_function(s):
    sum: int = 0
    for age in ages:
        print("age: ", age)
        if age.dtype(int):
            sum += age
        print("sum: ", sum)


# ages_function(ages)
