# Day 22: NumPy Basics

## Learning Goals

- Understand why NumPy is useful for data analysis and AI/ML work.
- Create 1D and 2D arrays from Python lists.
- Compare Python list behavior with NumPy array behavior.
- Use array properties such as `shape`, `ndim`, `size`, and `dtype`.
- Create arrays with `zeros()`, `ones()`, `full()`, `arange()`, and `linspace()`.
- Reshape arrays without changing their total number of values.
- Select values with indexing, slicing, masks, and `np.where()`.
- Use vectorized operations instead of manual loops.
- Calculate totals, averages, minimums, and maximums with the correct axis.
- Practice reading small real-world datasets as rows and columns.

---

## Quick Review From Earlier Days

Answer these from memory before reading the notes:

1. What is the difference between a Python list and a number variable?
2. How do you access the first item in a list?
3. What does slicing such as `marks[1:4]` return?
4. How does a `for` loop help process many values?
5. When should a function return a value instead of printing it?
6. Why is clean, consistent data important before doing calculations?
7. What does it mean for a table to have rows and columns?

NumPy builds on lists, loops, functions, and tabular thinking from the earlier
weeks.

---

## Study Notes

### Why NumPy?

Python lists are flexible, but data analysis often needs fast calculations on
many numbers at once.

NumPy gives you an `array`, which is designed for numerical work:

```python
import numpy as np

marks = np.array([78, 85, 92])
print(marks + 5)
```

Output:

```text
[83 90 97]
```

The `+ 5` is applied to every value. This is called a vectorized operation.

### Python Lists Versus NumPy Arrays

Python list multiplication repeats the list:

```python
numbers = [1, 2, 3]
print(numbers * 3)
```

Output:

```text
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

NumPy array multiplication multiplies each item:

```python
numbers = np.array([1, 2, 3])
print(numbers * 3)
```

Output:

```text
[3 6 9]
```

This difference is one of the first reasons NumPy feels powerful.

### Creating Arrays

Create arrays from lists:

```python
one_dimensional = np.array([1, 2, 3])
two_dimensional = np.array([[1, 2, 3], [4, 5, 6]])
```

Useful array creators:

```python
np.zeros((2, 3))       # 2 rows, 3 columns of zeros
np.ones((2, 3))        # 2 rows, 3 columns of ones
np.full((2, 2), 7)     # 2 rows, 2 columns filled with 7
np.arange(0, 10, 2)    # 0, 2, 4, 6, 8
np.linspace(0, 10, 5)  # 5 evenly spaced values from 0 to 10
```

Use a tuple such as `(2, 3)` when describing rows and columns.

### Vectors, Matrices, and Tensors

In beginner NumPy practice:

- a 1D array is often called a vector
- a 2D array is often called a matrix
- a 3D or higher array is often called a tensor

```python
vector = np.array([1, 2, 3])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
```

For now, focus mostly on vectors and matrices. They are enough for many data
analysis tasks.

### Array Properties

Use these properties to inspect an array before calculating:

```python
marks = np.array([[78, 85, 92], [66, 74, 81]])

print(marks.shape)  # rows and columns
print(marks.ndim)   # number of dimensions
print(marks.size)   # total values
print(marks.dtype)  # data type
```

For a 2D dataset, `shape` is especially important because it tells you how many
rows and columns you are working with.

### Indexing and Slicing

NumPy uses zero-based indexing like Python lists.

```python
scores = np.array([55, 68, 72, 91, 84])

print(scores[0])     # first value
print(scores[-1])    # last value
print(scores[1:4])   # values from index 1 to 3
```

For 2D arrays, use row and column positions:

```python
marks = np.array([
    [78, 85, 92],
    [66, 74, 81],
])

print(marks[0, 1])  # row 0, column 1
print(marks[1])     # full row at index 1
print(marks[:, 2])  # full column at index 2
```

### Boolean Masks

A mask is an array of `True` and `False` values used to filter data.

```python
scores = np.array([55, 68, 72, 91, 84])

passing_scores = scores[scores >= 60]
print(passing_scores)
```

Use masks when you need values that match a condition.

### `np.where()`

`np.where()` can find positions or choose values based on a condition.

```python
scores = np.array([55, 68, 72, 91, 84])

print(np.where(scores >= 60))
print(np.where(scores >= 60, "Pass", "Fail"))
```

The three-argument version means:

```text
np.where(condition, value_if_true, value_if_false)
```

### Axis Thinking

Axis is one of the most important NumPy ideas.

For a 2D array:

- `axis=0` calculates down each column
- `axis=1` calculates across each row

```python
marks = np.array([
    [78, 85, 92],
    [66, 74, 81],
    [90, 88, 95],
])

print(np.mean(marks, axis=0))  # subject averages
print(np.mean(marks, axis=1))  # student averages
```

When confused, ask: "Do I want one answer per column, or one answer per row?"

### Reshaping

`reshape()` changes the shape, not the values.

```python
numbers = np.arange(12)
matrix = numbers.reshape(3, 4)
```

The total number of values must still match:

```text
12 values can become 3 x 4
12 values can become 2 x 6
12 values cannot become 5 x 3
```

### Broadcasting

Broadcasting lets NumPy apply one value across many values.

```python
yearly_sales = np.array([120000, 180000, 240000])
monthly_average = yearly_sales / 12
```

The `12` is applied to every item.

### NumPy in AI/ML

NumPy prepares you for Pandas, data cleaning, visualization, and machine
learning because most AI/ML workflows depend on numerical arrays.

Common AI/ML tasks use NumPy-style thinking:

- rows as records
- columns as features
- masks for filtering
- vectorized calculations
- means, minimums, maximums, and totals
- reshaping data before passing it into another tool

---

## Code-Along

The guided `main.py` walks through:

1. Creating arrays.
2. Comparing lists and arrays.
3. Inspecting shape, dimensions, size, and dtype.
4. Creating helper arrays from scratch.
5. Reshaping and transposing.
6. Slicing rows and columns.
7. Filtering with masks and `np.where()`.
8. Calculating totals and averages from a student marks matrix.

Run it from the repository root:

```bash
python3 python/week-04-ai-ml-foundation/day-22-numpy-basics/main.py
```

If NumPy is not installed yet, activate the project virtual environment and
install the Week 4 dependency:

```bash
cd python
source .venv/bin/activate
pip install numpy
```

---

## Daily Exercises

Use `main.py` for the guided lesson and the files in `exercises/` for
independent practice. The `exercises/youtube/` folder preserves your video
practice in smaller chunks.

### Exercise 1: Student Marks Statistics

Create a marks matrix where rows are students and columns are subjects.
Calculate:

- total marks per student
- percentage per student
- average marks per subject
- highest and lowest marks per subject
- pass/fail status for each student

File: `exercises/student_marks_statistics.py`

### Exercise 2: Sales Matrix Analysis

Create a sales matrix where rows are products and columns are months.
Calculate:

- total sales per product
- total sales per month
- average monthly sales per product
- best product by total sales
- months where total sales crossed a target

File: `exercises/sales_matrix_analysis.py`

### Exercise 3: Marks Filtering and Cleanup

Use masks and `np.where()` to identify invalid marks, replace invalid marks
with `0`, and calculate clean totals.

File: `exercises/marks_filtering_cleanup.py`

### Mini-Project: Restaurant Performance Report

Build a small restaurant sales report using a 2D NumPy array.

Include:

- restaurant IDs
- yearly sales columns
- total sales per restaurant
- average sales per year
- best restaurant by total sales
- year-over-year growth for each restaurant

File: `exercises/restaurant_performance_report.py`

---

## AI/ML Preparation

After Day 22, you should be comfortable with the idea that many datasets can be
represented as arrays:

```text
rows    -> records, students, restaurants, products
columns -> features, subjects, years, months
values  -> numbers used for analysis
```

This is the mental model you will reuse in Pandas and machine learning.

---

## Common Mistakes

- Forgetting to import NumPy with `import numpy as np`.
- Expecting Python lists and NumPy arrays to behave the same during arithmetic.
- Passing separate lists into `np.array()` instead of one nested list.
- Confusing row index and column index in 2D arrays.
- Forgetting that slicing stop positions are excluded.
- Using `axis=0` when you meant row-wise calculations with `axis=1`.
- Reshaping into a size that does not match the number of values.
- Forgetting that `np.delete()` returns a new array.
- Including ID columns in totals or averages by mistake.
- Trying to solve every array task with loops before checking whether NumPy can
  do it directly.

---

## End-of-Day Checklist

- [ ] Answered the quick review questions from memory.
- [ ] Read the study notes.
- [ ] Installed NumPy in the project virtual environment if needed.
- [ ] Ran and modified `main.py`.
- [ ] Created 1D and 2D arrays.
- [ ] Explained the difference between list multiplication and array multiplication.
- [ ] Used `shape`, `ndim`, `size`, and `dtype`.
- [ ] Practiced slicing rows and columns.
- [ ] Used a boolean mask to filter values.
- [ ] Used `np.where()` for conditional output.
- [ ] Calculated totals and averages with both `axis=0` and `axis=1`.
- [ ] Completed at least three exercise scripts.
- [ ] Built the Restaurant Performance Report mini-project.
- [ ] Updated `python/progress.md` with confidence and blockers.
- [ ] Committed the day using Conventional Commit style.
