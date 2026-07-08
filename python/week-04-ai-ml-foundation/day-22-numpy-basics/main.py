# Day 22: NumPy Basics
# Topic: arrays, vectorized operations, slicing, masks, and simple analysis.

import numpy as np


print("--- 1. Creating Arrays ---")

marks_1d = np.array([78, 85, 92, 66, 74])
print("1D marks array:", marks_1d)

marks_2d = np.array([
    [78, 85, 92],
    [66, 74, 81],
    [90, 88, 95],
])
print("\n2D marks matrix:\n", marks_2d)


print("\n--- 2. Python List vs NumPy Array ---")

python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

print("Python list * 3:", python_list * 3)
print("NumPy array * 3:", numpy_array * 3)


print("\n--- 3. Array Properties ---")

print("Shape:", marks_2d.shape)
print("Dimensions:", marks_2d.ndim)
print("Size:", marks_2d.size)
print("Data type:", marks_2d.dtype)


print("\n--- 4. Creating Arrays From Scratch ---")

attendance_template = np.zeros((3, 4))
bonus_marks = np.ones((3, 3)) * 5
passing_line = np.full((3,), 60)
roll_numbers = np.arange(101, 104)
progress_points = np.linspace(0, 100, 5)

print("Attendance template:\n", attendance_template)
print("\nBonus marks:\n", bonus_marks)
print("\nPassing line:", passing_line)
print("Roll numbers:", roll_numbers)
print("Progress points:", progress_points)


print("\n--- 5. Vectorized Calculations ---")

updated_marks = marks_1d + 5
scaled_marks = marks_1d * 2

print("Original marks:", marks_1d)
print("Marks after +5 bonus:", updated_marks)
print("Marks multiplied by 2:", scaled_marks)


print("\n--- 6. Reshaping and Transpose ---")

numbers = np.arange(12)
reshaped_numbers = numbers.reshape(3, 4)

print("Original numbers:", numbers)
print("\nReshaped as 3 x 4:\n", reshaped_numbers)
print("\nTransposed matrix:\n", reshaped_numbers.T)


print("\n--- 7. Indexing and Slicing ---")

print("First student marks:", marks_2d[0])
print("Second student's science mark:", marks_2d[1, 1])
print("All math marks:", marks_2d[:, 0])
print("All English marks:", marks_2d[:, 2])
print("First two students:\n", marks_2d[:2])


print("\n--- 8. Masks and np.where() ---")

passing_marks = marks_1d[marks_1d >= 60]
high_marks = marks_1d[marks_1d >= 80]
result_labels = np.where(marks_1d >= 60, "Pass", "Fail")

print("Passing marks:", passing_marks)
print("Marks 80 or above:", high_marks)
print("Result labels:", result_labels)


print("\n--- 9. Student Marks Analysis ---")

student_names = np.array(["Aarav", "Meera", "Kashif"])
subject_names = np.array(["Math", "Science", "English"])

student_totals = np.sum(marks_2d, axis=1)
student_percentages = np.mean(marks_2d, axis=1)
subject_averages = np.mean(marks_2d, axis=0)
subject_highest = np.max(marks_2d, axis=0)
subject_lowest = np.min(marks_2d, axis=0)

for index, student_name in enumerate(student_names):
    print(
        f"{student_name}: total {student_totals[index]}, "
        f"percentage {student_percentages[index]:.2f}%"
    )

print("\nSubject averages:")

for index, subject_name in enumerate(subject_names):
    print(
        f"{subject_name}: avg {subject_averages[index]:.2f}, "
        f"highest {subject_highest[index]}, lowest {subject_lowest[index]}"
    )


print("\n--- 10. Broadcasting ---")

monthly_sales = np.array([12000, 15000, 18000])
yearly_projection = monthly_sales * 12
sales_after_discount = monthly_sales * 0.90

print("Monthly sales:", monthly_sales)
print("Yearly projection:", yearly_projection)
print("Sales after 10% discount:", sales_after_discount)
