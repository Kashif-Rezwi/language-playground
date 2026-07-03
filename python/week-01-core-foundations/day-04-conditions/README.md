# Day 04: Conditions & Control Flow

## Learning Goals

- Understand `if`, `elif`, and `else` blocks.
- Use comparison operators to check numeric and text values.
- Combine multiple checks with `and`, `or`, and `not`.
- Validate beginner user input before doing calculations.
- Convert marks and percentages into clear decisions such as pass/fail, grade, and warning messages.
- Prepare the decision logic needed for the Week 1 Student Result Management System.

---

## Quick Review From Days 1-3

Before starting Day 4, quickly recall:

1. Why does `input()` always need casting before numeric comparison?
2. What does `.strip().lower()` do to user-entered text?
3. How do you calculate a percentage from total marks?
4. What is the difference between `/`, `//`, and `%`?

Write the answers in your own words before checking old files. This is active recall, and it makes the lesson stick better.

---

## Study Notes

### Conditions

A condition lets your program choose what to do.

```python
score = 82

if score >= 60:
    print("Passed")
else:
    print("Failed")
```

Python uses indentation to decide which lines belong inside the condition.

### `if`, `elif`, and `else`

Use `elif` when there are multiple possible branches.

```python
percentage = 87

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

Order matters. Put the highest or most specific condition first.

### Comparison Operators

```python
age >= 18
marks < 0
email == ""
answer != "yes"
```

Common operators:

- `==` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

### Logical Operators

Use logical operators to combine checks.

```python
marks = 85

if marks >= 0 and marks <= 100:
    print("Valid marks")
else:
    print("Marks must be between 0 and 100")
```

```python
answer = input("Continue? yes/no: ").strip().lower()

if answer == "yes" or answer == "y":
    print("Continuing...")
else:
    print("Stopping...")
```

### Beginner Input Validation

Day 4 validation should stay simple. Check whether values are in the allowed range after casting them.

```python
marks = float(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Enter a value from 0 to 100.")
else:
    print(f"Accepted marks: {marks:.1f}")
```

Later, error handling will make invalid text input safer. For today, focus on decision logic.

---

## Daily Exercises

Use `main.py` for the main lesson and integrated practice. Use the files in `exercises/` for independent drills.

### Exercise 1: Age Category Checker

Ask for the user's age and print one category:

- child: below 13
- teen: 13 to 17
- adult: 18 to 59
- senior: 60 and above

Also print a validation message if age is below 0.

### Exercise 2: Marks Validator

Ask for marks in one subject. Print:

- invalid if marks are below `0` or above `100`
- passed if marks are `40` or higher
- failed if marks are below `40`

### Exercise 3: Grade Calculator

Ask for three subject marks, calculate total and percentage, then assign:

- `A` for `90%` and above
- `B` for `80%` to `89%`
- `C` for `70%` to `79%`
- `D` for `60%` to `69%`
- `F` below `60%`

Print a report using f-string formatting.

### Exercise 4: Login Decision Simulator

Ask for username and password. Clean the username with `.strip().lower()`.

Accept login only when:

- username is `admin`
- password is `python123`

Print a helpful message for success or failure.

### Mini-Project: Student Result Decision System

Build a small script that asks for:

- student name
- roll number
- mathematics marks
- science marks
- english marks

Then print:

- cleaned student name
- validated roll number status
- total marks
- percentage
- grade
- pass/fail status
- warning if any subject is below `40`

This mini-project is the bridge to the Day 7 Student Result Management System.

---

## AI/ML Preparation

Conditions are used constantly in data work:

- validating whether a value is inside a useful range
- checking whether a field is missing or empty
- assigning categories from numbers
- labeling rows as pass/fail, high/medium/low, valid/invalid
- filtering data before analysis

Today's goal is to think like a data cleaner: check assumptions before trusting values.

---

## Common Mistakes

- Using `=` instead of `==` in comparisons.
- Comparing strings and numbers without casting.
- Putting grade conditions in the wrong order.
- Forgetting indentation after `if`, `elif`, or `else`.
- Using too many separate `if` blocks when only one final decision should be selected.
- Forgetting to clean text input before comparing it.

---

## End-of-Day Checklist

- [ ] Answered the quick review questions from memory.
- [ ] Read the study notes.
- [ ] Ran `python main.py`.
- [ ] Practiced `if`, `elif`, and `else`.
- [ ] Practiced comparison operators.
- [ ] Practiced `and`, `or`, and `not`.
- [ ] Completed at least three exercise scripts.
- [ ] Built the Student Result Decision System mini-project.
- [ ] Updated `python/progress.md` with confidence and blockers.
- [ ] Committed the day using Conventional Commit style.
