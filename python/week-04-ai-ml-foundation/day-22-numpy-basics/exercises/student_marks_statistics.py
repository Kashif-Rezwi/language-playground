# Student Marks Statistics
# Practice NumPy row-wise and column-wise calculations using a marks matrix.

import numpy as np


print("\n==============================================")
print("          STUDENT MARKS STATISTICS            ")
print("==============================================\n")

student_names = np.array(["Aarav", "Meera", "Kashif", "Nisha"])
subject_names = np.array(["Math", "Science", "English"])

# Rows are students. Columns are subjects.
marks = np.array([
    [78, 85, 92],
    [66, 74, 81],
    [90, 88, 95],
    [52, 61, 58],
])

print("Marks matrix:\n", marks)
print("Shape:", marks.shape)

# axis=1 calculates across each row, so it gives one result per student.
student_totals = np.sum(marks, axis=1)
student_percentages = np.mean(marks, axis=1)

# axis=0 calculates down each column, so it gives one result per subject.
subject_averages = np.mean(marks, axis=0)
subject_highest = np.max(marks, axis=0)
subject_lowest = np.min(marks, axis=0)

print("\n--- Student Results ---")

for index, student_name in enumerate(student_names):
    status = "Pass" if student_percentages[index] >= 60 else "Fail"
    print(
        f"{student_name}: total {student_totals[index]}, "
        f"percentage {student_percentages[index]:.2f}%, {status}"
    )

print("\n--- Subject Summary ---")

for index, subject_name in enumerate(subject_names):
    print(
        f"{subject_name}: average {subject_averages[index]:.2f}, "
        f"highest {subject_highest[index]}, lowest {subject_lowest[index]}"
    )
