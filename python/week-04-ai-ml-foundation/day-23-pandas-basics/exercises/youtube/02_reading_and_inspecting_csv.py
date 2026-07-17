# Crash-course practice: read and inspect CSV data with Pandas.

from pathlib import Path

import pandas as pd


# Constructing a path to the iris_sample.csv file.
DAY_DIRECTORY = Path(__file__).parents[2]
DATA_PATH = DAY_DIRECTORY / "data" / "iris_sample.csv"

# Reading the CSV file into a pandas DataFrame.
iris = pd.read_csv(DATA_PATH)

print("\n\nFirst five rows:\n", iris.head())
print("\n\nLast five rows:\n", iris.tail())
print("\n\nShape:", iris.shape)
print("\n\nColumns:", iris.columns.tolist())
print("\n\nData types:\n", iris.dtypes)

print("\n\nNumeric summary:\n", iris.describe())

# info() prints its output directly and returns None.
print("\n\nDataFrame information:")
iris.info()

