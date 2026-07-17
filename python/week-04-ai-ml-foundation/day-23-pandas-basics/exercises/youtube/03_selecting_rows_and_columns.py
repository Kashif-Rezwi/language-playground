# Crash-course practice: select Pandas rows and columns.

from pathlib import Path

import pandas as pd


DAY_DIRECTORY = Path(__file__).parents[2]
DATA_PATH = DAY_DIRECTORY / "data" / "iris_sample.csv"
iris = pd.read_csv(DATA_PATH)

# One column label returns a Series.
variety = iris["variety"]
print("\n\nVariety:\n", variety)
print("\n\nVariety Series:\n", variety.head())
print("\n\nVariety Series:\n", variety.tail())
print("\n\nSelected object type:", type(variety).__name__)

# A list of column labels returns a DataFrame.
selected_columns = iris[["variety", "sepal.length"]]
print("\n\nSelected columns:\n", selected_columns)
print("\n\nSelected columns:\n", selected_columns.head())
print("\n\nSelected columns:\n", selected_columns.tail())
print("\n\nSelected object type:", type(selected_columns).__name__)

# iloc selects rows/columns by position.

# select rows
first_row = iris.iloc[0]
print("\n\nFirst row:\n", first_row)
print("\n\nOne row selected with iloc is a:", type(first_row).__name__)

print("\n\nFirst three rows:\n", iris.iloc[:3])
print("\n\nLast three rows:\n", iris.iloc[-3:])
print("\n\nRows 1 to 4:\n", iris.iloc[1:4])

# select columns
first_col = iris.iloc[:, 0]
print("\n\nFirst column:\n", first_col)
print("\n\nOne column selected with iloc is a:", type(first_col).__name__)

print("\n\nFirst three columns:\n", iris.iloc[:, :3])
print("\n\nLast three columns:\n", iris.iloc[:, -3:])
print("\n\nColumns 1 to 4:\n", iris.iloc[:, 1:4])

# find rows based on conditions. (find wide setosa with sepal width >= 3.5)
wide_setosa = iris.loc[
    (iris["variety"] == "Setosa") & (iris["sepal.width"] >= 3.5),
    ["variety", "sepal.length", "sepal.width"],
]
print("\n\nWide Setosa flowers:\n", wide_setosa)

