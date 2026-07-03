# Day 06: Functions & Variable Scope
# Topic: function definitions, calls, parameters, return values, and scope

# Function with parameters
def greet_student(name, course):
    print(f"Hello, {name}! Welcome to {course}.")


greet_student("Kashif", "Python Foundations")


# Function that returns a value
def calculate_total(math_marks, science_marks, english_marks):
    total_marks = math_marks + science_marks + english_marks
    return total_marks


total = calculate_total(85, 90, 78)
print(f"\nTotal marks: {total:.1f} / 300")


# Function with a default parameter
def calculate_percentage(total_marks, subject_count=3):
    return total_marks / subject_count


percentage = calculate_percentage(total)
print(f"Percentage: {percentage:.2f}%")


# Function with conditional return values
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


grade = calculate_grade(percentage)
print(f"Grade: {grade}")


# Function that returns a Boolean value
def is_valid_mark(marks):
    return 0 <= marks <= 100


marks = int(input("Enter marks: "))
print(f"\nAre {marks} valid marks? {is_valid_mark(marks)}")


# Local and global variable scope
passing_marks = 40


def show_scope():
    lesson_name = "Functions"
    passing_marks = 50

    print("\n--- Inside show_scope() ---")
    print(f"Lesson name: {lesson_name}")
    print(f"Local passing marks: {passing_marks}")


show_scope()

print("\n--- Outside show_scope() ---")
print(f"Global passing marks: {passing_marks}")

# `lesson_name` is local to show_scope(), so this would raise a NameError:
# print(lesson_name)


# Small functions working together
def get_result_status(percentage, subject_failed):
    if percentage >= 60 and not subject_failed:
        return "PASSED"

    return "FAILED"


def print_result_summary(student_name, total_marks, percentage, grade, status):
    print("\n--- Result Summary ---")
    print(f"Student:    {student_name}")
    print(f"Total:      {total_marks:.1f} / 300")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade:      {grade}")
    print(f"Status:     {status}")


student_name = input("\nEnter student name: ").strip().title()
math_marks = float(input("Enter Mathematics marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

all_marks_are_valid = (
    is_valid_mark(math_marks)
    and is_valid_mark(science_marks)
    and is_valid_mark(english_marks)
)

if not all_marks_are_valid:
    print("Invalid marks. Each mark must be between 0 and 100.")
else:
    total_marks = calculate_total(math_marks, science_marks, english_marks)
    percentage = calculate_percentage(total_marks)
    grade = calculate_grade(percentage)
    subject_failed = (
        math_marks < passing_marks
        or science_marks < passing_marks
        or english_marks < passing_marks
    )
    status = get_result_status(percentage, subject_failed)

    print_result_summary(
        student_name,
        total_marks,
        percentage,
        grade,
        status,
    )
