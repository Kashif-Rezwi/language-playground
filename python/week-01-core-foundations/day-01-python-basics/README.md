# Day 1 Study Plan: CLI, Git, and Python Basics

## 1. Day 1 Learning Objectives

Expected outcomes by the end of Day 1:

1. Navigate the repository using the terminal.
2. Understand how the Python learning repo is organized.
3. Run a Python file from the command line.
4. Use basic Git commands to track progress.
5. Write clean beginner Python code using:

   * comments
   * `print()`
   * variables
   * basic data types
   * `type()`
   * `input()`
   * simple type conversion
6. Update `README.md`, `main.py`, and progress trackers correctly.
7. Commit Day 1 work using the Conventional Commit style.

---

# 2. Concepts to Study in Order

## Step 1: Understand the Repository Structure

The repository follows this learning method:

* root `README.md` explains the overall purpose
* `python/README.md` contains the Python roadmap
* daily folders contain `README.md` and `main.py`
* progress is tracked in `progress.md` files

Create this Day 1 folder:

```text
python/week-01-core-foundations/day-01-python-basics/
├── README.md
└── main.py
```

The Week 1 folder already focuses on Python basics like variables, data types, strings, numbers, conditions, loops, and functions.

---

## Step 2: CLI Basics

Study these commands from `python/setup.md`:

```bash
pwd
ls
cd python
cd ..
mkdir folder-name
```

The setup guide lists these as basic navigation commands.

Practice:

```bash
pwd
ls
cd python
ls
cd week-01-core-foundations
ls
cd ../..
```

Goal: the current directory path should be known before creating or running files.

---

## Step 3: Git Basics

Study these commands:

```bash
git status
git add .
git commit -m "feat(day-01): complete python basics exercises"
git push origin main
```

The setup guide recommends tracking daily progress from the repository root.

For Day 1, use Git after finishing writing and testing code.

---

## Step 4: Python Setup Check

Run:

```bash
python3 --version
```

On Windows, use:

```bash
python --version
```

This is also documented in the setup guide.

For Day 1, external packages are not needed. Installing `requirements.txt` can be skipped unless preparing the full environment.

---

## Step 5: Comments

Comments are notes inside code. Python ignores them when running the file.

```python
# This is a comment
# Comments explain why the code exists

print("Hello, Python!")
```

Use comments to explain beginner code, but do not over-comment obvious things.

Good:

```python
# Store user's name for greeting
name = "Kashif"
print(name)
```

Avoid:

```python
# Print prints something
print("Hello")
```

---

## Step 6: `print()`

`print()` displays output in the terminal.

```python
print("Hello, Python!")
print("I am learning Python Day 1")
print(100)
```

Practice:

```python
print("Name: Kashif")
print("Goal: Learn Python for AI/ML")
print("Day: 1")
```

---

## Step 7: Variables

A variable stores a value.

```python
name = "Kashif"
age = 24
is_learning = True

print(name)
print(age)
print(is_learning)
```

Think of a variable as a label attached to data.

Good variable names:

```python
student_name = "Ali"
course_fee = 118500
is_active = True
```

Avoid:

```python
x = "Ali"       # unclear
a1 = 118500    # unclear
```

For this repository, use Python-style `snake_case` variable names.

---

## Step 8: Basic Data Types

For Day 1, learn these basic types only:

```python
name = "Kashif"       # str
age = 24              # int
height = 5.8          # float
is_student = True     # bool

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

Expected output:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Do not go deep into lists, tuples, sets, or dictionaries yet. The roadmap covers them properly later in Week 2.

---

## Step 9: `input()`

`input()` takes user input from the terminal.

```python
name = input("Enter name: ")
print("Hello", name)
```

Important rule:

```python
age = input("Enter age: ")
print(type(age))
```

Even if the user enters `24`, Python stores it as a string:

```text
<class 'str'>
```

So for numbers, convert input.

```python
age = int(input("Enter age: "))
print("Next year, the age will be", age + 1)
```

---

## Step 10: Simple Type Casting

Type casting means converting one data type into another.

```python
price = "100"
price_number = int(price)

print(price_number + 50)
```

More examples:

```python
age = int("24")
height = float("5.8")
score = str(95)

print(age)
print(height)
print(score)
```

Common beginner mistake:

```python
age = input("Enter age: ")
print(age + 1)  # Error
```

Correct:

```python
age = int(input("Enter age: "))
print(age + 1)
```

---

# 3. Suggested `main.py` Structure

Use the repo’s day template style. The template expects code examples first, then exercises.

Create:

```text
python/week-01-core-foundations/day-01-python-basics/main.py
```

Use this structure:

```python
# Day 01: CLI, Git, and Python Basics
# Topic: comments, print, variables, input, and type casting

# ==========================================
# Code-Along & Examples
# ==========================================
print("--- Code-Along Examples ---")

# Comments
print("Hello, Python!")

# Variables
name = "Kashif"
age = 24
height = 5.8
is_learning_python = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Learning Python:", is_learning_python)

# Checking data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_learning_python))

# Type casting example
course_fee = "118500"
course_fee_number = int(course_fee)

print("Course fee after conversion:", course_fee_number)


# ==========================================
# Exercise 1: Beginner Level
# ==========================================
print("\n--- Exercise 1 ---")

student_name = "Adnan"
student_age = 24
learning_goal = "Learn Python basics"

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Learning Goal:", learning_goal)


# ==========================================
# Exercise 2: Intermediate Level
# ==========================================
print("\n--- Exercise 2 ---")

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

total = first_number + second_number

print("Total:", total)


# ==========================================
# Exercise 3: Advanced Challenge
# ==========================================
print("\n--- Exercise 3 ---")

user_name = input("Enter name: ")
user_age = int(input("Enter age: "))
current_year = 2026

birth_year = current_year - user_age

print("Hello", user_name)
print("Approximate birth year is:", birth_year)
```

Run it from the Day 1 folder:

```bash
python main.py
```

The setup guide confirms the daily run command is `python main.py`.

---

# 4. Beginner Exercises

Complete these inside `main.py`.

## Exercise 1: Personal Profile Printer

Create variables:

```python
name
age
city
learning_goal
```

Print them clearly.

Expected output example:

```text
Name: Kashif
Age: 24
City: Kolkata
Learning Goal: Learn Python for AI/ML
```

---

## Exercise 2: Type Checker

Create variables of these types:

```python
str
int
float
bool
```

Print each value and its type.

Example:

```python
language = "Python"
days = 30
daily_hours = 1.5
is_consistent = True

print(language, type(language))
print(days, type(days))
print(daily_hours, type(daily_hours))
print(is_consistent, type(is_consistent))
```

---

## Exercise 3: Input Greeting

Ask the user for their name and print a greeting.

```python
name = input("Enter name: ")
print("Welcome to Python Day 1,", name)
```

---

# 5. Intermediate Exercises

## Exercise 4: Simple Calculator

Ask the user for two numbers and print:

* sum
* difference
* product
* division

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
```

---

## Exercise 5: Age Calculator

Ask for:

```text
name
age
```

Print:

```text
Hello Kashif, next year's age will be 25.
```

---

## Exercise 6: Course Fee Split

Apply real-world logic.

Ask:

```text
Total course fee
Amount paid by card 1
```

Calculate remaining amount.

```python
total_fee = int(input("Enter total fee: "))
card_1_amount = int(input("Enter card 1 amount: "))

remaining_amount = total_fee - card_1_amount

print("Remaining amount:", remaining_amount)
```

This is a good beginner engineering exercise because it connects Python basics to a real calculation.

---

# 6. Advanced Exercises

## Exercise 7: Simple Student Record

Ask for:

```text
student name
math marks
english marks
science marks
```

Calculate total and average.

```python
student_name = input("Enter student name: ")

math_marks = int(input("Enter math marks: "))
english_marks = int(input("Enter English marks: "))
science_marks = int(input("Enter science marks: "))

total_marks = math_marks + english_marks + science_marks
average_marks = total_marks / 3

print("Student:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
```

This connects directly to the Week 1 project: **Student Result Management System**.

---

## Exercise 8: Data Type Debugging

Predict the output before running:

```python
x = "10"
y = 5

print(x + str(y))
print(int(x) + y)
```

Expected learning:

```python
"10" + "5"  # "105"
10 + 5      # 15
```

---

## Exercise 9: Input Conversion Bug Fix

Broken code:

```python
price = input("Enter price: ")
quantity = input("Enter quantity: ")

total = price * quantity
print(total)
```

Fix it.

Correct version:

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
print("Total:", total)
```

---

# 7. Mini-Project: Day 1 Profile + Calculator Script

Build a small terminal program inside `main.py`.

It should:

1. Ask for a name.
2. Ask for a learning goal.
3. Ask for the number of study days.
4. Ask for study hours per day.
5. Calculate total study hours.

Example:

```python
name = input("Enter name: ")
goal = input("Enter learning goal: ")
days = int(input("Enter number of days to study: "))
hours_per_day = float(input("Enter hours per day: "))

total_hours = days * hours_per_day

print("\n--- Study Plan Summary ---")
print("Name:", name)
print("Goal:", goal)
print("Days:", days)
print("Hours per day:", hours_per_day)
print("Total study hours:", total_hours)
```

This is small, practical, and repo-friendly.

---

# 8. Common Mistakes to Avoid

## Mistake 1: Forgetting that `input()` returns a string

Wrong:

```python
age = input("Enter age: ")
print(age + 1)
```

Correct:

```python
age = int(input("Enter age: "))
print(age + 1)
```

---

## Mistake 2: Using invalid variable names

Wrong:

```python
1name = "Kashif"
my-name = "Kashif"
user age = 24
```

Correct:

```python
name = "Kashif"
my_name = "Kashif"
user_age = 24
```

---

## Mistake 3: Using `is` instead of `==`

Wrong:

```python
a = 10
b = 10

print(a is b)
```

Better for value comparison:

```python
print(a == b)
```

Use `==` when comparing values.

---

## Mistake 4: Copying Python interactive shell `>>>` prompt into `main.py`

Some examples use the Python interactive shell style:

```python
>>> help("keywords")
```

Do not paste `>>>` into `main.py`.

Correct:

```python
help("keywords")
```

---

## Mistake 5: Keeping invalid examples as runnable code

Some learning materials show invalid variable names as examples. Do not run them directly:

```python
1a = 10
n%4 = 5
n 9 = 8
```

Put them in comments instead:

```python
# Invalid examples:
# 1a = 10
# n%4 = 5
# n 9 = 8
```

---

# 9. Repository Update Instructions

From the repository root:

```bash
cd language-playground
```

Create Day 1 folder:

```bash
mkdir -p python/week-01-core-foundations/day-01-python-basics
```

Copy the template:

```bash
cp python/templates/day-template/README.md python/week-01-core-foundations/day-01-python-basics/README.md
cp python/templates/day-template/main.py python/week-01-core-foundations/day-01-python-basics/main.py
```

The root README states the daily learning flow: scaffold, study, code, clean/format, commit, and log progress.

---

# 10. What to Write in Day 1 `README.md`

Update:

```text
python/week-01-core-foundations/day-01-python-basics/README.md
```

Use this structure:

```markdown
# Day 01: CLI, Git, and Python Basics

## Learning Goals

- Understand basic terminal navigation.
- Understand basic Git workflow.
- Run a Python file from the command line.
- Use comments, print statements, variables, and input.
- Understand basic data types and type casting.

## Study Notes

### CLI Basics

- `pwd` shows the current directory.
- `ls` lists files and folders.
- `cd folder-name` moves into a folder.
- `cd ..` moves one level up.

### Git Basics

- `git status` checks changed files.
- `git add .` stages changes.
- `git commit -m "message"` saves changes locally.
- `git push origin main` pushes changes to GitHub.

### Python Basics

- `print()` displays output.
- Variables store values.
- `input()` always returns a string.
- Type casting converts one data type into another.

## Code Examples

See `main.py`.

## Exercises

### Beginner

- Create and print a personal profile.
- Print variable types using `type()`.

### Intermediate

- Build a two-number calculator.
- Build a remaining payment calculator.

### Advanced

- Build a simple student marks summary.
- Debug input/type conversion errors.

## Common Mistakes

- Forgetting to convert input before math.
- Using invalid variable names.
- Copying interactive shell `>>>` syntax into `.py` files.
- Using `is` instead of `==` for value comparison.

## End-of-Day Checklist

- [X] Created Day 1 folder.
- [X] Added `README.md`.
- [X] Added `main.py`.
- [X] Practiced CLI commands.
- [X] Practiced Git commands.
- [X] Completed beginner exercises.
- [X] Completed intermediate exercises.
- [X] Attempted advanced exercise.
- [X] Ran `python main.py`.
- [X] Updated `python/progress.md`.
- [X] Updated root `progress.md`.
- [X] Committed and pushed changes.
```

---

# 11. Progress Updates

Update root `progress.md`.

Current root progress shows Python is in progress and Day is still `0`.

After finishing Day 1, change it to:

```markdown
| Language | Status | Current Focus | Day |
|---|---|---|---|
| Python | In Progress | Day 02: Strings & Manipulation | 1 |
```

Update `python/progress.md`.

Current Day 1 status is `Not Started`.

Change Day 1 row to something like:

```markdown
| **Day 01** | CLI, Git, and Python Basics | 2026-06-24 | Completed | 4/5 | [main.py](week-01-core-foundations/day-01-python-basics/main.py) | Learned CLI, Git basics, variables, input, and type casting. Need more practice with input conversion. |
```

Recommendation: replace local `file:///Users/...` links with relative GitHub-friendly links. Local file links only work on the local machine.

---

# 12. Git Commit Instructions

From repo root:

```bash
git status
```

Stage files:

```bash
git add python/week-01-core-foundations/day-01-python-basics/README.md
git add python/week-01-core-foundations/day-01-python-basics/main.py
git add python/progress.md
git add progress.md
```

Commit:

```bash
git commit -m "feat(day-01): complete python basics exercises"
```

Push:

```bash
git push origin main
```

This follows the Conventional Commit rule.

---

# 13. End-of-Day Checklist

Before calling Day 1 complete, verify:

```text
[X] I can explain what Python is in simple words.
[X] I can navigate folders using terminal commands.
[X] I can run main.py from the terminal.
[X] I understand comments.
[X] I understand print().
[X] I understand variables.
[X] I know basic data types: str, int, float, bool.
[X] I know input() returns a string.
[X] I can convert input using int() and float().
[X] I completed beginner exercises.
[X] I completed intermediate exercises.
[X] I attempted at least one advanced exercise.
[X] I updated Day 1 README.md.
[X] I updated main.py.
[X] I updated python/progress.md.
[X] I updated root progress.md.
[X] I completed current day's exercises and projects
```

Day 1 should feel complete when a small terminal script can be built independently: ask for input, store values, convert numbers, calculate, and print a clean output.
