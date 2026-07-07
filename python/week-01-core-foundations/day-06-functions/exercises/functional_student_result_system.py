# Functional Student Result System
# Refactors student-result logic into small reusable functions.

PASSING_MARKS = 40
PASSING_PERCENTAGE = 60


def is_valid_mark(marks):
    return 0 <= marks <= 100


def calculate_total(math_marks, science_marks, english_marks):
    return math_marks + science_marks + english_marks


def calculate_percentage(total_marks, subject_count=3):
    return total_marks / subject_count


def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def has_failed_subject(math_marks, science_marks, english_marks):
    return (
        math_marks < PASSING_MARKS
        or science_marks < PASSING_MARKS
        or english_marks < PASSING_MARKS
    )


def get_result_status(percentage, subject_failed):
    if percentage >= PASSING_PERCENTAGE and not subject_failed:
        return "PASSED"

    return "FAILED"


def print_student_report(
    student_name,
    roll_number,
    math_marks,
    science_marks,
    english_marks,
    total_marks,
    percentage,
    grade,
    status,
):
    print("\n" + "=" * 46)
    print("                STUDENT REPORT              ")
    print("=" * 46)
    print(f"Student:       {student_name}")
    print(f"Roll number:   {roll_number}")
    print(f"Mathematics:   {math_marks:.1f}")
    print(f"Science:       {science_marks:.1f}")
    print(f"English:       {english_marks:.1f}")
    print("-" * 46)
    print(f"Total marks:   {total_marks:.1f} / 300")
    print(f"Percentage:    {percentage:.2f}%")
    print(f"Grade:         {grade}")
    print(f"Status:        {status}")
    print("=" * 46)


print("\n==============================================")
print("       FUNCTIONAL STUDENT RESULT SYSTEM       ")
print("==============================================\n")

student_name = input("Enter student name: ").strip().title()
roll_number = input("Enter roll number: ").strip().upper()
math_marks = float(input("Enter Mathematics marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

all_marks_are_valid = (
    is_valid_mark(math_marks)
    and is_valid_mark(science_marks)
    and is_valid_mark(english_marks)
)

if not student_name:
    print("Invalid student name.")
elif not roll_number:
    print("Invalid roll number.")
elif not all_marks_are_valid:
    print("Invalid marks. Each mark must be between 0 and 100.")
else:
    total_marks = calculate_total(math_marks, science_marks, english_marks)
    percentage = calculate_percentage(total_marks)
    grade = calculate_grade(percentage)
    subject_failed = has_failed_subject(
        math_marks,
        science_marks,
        english_marks,
    )
    status = get_result_status(percentage, subject_failed)

    print_student_report(
        student_name,
        roll_number,
        math_marks,
        science_marks,
        english_marks,
        total_marks,
        percentage,
        grade,
        status,
    )
