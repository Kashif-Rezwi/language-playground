# Day 23 guided practice: Pandas fundamentals.

from pathlib import Path

import pandas as pd


DAY_DIRECTORY = Path(__file__).parent
DATA_PATH = DAY_DIRECTORY / "data" / "iris_sample.csv"
OUTPUT_DIRECTORY = DAY_DIRECTORY / "outputs"


def square(value: float) -> float:
    # Return the square of a numeric value.
    return value**2


print("--- 1. Series ---")

default_index_series = pd.Series([1, 2, 3, 4, 5], name="number")
labeled_series = pd.Series(
    [1, 2, 3, 4, 5],
    index=["a", "b", "c", "d", "e"],
    name="number",
)

print("Series with the default index:\n", default_index_series)
print("\n\nSeries with custom labels:\n", labeled_series)
print("\n\nValue at label 'c':", labeled_series.loc["c"])


print("\n\n--- 2. DataFrames ---")

students = pd.DataFrame(
    {
        "name": ["Harry", "Rohan", "Shubham"],
        "marks": [100, 53, 45],
    }
)

print(students)
print("\n\nThe 'marks' column is a:", type(students["marks"]).__name__)


print("\n\n--- 3. Reading and Inspecting CSV Data ---")

iris = pd.read_csv(DATA_PATH)

print("\n\nFirst five rows:\n", iris.head())
print("\n\nLast five rows:\n", iris.tail())
print("\n\nShape:", iris.shape)
print("\n\nColumns:", iris.columns.tolist())
print("\n\nNumeric summary:\n", iris.describe())
print("\n\nDataFrame information:")
iris.info()


print("\n\n--- 4. Selecting Data ---")

varieties = iris["variety"]
selected_columns = iris[["variety", "sepal.length"]]
first_row = iris.iloc[0]
wide_sepals = iris.loc[
    iris["sepal.width"] >= 3.5,
    ["variety", "sepal.width"],
]

print("\n\nOne column (Series):\n", varieties.head())
print("\n\nTwo columns (DataFrame):\n", selected_columns.head())
print("\n\nFirst row by position:\n", first_row)
print("\n\nRows with sepal width >= 3.5:\n", wide_sepals)


print("\n\n--- 5. Missing Values ---")

incomplete_students = pd.DataFrame(
    {
        "name": ["Kashif", "Thamizh", None, "Ken"],
        "marks": [53, None, 70, 90],
        "city": ["Kolkata", "Chennai", "Mumbai", None],
    }
)

rows_without_missing_values = incomplete_students.dropna()
filled_students = incomplete_students.fillna(
    {
        "name": "Unknown",
        "marks": incomplete_students["marks"].median(),
        "city": "Unknown",
    }
)

print("\n\nOriginal data:\n", incomplete_students)
print("\n\nAfter dropna():\n", rows_without_missing_values)
print("\n\nAfter fillna():\n", filled_students)


print("\n\n--- 6. Renaming Columns and Converting Types ---")

renamed_iris = iris.rename(
    columns={
        "sepal.length": "sepal_length",
        "sepal.width": "sepal_width",
        "petal.length": "petal_length",
        "petal.width": "petal_width",
    }
)
renamed_iris["sepal_length"] = renamed_iris["sepal_length"].astype(float)

print("\n\nOriginal columns:", iris.columns.tolist())
print("\n\nRenamed columns:", renamed_iris.columns.tolist())
print("\n\nSepal-length type:", renamed_iris["sepal_length"].dtype)


print("\n\n--- 7. Adding and Transforming Columns ---")

renamed_iris["reviewed"] = False
renamed_iris["sepal_area"] = (
    renamed_iris["sepal_length"] * renamed_iris["sepal_width"]
)
renamed_iris["sepal_length_squared"] = renamed_iris["sepal_length"].apply(square)

print(
    renamed_iris[
        [
            "variety",
            "sepal_length",
            "reviewed",
            "sepal_area",
            "sepal_length_squared",
        ]
    ].head()
)

OUTPUT_DIRECTORY.mkdir(exist_ok=True)
export_path = OUTPUT_DIRECTORY / "iris_enriched.csv"
renamed_iris.to_csv(export_path, index=False)
print("\n\nExported enriched data to:", export_path)


print("\n\n--- 8. Concatenating DataFrames ---")

class_a = pd.DataFrame(
    {
        "name": ["Harry", "Rohan", "Shubham"],
        "marks": [100, 53, 45],
        "city": ["Delhi", "Mumbai", "Delhi"],
    }
)
class_b = pd.DataFrame(
    {
        "name": ["Kashif", "Thamizh", "Ken"],
        "marks": [53, 70, 90],
        "city": ["Kolkata", "Chennai", "Mumbai"],
    }
)
all_students = pd.concat([class_a, class_b], ignore_index=True)

print(all_students)


print("\n--- 9. Merging DataFrames ---")

attendance = pd.DataFrame(
    {
        "name": ["Kashif", "Thamizh", "Ken", "Akarsh"],
        "attendance_percentage": [92, 88, 95, 81],
    }
)
student_details = pd.merge(class_b, attendance, on="name")

print(student_details)
