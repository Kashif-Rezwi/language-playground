# Day 1 Study Plan: CLI, Git, and Python Basics

## 1. Day 1 Learning Objectives

By the end of Day 1, you should be able to:

1. Navigate your repository using the terminal.
2. Understand how your Python learning repo is organized.
3. Run a Python file from the command line.
4. Use basic Git commands to track your progress.
5. Write clean beginner Python code using:

   * comments
   * `print()`
   * variables
   * basic data types
   * `type()`
   * `input()`
   * simple type conversion
6. Update `README.md`, `main.py`, and progress trackers correctly.
7. Commit Day 1 work using your repo’s Conventional Commit style.

---

# 2. What the Colab File Covers

The attached Colab notebook is broader than Day 1. It covers:

* What Python is
* Applications of Python
* Data types
* Variables
* Variable naming rules
* Local and global variables
* Deleting variables
* Multiple assignment
* Keywords
* Inputs
* Operators
* Typecasting

For Day 1, focus mainly on:

```text
What is Python?
Variables
Naming rules
Comments
print()
input()
Basic data types
type()
Simple type casting
Basic Git/CLI usage
```

Keep **operators** and deeper typecasting as light preview only. They will become more important on Day 3.

---

# 3. Concepts to Study in Order

## Step 1: Understand the Repository Structure

Your repo follows this learning method:

* root `README.md` explains the overall purpose
* `python/README.md` contains the Python roadmap
* daily folders contain `README.md` and `main.py`
* progress is tracked in `progress.md` files

You should create this Day 1 folder:

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

The setup guide already lists these as your basic navigation commands.

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

Goal: you should always know **where you are** before creating or running files.

---

## Step 3: Git Basics

Study these commands:

```bash
git status
git add .
git commit -m "feat(day-01): complete python basics exercises"
git push origin main
```

Your setup guide already recommends tracking daily progress from the repository root.

For Day 1, use Git after you finish writing and testing code.

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

This is also documented in your setup guide.

For Day 1, you do not need extra packages. You can skip installing `requirements.txt` unless you want to prepare the full environment.

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

Your Colab file includes variable naming rules. For your repo, use Python-style `snake_case`.

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

Do not go deep into lists, tuples, sets, dictionaries yet. The Colab introduces them, but your roadmap covers them properly later in Week 2.

---

## Step 9: `input()`

`input()` takes user input from the terminal.

```python
name = input("Enter your name: ")
print("Hello", name)
```

Important rule:

```python
age = input("Enter your age: ")
print(type(age))
```

Even if the user enters `24`, Python stores it as a string:

```text
<class 'str'>
```

So for numbers, convert input.

```python
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
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

# 4. Suggested `main.py` Structure

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

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
current_year = 2026

birth_year = current_year - user_age

print("Hello", user_name)
print("Your approximate birth year is:", birth_year)
```

Run it from the Day 1 folder:

```bash
python main.py
```

Your setup guide confirms the daily run command is `python main.py`.

---

# 5. Beginner Exercises

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
name = input("Enter your name: ")
print("Welcome to Python Day 1,", name)
```

---

# 6. Intermediate Exercises

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
Hello Kashif, next year you will be 25.
```

---

## Exercise 6: Course Fee Split

Use your real-world thinking.

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

# 7. Advanced Exercises

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

This connects directly to your Week 1 project: **Student Result Management System**.

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

# 8. Mini-Project: Day 1 Profile + Calculator Script

Build a small terminal program inside `main.py`.

It should:

1. Ask your name.
2. Ask your learning goal.
3. Ask how many days you want to study.
4. Ask how many hours per day.
5. Calculate total study hours.

Example:

```python
name = input("Enter your name: ")
goal = input("Enter your learning goal: ")
days = int(input("How many days will you study? "))
hours_per_day = float(input("How many hours per day? "))

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

# 9. Common Mistakes to Avoid

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

## Mistake 4: Copying Colab `>>>` examples into `main.py`

In the notebook, some examples use Python shell style:

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

The Colab shows invalid variable names as examples. Do not run them directly:

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

# 10. Repository Update Instructions

From your repo root:

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

Your root README says the daily learning flow is: scaffold, study, code, clean/format, commit, and log progress.

---

# 11. What to Write in Day 1 `README.md`

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
- Copying notebook `>>>` syntax into `.py` files.
- Using `is` instead of `==` for value comparison.

## End-of-Day Checklist

- [ ] Created Day 1 folder.
- [ ] Added `README.md`.
- [ ] Added `main.py`.
- [ ] Practiced CLI commands.
- [ ] Practiced Git commands.
- [ ] Completed beginner exercises.
- [ ] Completed intermediate exercises.
- [ ] Attempted advanced exercise.
- [ ] Ran `python main.py`.
- [ ] Updated `python/progress.md`.
- [ ] Updated root `progress.md`.
- [ ] Committed and pushed changes.
```

---

# 12. Progress Updates

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

Recommendation: replace local `file:///Users/...` links with relative GitHub-friendly links. Local file links only work on your machine.

---

# 13. Git Commit Instructions

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

This follows your repo’s Conventional Commit rule.

---

# 14. End-of-Day Checklist

Before calling Day 1 complete, verify:

```text
[ ] I can explain what Python is in simple words.
[ ] I can navigate folders using terminal commands.
[ ] I can run main.py from the terminal.
[ ] I understand comments.
[ ] I understand print().
[ ] I understand variables.
[ ] I know basic data types: str, int, float, bool.
[ ] I know input() returns a string.
[ ] I can convert input using int() and float().
[ ] I completed beginner exercises.
[ ] I completed intermediate exercises.
[ ] I attempted at least one advanced exercise.
[ ] I updated Day 1 README.md.
[ ] I updated main.py.
[ ] I updated python/progress.md.
[ ] I updated root progress.md.
[ ] I committed using a clean commit message.
[ ] I pushed changes to GitHub.
```

Day 1 should feel complete when you can build a small terminal script without looking at the Colab: ask for input, store values, convert numbers, calculate something, and print a clean output.
