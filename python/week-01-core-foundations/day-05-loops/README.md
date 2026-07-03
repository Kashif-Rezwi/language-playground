# Day 05: Loops & Iterables

## Learning Goals

- Understand why loops are used.
- Practice `for` loops with `range()`.
- Practice `while` loops for repeated input.
- Use counters and accumulators.
- Control loop flow with `break` and `continue`.
- Build repeated student-entry logic for the Week 1 Student Result Management System.

---

## Quick Review From Days 1-4

Before starting Day 5, quickly answer:

1. Why does `input()` return a string?
2. How do you convert marks into a percentage?
3. When should you use `if`, `elif`, and `else`?
4. How do you validate that marks are between `0` and `100`?
5. What does `.strip().lower()` help with?

Write the answers in your own words before checking old files.

---

## Study Notes

### Why Loops Matter

A loop repeats work without copying code again and again.

Without a loop:

```python
print("Student 1")
print("Student 2")
print("Student 3")
```

With a loop:

```python
for student_number in range(1, 4):
    print(f"Student {student_number}")
```

### `for` Loops

Use a `for` loop when you know how many times to repeat.

```python
for number in range(1, 6):
    print(number)
```

`range(1, 6)` produces `1, 2, 3, 4, 5`.

### `while` Loops

Use a `while` loop when repetition depends on a condition.

```python
answer = "yes"

while answer == "yes":
    print("Keep practicing Python.")
    answer = input("Continue? yes/no: ").strip().lower()
```

Always make sure a `while` loop can eventually stop.

### Counters

A counter tracks how many times something happened.

```python
passed_count = 0

for marks in [85, 32, 91]:
    if marks >= 40:
        passed_count = passed_count + 1

print(f"Passed students: {passed_count}")
```

### Accumulators

An accumulator stores a running total.

```python
total_marks = 0

for marks in [85, 90, 78]:
    total_marks = total_marks + marks

print(f"Total marks: {total_marks}")
```

### `break` and `continue`

Use `break` to stop a loop early.

```python
while True:
    command = input("Enter command: ").strip().lower()

    if command == "exit":
        break
```

Use `continue` to skip the rest of the current loop and move to the next round.

```python
for marks in [80, -5, 91]:
    if marks < 0:
        continue

    print(f"Accepted marks: {marks}")
```

---

## Daily Exercises

Use `main.py` for the main lesson and integrated practice. Use the files in `exercises/` for independent drills.

### Exercise 1: Multiplication Table

Ask the user for a number and print its multiplication table from `1` to `10`.

### Exercise 2: Marks Average Loop

Ask how many subjects a student has. Use a loop to collect marks, calculate total marks, and print the average.

### Exercise 3: Password Attempts

Give the user three attempts to enter the correct password. Stop early when the password is correct.

### Exercise 4: Skip Invalid Marks

Loop through five entered marks. If a mark is outside `0` to `100`, skip it and continue with the next one.

### Mini-Project: Student Marks Collector

Build a script that repeatedly asks for student names and marks until the user chooses to stop.

Track:

- number of students processed
- total class percentage
- passed students
- failed students
- class average percentage

This is the loop foundation for the Day 7 Student Result Management System.

---

## AI/ML Preparation

Loops are used constantly in data work:

- reading rows one by one
- cleaning repeated values
- counting valid and invalid records
- accumulating totals and averages
- stopping when a condition is met
- skipping bad data during preprocessing

Today's goal is to become comfortable repeating logic safely and clearly.

---

## Common Mistakes

- Creating an infinite `while` loop by forgetting to update the condition.
- Forgetting that `range(1, 10)` stops before `10`.
- Resetting a counter inside the loop by mistake.
- Using `break` when `continue` is the better choice.
- Copying repeated code instead of using a loop.
- Forgetting to validate input before adding it to a total.

---

## End-of-Day Checklist

- [ ] Answered the quick review questions from memory.
- [ ] Read the study notes.
- [ ] Ran `python main.py`.
- [ ] Practiced `for` loops and `range()`.
- [ ] Practiced `while` loops.
- [ ] Used at least one counter and one accumulator.
- [ ] Practiced `break` and `continue`.
- [ ] Completed at least three exercise scripts.
- [ ] Built the Student Marks Collector mini-project.
- [ ] Updated `python/progress.md` with confidence and blockers.
- [ ] Committed the day using Conventional Commit style.
