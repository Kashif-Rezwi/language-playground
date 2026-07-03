# Student Result Decision System
# Bridges Day 4 conditions to the Week 1 Student Result Management project.

print("\n==========================================")
print("       STUDENT RESULT DECISION SYSTEM     ")
print("==========================================\n")

raw_student_name = input("Enter student name: ")
roll_number = int(input("Enter roll number: "))
math_marks = float(input("Enter Mathematics marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

student_name = " ".join(raw_student_name.split()).title()
roll_number_status = "Valid" if roll_number > 0 else "Invalid"
marks_are_valid = (
    0 <= math_marks <= 100
    and 0 <= science_marks <= 100
    and 0 <= english_marks <= 100
)

if not marks_are_valid:
    print("\nInvalid marks. All subject marks must be between 0 and 100.")
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

    subject_warning = (
        math_marks < 40
        or science_marks < 40
        or english_marks < 40
    )
    result_status = "FAILED" if grade == "F" or subject_warning else "PASSED"

    print("\n" + "=" * 44)
    print("          STUDENT RESULT SUMMARY          ")
    print("=" * 44)
    print(f"Student Name:       {student_name}")
    print(f"Roll Number:        {roll_number}")
    print(f"Roll Number Status: {roll_number_status}")
    print("-" * 44)
    print(f"Mathematics:        {math_marks:6.1f} / 100")
    print(f"Science:            {science_marks:6.1f} / 100")
    print(f"English:            {english_marks:6.1f} / 100")
    print("-" * 44)
    print(f"Total Marks:        {total_marks:6.1f} / 300")
    print(f"Percentage:         {percentage:6.2f}%")
    print(f"Grade:              {grade:>6}")
    print(f"Status:             {result_status:>6}")

    if subject_warning:
        print("Warning: One or more subjects are below 40.")

    if roll_number_status == "Invalid":
        print("Warning: Roll number should be greater than 0.")

    print("=" * 44)
