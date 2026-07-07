# Day 06: Functions & Variable Scope

## Learning Goals

- Understand why functions make programs easier to reuse and maintain.
- Define and call functions with `def`.
- Pass information through parameters and arguments.
- Return calculated values with `return`.
- Understand the difference between local and global scope.
- Refactor student-result logic into small reusable functions for the Week 1 project.

---

## Quick Review From Days 1-5

Before starting Day 6, answer these from memory:

1. Why does `input()` return a string, and how do you convert it for calculations?
2. How would you clean a name and format it in title case?
3. How do you calculate and display a percentage to two decimal places?
4. How do you check that marks are valid and then decide pass or fail?
5. When would you choose a `for` loop instead of a `while` loop?
6. What is the difference between `break` and `continue`?
7. What are counters and accumulators used for?

---

## Study Notes

### Why Functions Matter

A function gives a name to a reusable block of code. Define it once, then call it whenever you need that behavior.

```python
def print_welcome():
    print("Welcome to the Student Result System")


print_welcome()
print_welcome()
```

Defining a function does not run it. The code runs only when the function is called.

### Parameters and Arguments

Parameters are names in the function definition. Arguments are the actual values supplied during a call.

```python
def greet_student(name):
    print(f"Welcome, {name}!")


greet_student("Aarav")
greet_student("Meera")
```

Here, `name` is a parameter. `"Aarav"` and `"Meera"` are arguments.

### Returning Values

Use `return` when the rest of the program needs the function's result.

```python
def calculate_percentage(total_marks, subject_count):
    return total_marks / subject_count


percentage = calculate_percentage(240, 3)
print(f"Percentage: {percentage:.2f}%")
```

`print()` displays a value. `return` sends a value back to the caller. They are not interchangeable.

### Functions Can Call Other Functions

Small functions can be combined to build larger behavior.

```python
def marks_are_valid(marks):
    return 0 <= marks <= 100


def get_result_status(percentage):
    if percentage >= 60:
        return "PASSED"

    return "FAILED"
```

A function stops as soon as it reaches `return`.

### Local Scope

A variable created inside a function is local to that function.

```python
def calculate_total(math_marks, science_marks):
    total = math_marks + science_marks
    return total


result = calculate_total(80, 90)
print(result)
```

`total` cannot be used outside `calculate_total()`. This is helpful: one function's temporary variables do not accidentally interfere with another part of the program.

### Global Scope

A variable created outside functions is global and can be read inside them.

```python
passing_marks = 40


def has_passed(marks):
    return marks >= passing_marks
```

Prefer parameters and return values over changing global variables inside functions. Explicit inputs and outputs make code easier to understand and test.

### Default Parameters

A default value makes an argument optional.

```python
def print_message(message, prefix="INFO"):
    print(f"[{prefix}] {message}")


print_message("Result saved")
print_message("Marks are invalid", "ERROR")
```

Required parameters must come before parameters with default values.

---

## Daily Exercises

Use `main.py` for the main lesson and integrated practice. Use the files in `exercises/` for independent drills.

### Exercise 1: Personalized Greeting

Write a function named `greet_student()` that accepts a student's name and course, then prints a personalized welcome message.

### Exercise 2: Reusable Calculator

Create four functions:

- `add(number_1, number_2)`
- `subtract(number_1, number_2)`
- `multiply(number_1, number_2)`
- `divide(number_1, number_2)`

Each function should return its result. Handle division by zero with a clear returned message.

### Exercise 3: Marks Helper Functions

Create functions that:

- check whether one mark is between `0` and `100`
- calculate the total of three subject marks
- calculate the percentage
- return a grade from a percentage

Call the functions and print a formatted result.

### Exercise 4: Scope Experiment

Create a global variable named `passing_marks`. Write a function with a local variable of the same name and observe which value is used inside and outside the function. Add comments explaining the result in your own words.

### Mini-Project: Functional Student Result System

Refactor the earlier student-result logic into these functions:

- `is_valid_mark(marks)`
- `calculate_total(math_marks, science_marks, english_marks)`
- `calculate_percentage(total_marks, subject_count=3)`
- `calculate_grade(percentage)`
- `has_failed_subject(math_marks, science_marks, english_marks)`
- `get_result_status(percentage, subject_failed)`
- `print_student_report(...)`

Keep `input()` calls in the main program. Pass the collected values into functions, and use returned values for later calculations.

---

## AI/ML Preparation

Functions are essential in data and machine-learning work. They help you:

- reuse cleaning rules across many values
- separate data loading, processing, and reporting
- test one calculation independently
- turn notebook experiments into maintainable programs
- build predictable transformations with clear inputs and outputs

Aim for functions that do one clear job.

---

## Common Mistakes

- Defining a function but forgetting to call it.
- Forgetting parentheses when calling a function.
- Printing a result when the caller needs it returned.
- Forgetting to store or use a returned value.
- Writing code after `return` and expecting it to run.
- Trying to access a local variable outside its function.
- Changing global variables when parameters and return values would be clearer.
- Creating one very large function that does every job.

---

## End-of-Day Checklist

- [ ] Answered the Day 5 review questions from memory.
- [ ] Read the study notes.
- [ ] Ran and modified the examples in `main.py`.
- [ ] Defined and called functions.
- [ ] Practiced parameters and arguments.
- [ ] Returned and reused values.
- [ ] Explained local and global scope in my own words.
- [ ] Completed at least three exercise scripts.
- [ ] Built the Functional Student Result System mini-project.
- [ ] Updated `python/progress.md` with confidence and blockers.
- [ ] Committed the day using Conventional Commit style.
