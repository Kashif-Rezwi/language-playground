# Crash-course practice: missing values, renaming, and data types.

import pandas as pd


students = pd.DataFrame(
    {
        "student.name": ["Kashif", "Thamizh", None, "Ken"],
        "marks": ["53", None, "not recorded", "90"],
        "city": ["Kolkata", "Chennai", "Mumbai", None],
    }
)

print("Original data:\n", students)
print("\n\nMissing values per column:\n", students.isna().sum())

# dropna() returns a new DataFrame by default.
students_with_names = students.dropna(subset=["student.name"])
print("\nRows with a student name:\n", students_with_names)

# Rename returns a new DataFrame unless the result is assigned or inplace=True is used. 
# It does not edit any source CSV file.
students = students_with_names.rename(columns={"student.name": "student_name"})

# errors="coerce" changes invalid numeric text to NaN.
students["marks"] = pd.to_numeric(students["marks"], errors="coerce")
students["marks"] = students["marks"].fillna(students["marks"].median())
students["city"] = students["city"].fillna("Unknown")

# The median is 71.5, so keep a floating type instead of discarding precision by
# forcing the imputed value into an integer.
students["marks"] = students["marks"].astype("Float64")

print("\nCleaned data:\n", students)
print("\nCleaned data types:\n", students.dtypes)
