# Day 23: Pandas Basics

## Learning Goals

- Understand the difference between a Pandas `Series` and `DataFrame`.
- Create Series with default and custom index labels.
- Create DataFrames from Python dictionaries.
- Load a CSV file with `pd.read_csv()`.
- Inspect data with `head()`, `tail()`, `info()`, and `describe()`.
- Select columns, multiple columns, and rows by position or label.
- Handle missing values with `dropna()` and `fillna()`.
- Rename columns and convert column data types safely.
- Add calculated columns with vectorized operations and `apply()`.
- Export a DataFrame with `to_csv()`.
- Combine row-shaped datasets with `concat()` and related tables with `merge()`.

---

## Source Practice

The files in `exercises/youtube/` preserve the topics practiced in the Pandas
crash-course notebook as small, terminal-friendly scripts. The Google Colab
upload step has been replaced with the local dataset at
`data/iris_sample.csv`, so every example can run directly from this repository.

The repository version also clarifies a few easy-to-miss details from the
notebook:

- `df.info()` prints information and returns `None`.
- `dropna()`, `fillna()`, and `rename()` return a new DataFrame unless their
  result is assigned or `inplace=True` is used.
- Renaming a DataFrame column does not modify the original CSV file.
- Converting decimal measurements with `astype(int)` removes their decimal
  portion; use `float` when the precision matters.
- `pd.concat()` keeps the original indexes unless `ignore_index=True` is used.
- `pd.merge()` performs an inner join by default, keeping only matching keys.

---

## Quick Review From Day 22

Answer these before reading the notes:

1. How are rows and columns represented in a 2D NumPy array?
2. What is the difference between `axis=0` and `axis=1`?
3. What does a boolean mask do?
4. Why are vectorized operations usually preferred over manual loops?
5. What information does an array's `shape` provide?

Pandas builds on the same row, column, filtering, and vectorized-operation
thinking used in NumPy.

---

## Study Notes

### Series and DataFrames

A `Series` is one-dimensional labeled data. It is similar to one column in a
table:

```python
import pandas as pd

marks = pd.Series([100, 53, 45])
print(marks)
```

By default, Pandas creates integer index labels starting at `0`. Custom labels
can make the values easier to understand:

```python
marks = pd.Series(
    [100, 53, 45],
    index=["Harry", "Rohan", "Shubham"],
    name="marks",
)

print(marks.loc["Harry"])
```

A `DataFrame` is two-dimensional labeled data with rows and columns:

```python
students = pd.DataFrame({
    "name": ["Harry", "Rohan", "Shubham"],
    "marks": [100, 53, 45],
})
```

Each DataFrame column is a Series:

```python
print(type(students["marks"]))  # pandas.Series
```

### Loading CSV Data

Use `pd.read_csv()` to load a comma-separated file:

```python
from pathlib import Path

data_path = Path(__file__).parent / "data" / "iris_sample.csv"
iris = pd.read_csv(data_path)
```

Using `Path` keeps the script working even when it is launched from a different
directory.

### Inspect Before Transforming

Always inspect a dataset before changing it:

```python
print(iris.head())
print(iris.tail())
print(iris.shape)
print(iris.columns)
print(iris.dtypes)
iris.info()
print(iris.describe())
```

These answer different questions:

- `head()` previews the first five rows by default.
- `tail()` previews the last five rows by default.
- `shape` gives `(number_of_rows, number_of_columns)`.
- `columns` lists the column labels.
- `dtypes` shows the type stored in each column.
- `info()` prints column types, non-null counts, and memory usage.
- `describe()` calculates statistics for numeric columns by default.

Do not store the result of `info()` expecting a summary DataFrame:

```python
result = iris.info()
print(result)  # None
```

### Selecting Columns and Rows

Single brackets with one column label return a Series:

```python
species = iris["variety"]
```

Double brackets with a list of labels return a DataFrame:

```python
measurements = iris[["variety", "sepal.length"]]
```

Use `iloc` for integer positions:

```python
first_row = iris.iloc[0]
first_three_rows = iris.iloc[:3]
first_value = iris.iloc[0, 0]
```

Use `loc` for labels and conditions:

```python
wide_sepals = iris.loc[
    iris["sepal.width"] >= 3.5,
    ["variety", "sepal.width"],
]
```

### Missing Values

`dropna()` removes rows or columns containing missing values:

```python
complete_rows = students.dropna()
```

`fillna()` replaces missing values:

```python
filled_students = students.fillna({"marks": students["marks"].median()})
```

Both methods return new DataFrames by default. Assign the result when you want
to keep it:

```python
students = students.dropna(subset=["name"])
```

### Renaming Columns

`rename()` returns a renamed copy by default:

```python
renamed = iris.rename(columns={"sepal.length": "sepal_length"})
```

Using `inplace=True` changes the DataFrame object:

```python
iris.rename(columns={"sepal.length": "sepal_length"}, inplace=True)
```

Neither version changes the CSV file on disk. Use `to_csv()` if the transformed
data should be saved.

### Converting Data Types

Use `astype()` when a column contains valid values that need a different type:

```python
students["marks"] = students["marks"].astype(float)
```

Be careful with measurements:

```python
whole_centimetres = iris["sepal.length"].astype(int)
```

A value such as `5.8` becomes `5`, so keep it as `float` when the decimal part
matters. For text that may contain invalid numbers, use `pd.to_numeric()`:

```python
students["marks"] = pd.to_numeric(students["marks"], errors="coerce")
```

Invalid values become missing values and can then be handled explicitly.

### Adding and Transforming Columns

Assign a scalar to give every row the same value:

```python
iris["reviewed"] = False
```

Prefer a vectorized operation for simple calculations:

```python
iris["sepal.area"] = iris["sepal.length"] * iris["sepal.width"]
```

Use `apply()` when the calculation needs a custom function:

```python
def square(value):
    return value**2


iris["sepal.length.squared"] = iris["sepal.length"].apply(square)
```

### Exporting Data

Write a DataFrame to CSV with `to_csv()`:

```python
iris.to_csv("iris_enriched.csv", index=False)
```

`index=False` prevents Pandas from writing the DataFrame index as an extra CSV
column.

### Concatenating DataFrames

Use `pd.concat()` when tables have the same columns and should be stacked as
more rows:

```python
all_students = pd.concat(
    [class_a, class_b],
    ignore_index=True,
)
```

The original DataFrames are unchanged.

### Merging DataFrames

Use `pd.merge()` when tables describe related information and share a key:

```python
student_details = pd.merge(
    students,
    attendance,
    on="name",
    how="inner",
)
```

Common join types are:

- `inner`: keep matching keys from both tables.
- `left`: keep every key from the left table.
- `right`: keep every key from the right table.
- `outer`: keep every key from both tables.

Choose the join type based on which records must be preserved.

---

## Code-Along

The guided `main.py` walks through the complete crash-course material with a
local dataset:

1. Creating Series and DataFrames.
2. Loading and inspecting an Iris CSV sample.
3. Selecting columns and rows.
4. Filtering with a condition.
5. Handling missing values.
6. Renaming and converting columns.
7. Adding calculated columns and exporting data.
8. Concatenating and merging DataFrames.

Run it from the repository root:

```bash
python3 python/week-04-ai-ml-foundation/day-23-pandas-basics/main.py
```

If Pandas is not installed, activate the project virtual environment and
install it:

```bash
cd python
source .venv/bin/activate
pip install pandas
```

The export example writes generated files under `outputs/`. That folder is
ignored by Git except for its `.gitkeep` placeholder.

---

## Crash-Course Practice Scripts

The `exercises/youtube/` directory contains the notebook material split into
focused scripts:

1. `01_series_and_dataframes.py`
2. `02_reading_and_inspecting_csv.py`
3. `03_selecting_rows_and_columns.py`
4. `04_missing_values_renaming_and_types.py`
5. `05_adding_columns_apply_and_export.py`
6. `06_concatenating_and_merging.py`

Run any script directly from the repository root. For example:

```bash
python3 python/week-04-ai-ml-foundation/day-23-pandas-basics/exercises/youtube/03_selecting_rows_and_columns.py
```

---

## Independent Exercises

### Exercise 1: Student Performance Report

Create a student DataFrame, calculate totals and averages, assign pass/fail
results, and identify the highest-performing student.

File: `exercises/student_performance_report.py`

### Exercise 2: Data Quality Cleanup

Clean inconsistent names, convert text marks to numbers, fill missing marks,
remove rows without student names, and report the cleaned data types.

File: `exercises/data_quality_cleanup.py`

### Mini-Project: Iris Species Summary

Load the local Iris CSV and create a summary containing the record count and
average measurements for each variety.

File: `exercises/iris_species_summary.py`

---

## NumPy to Pandas Mental Model

```text
NumPy array       -> values organized by numeric positions
Pandas Series     -> one-dimensional values with an index and optional name
Pandas DataFrame  -> rows and named columns, where each column is a Series
CSV file          -> data on disk that can be loaded into a DataFrame
```

NumPy remains useful underneath Pandas, but Pandas adds labels and table-aware
tools that make real datasets easier to inspect and transform.

---

## Common Mistakes

- Forgetting `import pandas as pd`.
- Expecting `df["column"]` to return a DataFrame instead of a Series.
- Using `iloc` with labels or `loc` with integer positions accidentally.
- Assigning `df.info()` to a variable and expecting a DataFrame.
- Calling `dropna()`, `fillna()`, or `rename()` without saving the result.
- Assuming an in-memory DataFrame change also edits the source CSV.
- Converting decimal measurements to integers and losing precision.
- Exporting without `index=False` and getting an unwanted index column.
- Concatenating without `ignore_index=True` and keeping duplicate indexes.
- Merging on a column that is not a reliable shared key.
- Forgetting that an inner merge drops non-matching records.

---

## End-of-Day Checklist

- [ ] Answered the NumPy review questions.
- [ ] Read the Pandas study notes.
- [ ] Ran `main.py` successfully.
- [ ] Created a Series with custom labels.
- [ ] Created a DataFrame from a dictionary.
- [ ] Loaded `data/iris_sample.csv`.
- [ ] Used `head()`, `tail()`, `info()`, and `describe()`.
- [ ] Selected one column, multiple columns, and positional rows.
- [ ] Filtered rows with `loc` and a boolean condition.
- [ ] Practiced both `dropna()` and `fillna()`.
- [ ] Renamed a column without confusing the DataFrame with the source file.
- [ ] Converted a column type without accidentally losing needed precision.
- [ ] Added a calculated column.
- [ ] Exported a DataFrame with `index=False`.
- [ ] Combined data with both `concat()` and `merge()`.
- [ ] Completed the independent exercises.
- [ ] Updated `python/progress.md`.

