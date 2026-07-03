# Marks Helper Functions
# Breaks marks validation and calculations into small reusable functions.


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


print("\n==========================================")
print("           MARKS HELPER FUNCTIONS         ")
print("==========================================\n")

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

    print("\n--- Marks Summary ---")
    print(f"Total marks: {total_marks:.1f} / 300")
    print(f"Percentage:  {percentage:.2f}%")
    print(f"Grade:       {grade}")
