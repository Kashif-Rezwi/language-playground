# Python Learning Playground

This directory contains my structured 30-day Python learning journey, designed to take me from core programming fundamentals to AI/ML readiness.

---

## 📅 Learning Plan Overview

* **Total Duration:** 30 Days (approx. 1–2 hours per day)
* **Main Focus Areas:**
  * Core Python & Data Structures (Weeks 1 & 2)
  * Intermediate Engineering, Testing, and APIs (Week 3)
  * Scientific Libraries & Machine Learning Basics (Week 4)

## Curriculum Rules

Use this roadmap as a practical training plan, not a checklist of every Python feature.

* Write code every day before adding more notes.
* Keep each day focused on one main concept and one practical outcome.
* Prefer small real-world scripts over abstract syntax drills.
* Connect exercises to data, files, validation, and reports whenever possible.
* Keep advanced topics out of Month 1 unless a project truly needs them.

---

## 📈 Weekly Structure

| Week | Focus | Projects |
| :--- | :--- | :--- |
| **Week 1** | Core Python Foundations | Student Result Management System |
| **Week 2** | Data Structures & Problem Solving | Personal Expense Tracker |
| **Week 3** | Intermediate Python & Clean Code | CLI Personal Assistant |
| **Week 4** | Python for AI/ML Foundation | Student Performance Analyzer (Capstone) |

---

## 🗺️ Detailed 30-Day Roadmap

### Week 1: Core Python Foundations

**Weekly goal:** Become comfortable writing and running small terminal programs using variables, input, type conversion, conditions, loops, and functions.

**Hands-on focus:** Beginner CLI scripts, simple calculators, student records, validation messages, and reusable helper functions.

| Day | Topic | Scope |
| :--- | :--- | :--- |
| **Day 01** | CLI, Git, and Python Basics | Command Line navigation, basic Git commands, Python setup, variable declaration, print statements, user inputs, and syntax comments. |
| **Day 02** | Strings & Manipulation | String methods, index slicing, string concatenation, and modern f-string formatting. |
| **Day 03** | Numbers & Operations | Numeric types, arithmetic operators, casting/type conversion, and basic math module applications. |
| **Day 04** | Conditions & Control Flow | Conditionals (`if`, `elif`, `else`), comparison operators, logical operators, and beginner input validation. |
| **Day 05** | Loops & Iterables | `for` and `while` loops, `range()`, repeated input, counters, accumulators, `break`, and `continue`. |
| **Day 06** | Functions & Variable Scope | Defining functions, arguments, return values, local scope, and splitting a script into reusable parts. |
| **Day 07** | Weekly Project 1 | Build **Student Result Management System** inside `projects/student-result-management/`. |

**Mini-projects/exercises:** Profile formatter, simple calculator, marks summary, study-hours calculator, and input conversion bug fixes.

### Week 2: Data Structures & Problem Solving

**Weekly goal:** Learn how Python stores, organizes, transforms, and persists data.

**Hands-on focus:** Lists of records, dictionaries for structured data, filtering, summaries, CSV/JSON files, and error handling.

| Day | Topic | Scope |
| :--- | :--- | :--- |
| **Day 08** | Lists | Creation, modification, index slicing, nesting, list methods, and iteration. |
| **Day 09** | Tuples and Sets | Unpacking tuples, read-only structures, sets operations (union, intersection), and removing duplicates. |
| **Day 10** | Dictionaries | Key-value mapping, dict methods, iteration over keys/values, and nested structures. |
| **Day 11** | Comprehensions | List dictionary, and set comprehensions with conditional filtering. |
| **Day 12** | Error Handling | catching exceptions using `try`, `except`, `finally`, raising exceptions, and logging errors. |
| **Day 13** | File Handling, CSV & JSON | Reading/writing text files, CSV rows, JSON objects, and using context managers (`with`). |
| **Day 14** | Weekly Project 2 | Build **Personal Expense Tracker** inside `projects/personal-expense-tracker/`. |

**AI/ML preparation:** Treat records as rows, dictionaries as structured samples, CSV files as datasets, and summaries as early data analysis.

### Week 3: Intermediate Python & Clean Code

**Weekly goal:** Make scripts more reusable, testable, and project-like without overengineering.

**Hands-on focus:** Modules, virtual environments, package installation, basic classes, debugging, formatting, tests, and API/data fetching.

| Day | Topic | Scope |
| :--- | :--- | :--- |
| **Day 15** | Modules and Imports | Standard library imports, creating custom utility modules, and standard package structure. |
| **Day 16** | Environments & Packages | Virtual environment creation/activation, package installation via `pip`, and managing `requirements.txt`. |
| **Day 17** | OOP Basics | Understanding object-oriented programming: Classes, Objects, instance methods, constructor (`__init__`), and attributes. |
| **Day 18** | Classes in Practical Projects | Use simple classes to model records; lightly introduce `__str__`, but avoid deep inheritance for now. |
| **Day 19** | Debugging, Ruff & Testing | Troubleshooting logic errors, auto-formatting with `ruff`, and writing basic unit tests with `pytest`. |
| **Day 20** | Working with Web APIs | Using `requests` to fetch JSON from a public API, with a local sample JSON fallback if network access is unavailable. |
| **Day 21** | Weekly Project 3 | Build **CLI Personal Assistant** inside `projects/cli-personal-assistant/` (fully structured, tested, and linted). |

**AI/ML preparation:** Learn dependency management, reusable modules, tests, and JSON/API data ingestion before touching ML libraries.

### Week 4: Python for AI/ML Foundation
*(We will transition to Jupyter Notebooks `.ipynb` for data operations starting Day 22)*

**Weekly goal:** Become comfortable loading, cleaning, exploring, visualizing, and modeling a small dataset.

**Hands-on focus:** NumPy arrays, Pandas DataFrames, CSV datasets, missing values, charts, train/test split, and simple model evaluation.

| Day | Topic | Scope |
| :--- | :--- | :--- |
| **Day 22** | NumPy Basics | Creating vectors and matrices, element-wise arithmetic, indexing, slicing, and reshaping arrays. |
| **Day 23** | Pandas Basics | Series vs DataFrames, loading data, inspecting indices, and basic statistics (mean, median, std dev). |
| **Day 24** | Data Cleaning | Dropping missing values, filtering rows, sorting index/values, and casting column data types. |
| **Day 25** | Visualizations | Charting lines, bars, scatter plots, and distributions using Matplotlib and Seaborn. |
| **Day 26** | Exploratory Data Analysis | Conducting a mini-data analysis project on a small CSV dataset stored in the repo. |
| **Day 27** | ML Thinking | Understanding machine learning: Features, Target variables, Training datasets vs. Test datasets. |
| **Day 28** | Simple ML Model | Training your first regression or classification model using `scikit-learn`, then measuring basic accuracy/error. |
| **Day 29** | Capstone Planning | Structuring the end-to-end data pipeline for the final project. |
| **Day 30** | Capstone Build | Build and evaluate the **Student Performance Analyzer** inside `projects/student-performance-analyzer/`. |

**Capstone outcome:** Load a student-performance CSV, clean it, explore grade/score patterns, visualize insights, train one simple model, and write a short conclusion.

---

## What to Skip for Now

These topics are useful later, but they are not worth spending Month 1 energy on:

* decorators
* generators
* advanced inheritance patterns
* async Python
* Django, FastAPI, or web backend frameworks
* deep learning frameworks
* complex algorithms
* Python package publishing
* advanced type hints

## What to Learn Later

After this 30-day track, revisit:

* type hints and `dataclasses`
* SQL and database basics
* stronger `pytest` habits
* Git branching and pull requests
* FastAPI for serving ML/data projects
* feature engineering and model evaluation
* data pipelines and scheduled scripts

## Recommended Daily Routine

1. Read the day's `README.md`.
2. Write or modify code in `main.py`.
3. Complete at least two exercises and one small practical script.
4. Run the file from the terminal.
5. Update `python/progress.md` with confidence and blockers.
6. Commit the day using the repo's Conventional Commit style.
