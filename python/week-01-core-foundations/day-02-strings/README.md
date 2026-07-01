# Day 02: Strings & Manipulation

## Learning Goals

- Understand strings as text data.
- Use common string methods for cleaning and formatting text.
- Practice indexing and slicing.
- Build readable output using f-strings.
- Prepare for data cleaning tasks used later in AI/ML work.

---

## Study Notes

### Strings

A string stores text.

```python
name = "Kashif"
goal = "Learn Python for AI/ML"
```

Strings can use single quotes or double quotes. Pick one style and stay consistent.

### Indexing

Indexing gets one character from a string.

```python
language = "Python"

print(language[0])   # P
print(language[-1])  # n
```

### Slicing

Slicing gets part of a string.

```python
language = "Python"

print(language[0:3])  # Pyt
print(language[:2])   # Py
print(language[2:])   # thon
```

### Useful String Methods

```python
text = "  python for AI/ML  "

print(text.strip())
print(text.lower())
print(text.upper())
print(text.title())
print(text.replace("AI/ML", "data science"))
```

### F-Strings

Use f-strings to build readable output.

```python
name = "Kashif"
day = 2

print(f"{name} is practicing Python Day {day}.")
```

---

## Daily Exercises

Complete these inside `main.py`.

### Exercise 1: Profile Formatter

Ask the user for:

- name
- city
- learning goal

Clean extra spaces and print a formatted profile.

### Exercise 2: Username Generator

Ask the user for their first and last name. Generate a lowercase username.

Example:

```text
First name: Kashif
Last name: Rezwi
Username: kashif.rezwi
```

### Exercise 3: Email Cleaner

Ask for an email address. Clean spaces, lowercase it, and print the domain.

Example:

```text
Email:  Kashif@Example.COM
Clean email: kashif@example.com
Domain: example.com
```

### Exercise 4: Text Summary

Ask the user for one sentence. Print:

- original sentence
- cleaned sentence
- character count
- first 10 characters
- last 10 characters

### Mini-Project: Student Name Normalizer

Ask for three student names with messy spacing/casing. Print a clean numbered list.

Example:

```text
1. Kashif Rezwi
2. Ali Khan
3. Sara Ahmed
```

---

## AI/ML Preparation

String cleaning is one of the first skills needed for data work. Real datasets often contain names, emails, labels, categories, and text fields with inconsistent casing or extra spaces.

Today's focus prepares you for:

- cleaning CSV text columns
- standardizing labels
- extracting parts of text
- preparing user-entered data for storage

---

## Common Mistakes

- Forgetting that indexes start at `0`.
- Forgetting that string methods return a new value.
- Using `+` for messy output when an f-string would be clearer.
- Forgetting to clean user input with `.strip()`.

---

## End-of-Day Checklist

- [X] Read the study notes.
- [X] Practiced indexing and slicing.
- [X] Practiced `.strip()`, `.lower()`, `.upper()`, `.title()`, and `.replace()`.
- [X] Completed at least three exercises.
- [X] Built the Student Name Normalizer mini-project.
- [X] Ran `python main.py`.
- [X] Updated `python/progress.md`.
- [X] Committed the day using Conventional Commit style.
