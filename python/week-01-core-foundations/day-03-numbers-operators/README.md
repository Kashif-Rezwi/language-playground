# Day 03: Numbers & Operations

## Learning Goals

- Understand `int` and `float` numeric values.
- Practice arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, and `**`.
- Learn operator precedence with simple examples.
- Use `round()` and numeric f-string formatting for cleaner output.
- Try beginner-friendly `math` module functions.
- Build small calculation scripts that prepare for marks, fees, and study-hour summaries.

---

## Study Notes

### Numeric Types

Python commonly uses two number types for beginner calculations:

```python
students = 30       # int
average_score = 84.5  # float
```

Use `int()` for whole numbers and `float()` when decimals are allowed.

### Arithmetic Operators

```python
a = 17
b = 5

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division, always returns a float
print(a // b)  # floor division
print(a % b)   # remainder
print(a ** 2)  # exponent
```

### Precedence

Python follows math order rules:

```python
result = 10 + 5 * 2
print(result)  # 20

clear_result = (10 + 5) * 2
print(clear_result)  # 30
```

Use parentheses when the calculation should be obvious to a future reader.

### Rounding and Formatting

```python
percentage = 254 / 3

print(round(percentage, 2))
print(f"{percentage:.2f}%")
```

`round()` changes the numeric display or value. F-string formatting is useful for reports.

### Basic `math` Module

```python
import math

print(math.sqrt(81))
print(math.ceil(7.2))
print(math.floor(7.8))
```

Use the `math` module only for small helper calculations today. Deeper imports come later.

---

## Daily Exercises

Use `main.py` for the main lesson and integrated practice. Use the files in `exercises/` for independent drills.

### Exercise 1: Marks Percentage Calculator

Ask for marks in three subjects. Print total marks and percentage.

Example:

```text
Total Marks: 255.0 / 300
Percentage: 85.00%
```

### Exercise 2: Study Hours Estimator

Ask for study days and average hours per day. Print total study hours and weekly average.

### Exercise 3: Fee Installment Calculator

Ask for total course fee and number of installments. Print the amount per installment.

---

## AI/ML Preparation

Numeric operations show up constantly in AI/ML work:

- calculating totals and averages
- converting raw counts into percentages
- formatting metrics for reports
- understanding remainders and floor division when batching data
- rounding model scores for readable output

Today is not about advanced math. It is about becoming comfortable with reliable everyday calculations.

---

## Common Mistakes

- Forgetting that `input()` returns a string.
- Using `/` when `//` is needed for whole-number division.
- Forgetting parentheses in calculations with multiple operators.
- Printing long decimal values instead of formatting them.
- Mixing text and numbers without casting.

---

## End-of-Day Checklist

- [ ] Read the study notes.
- [ ] Ran `python main.py`.
- [ ] Practiced `int`, `float`, and `type()`.
- [ ] Practiced arithmetic operators.
- [ ] Used `round()` or f-string numeric formatting.
- [ ] Completed the three exercise scripts.
- [ ] Updated `python/progress.md`.
- [ ] Committed the day using Conventional Commit style.
