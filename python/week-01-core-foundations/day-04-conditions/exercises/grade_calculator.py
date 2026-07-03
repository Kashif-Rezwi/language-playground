# Grade Calculator
# Converts three subject marks into total marks, percentage, grade, and status.

print("\n==========================================")
print("             GRADE CALCULATOR             ")
print("==========================================\n")

math_marks = float(input("Enter Mathematics marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

marks_are_valid = (
    0 <= math_marks <= 100
    and 0 <= science_marks <= 100
    and 0 <= english_marks <= 100
)

if not marks_are_valid:
    print("Invalid marks. Each subject must be between 0 and 100.")
else:
    total_marks = math_marks + science_marks + english_marks
    percentage = total_marks / 3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    subject_failed = (
        math_marks < 40
        or science_marks < 40
        or english_marks < 40
    )
    status = "FAILED" if grade == "F" or subject_failed else "PASSED"

    print("\n--- Grade Summary ---")
    print(f"Total Marks: {total_marks:.1f} / 300")
    print(f"Percentage:  {percentage:.2f}%")
    print(f"Grade:       {grade:>6}")
    print(f"Status:      {status:>6}")

    if subject_failed:
        print("Warning: At least one subject mark is below 40.")
