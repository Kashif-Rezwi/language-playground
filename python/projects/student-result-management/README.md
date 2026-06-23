# Weekly Project 1: Student Result Management System

## 📋 Objective
Build a command-line interface (CLI) application in Python that allows teachers to record, process, and analyze student test scores. The project integrates core Python foundations learned in Week 1: print statements, variables, type conversions, conditional validation, math operators, loops, and functions.

---

## ⚙️ Core Requirements

1. **Teacher Data Entry:**
   * Accept the student's **Name** and **Roll Number** (numeric).
   * Accept marks for three subjects: **Mathematics**, **Science**, and **English**.
   * Validate that the entered scores are valid numbers between `0` and `100`. If an invalid input is given, prompt again or report a clean validation error.

2. **Core Calculations:**
   * **Total Marks:** Sum of the three subjects (maximum possible: 300).
   * **Percentage:** Total Marks / 3.0.
   * **Grade Allocation:** Allocate a final letter grade based on the percentage:
     * `90%` and above: **A**
     * `80%` to `89%`: **B**
     * `70%` to `79%`: **C**
     * `60%` to `69%`: **D**
     * Below `60%`: **F**

3. **Report Generation:**
   * Print a beautifully structured report card to the terminal using f-strings and standard alignment.

4. **Multi-Student Entry:**
   * The program should run in a loop, asking the teacher if they want to enter another student's details or exit and display final aggregated metrics (e.g., number of students processed, class average percentage).

---

## 🖥️ Expected Report Output Structure

```text
========================================
           STUDENT REPORT CARD
========================================
Roll Number: 101
Student Name: John Doe
----------------------------------------
Mathematics: 85.0 / 100
Science:     92.0 / 100
English:     78.0 / 100
----------------------------------------
TOTAL MARKS: 255.0 / 300
PERCENTAGE:  85.00%
FINAL GRADE: B
STATUS:      PASSED (Grade D or higher)
========================================
```

---

## 🚀 Recommended Extension Goals (Optional)
* Save student reports to a local text file.
* Allow the user to find a student card by searching their Roll Number.
