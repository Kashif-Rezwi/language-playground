# Exercise: build a student performance report with Pandas.

import pandas as pd


students = pd.DataFrame(
    {
        "name": ["Aarav", "Meera", "Kashif", "Zoya", "Kabir"],
        "math": [78, 92, 85, 58, 71],
        "science": [85, 89, 88, 62, 69],
        "english": [92, 94, 81, 73, 76],
    }
)

subject_columns = ["math", "science", "english"]

# here axis=1 calculates across the subject columns for each student row.
students["total"] = students[subject_columns].sum(axis=1)
students["average"] = students[subject_columns].mean(axis=1).round(2)
students["result"] = students["average"].ge(60).map({True: "Pass", False: "Fail"})

print("\n\nStudent performance report:\n", students)

top_student = students.loc[students["total"].idxmax()]
print(
    f"\n\nTop student: {top_student['name']} "
    f"with {top_student['total']} total marks"
)

print("\n\nSubject averages:\n", students[subject_columns].mean().round(2))
print("\n\nResult counts:\n", students["result"].value_counts())

