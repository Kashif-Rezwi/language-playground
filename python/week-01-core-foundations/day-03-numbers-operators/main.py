# Day 03: Numbers & Operations
# Topic: int, float, arithmetic operators, rounding, and basic math helpers

import math
import datetime

# Advanced Format Specifier Examples (Numerical & Non-Numerical)
print("\n--- Format Specifiers Examples ---")

# 1. Truncating text
title = "Python Language Playground"
print(f"Truncated title: {title:.6s}")  # Limits to first 6 characters: "Python"

# 2. Alignment & Padding
name = "Kashif"
print(f"Left aligned:   '{name:<10s}'")  # Pads with spaces to 10 chars, left-aligned
print(f"Right aligned:  '{name:>10s}'")  # Pads with spaces to 10 chars, right-aligned
print(f"Center aligned: '{name:^10s}'")  # Pads with spaces to 10 chars, centered
print(f"Custom padding: '{name:*^11s}'")  # Centers and pads with '*' to 11 chars

# 3. Numeric Formatting (thousands comma separator)
large_number = 1234567.89
print(f"Comma separator: {large_number:,.2f}")  # Formats with commas and 2 decimals: "1,234,567.89"

# 4. Date formatting (using datetime module)
today = datetime.date.today()

# %A = Full weekday (e.g. Wednesday), %B = Full month (e.g. July), %d = Padded day (e.g. 01), %Y = 4-digit year
print(f"Formatted date: {today:%A, %B %d, %Y}")  # E.g., "Wednesday, July 01, 2026"

# Numeric Types
student_count = int(input("Enter number of students: "))
average_score = float(input("Enter average score: "))

print("\n--- Numeric Types ---")
print("Student count: ", student_count, type(student_count))
print("Average score: ", average_score, type(average_score))

# Arithmetic operations
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("\n--- Arithmetic Operations ---")
print("First number: ", first_number, type(first_number))
print("Second number: ", second_number, type(second_number))

print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")
print(f"Division: {first_number / second_number}")
print(f"Floor division: {first_number // second_number}")
print(f"Remainder: {first_number % second_number}")
print(f"Power: {first_number ** 2}")

# Operator precedence
default_order = 10 + 5 * 2
clear_order = (10 + 5) * 2

print("\n--- Operator Precedence ---")
print(f"10 + 5 * 2 = {default_order}")
print(f"(10 + 5) * 2 = {clear_order}")

# Rounding and numeric formatting
total_marks = int(input("Enter total marks: "))
total_subjects = int(input("Enter total subjects: "))
percentage = total_marks / total_subjects

print("\n--- Rounding and Formatting ---")
print(f"Raw percentage: {percentage}")
print(f"Rounded percentage: {round(percentage, 2)}%")
print(f"Percentage with 1 decimal: {percentage:.1f}%")
print(f"Percentage with 2 decimals: {percentage:.2f}%")
print(f"Percentage with 3 decimals: {percentage:.3f}%")

# Basic math module usage
number = int(input("Enter a number: "))

print("\n--- Basic math Module ---")
print(f"Square root of {number}: {math.sqrt(number)}")
print(f"Ceiling of {number}: {math.ceil(number)}")
print(f"Floor of {number}: {math.floor(number)}")
print(f"Power of {number}: {number ** 2}")
print(f"Remainder of {number}: {number % 2}")
