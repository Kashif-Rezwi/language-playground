# Crash-course practice: create Pandas Series and DataFrames.

import pandas as pd


print("Introduction to Pandas")

# A Series is one-dimensional labeled data. (name is optional)
default_index_series = pd.Series([1, 2, 3, 4, 5], name="number")
print("\nSeries with the default index:\n", default_index_series)

# Index labels do not have to be integers.
labeled_series = pd.Series(
    [1, 2, 3, 4, 5],
    index=["a", "b", "c", "d", "e"],
    name="number",
)
print("\nSeries with custom labels:\n", labeled_series)
print("\nValue selected with label 'b':", labeled_series.loc["b"])

# A DataFrame is two-dimensional labeled data.
students = pd.DataFrame(
    {
        "name": ["Harry", "Rohan", "Shubham"],
        "marks": [100, 53, 45],
    }
)
print("\nStudent DataFrame:\n", students)

# Selecting one DataFrame column returns a Series.
print("\nType of one selected column:", type(students["marks"]))
print("\nType of one selected column:", type(students["marks"]).__name__)

