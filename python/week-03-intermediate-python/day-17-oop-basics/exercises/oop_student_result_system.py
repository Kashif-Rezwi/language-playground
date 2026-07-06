# OOP Student Result System
# Refactors the function-based Day 6 mini-project into a Student class.

PASSING_MARKS = 40
PASSING_PERCENTAGE = 60


class Student:
    def __init__(
        self,
        name,
        roll_number,
        math_marks,
        science_marks,
        english_marks,
    ):
        self.name = " ".join(name.split()).title()
        self.roll_number = roll_number.strip().upper()
        self.math_marks = math_marks
        self.science_marks = science_marks
        self.english_marks = english_marks

    def marks_are_valid(self):
        return (
            0 <= self.math_marks <= 100
            and 0 <= self.science_marks <= 100
            and 0 <= self.english_marks <= 100
        )

    def calculate_total(self):
        return self.math_marks + self.science_marks + self.english_marks

    def calculate_percentage(self):
        return self.calculate_total() / 3

    def calculate_grade(self):
        percentage = self.calculate_percentage()

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

    def has_failed_subject(self):
        return (
            self.math_marks < PASSING_MARKS
            or self.science_marks < PASSING_MARKS
            or self.english_marks < PASSING_MARKS
        )

    def get_result_status(self):
        if (
            self.calculate_percentage() >= PASSING_PERCENTAGE
            and not self.has_failed_subject()
        ):
            return "PASSED"

        return "FAILED"

    def print_report(self):
        if not self.marks_are_valid():
            print(f"\n{self.name}: invalid marks; report cannot be calculated.")
            return

        print("\n" + "=" * 46)
        print("                STUDENT REPORT              ")
        print("=" * 46)
        print(f"Student:       {self.name}")
        print(f"Roll number:   {self.roll_number}")
        print(f"Mathematics:   {self.math_marks:.1f}")
        print(f"Science:       {self.science_marks:.1f}")
        print(f"English:       {self.english_marks:.1f}")
        print("-" * 46)
        print(f"Total marks:   {self.calculate_total():.1f} / 300")
        print(f"Percentage:    {self.calculate_percentage():.2f}%")
        print(f"Grade:         {self.calculate_grade()}")
        print(f"Status:        {self.get_result_status()}")
        print("=" * 46)


print("\n==============================================")
print("         OOP STUDENT RESULT SYSTEM            ")
print("==============================================\n")

students = []
student_count = int(input("How many students do you want to enter? "))

for student_number in range(1, student_count + 1):
    print(f"\n--- Student {student_number} ---")

    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    math_marks = float(input("Enter Mathematics marks: "))
    science_marks = float(input("Enter Science marks: "))
    english_marks = float(input("Enter English marks: "))

    student = Student(
        name,
        roll_number,
        math_marks,
        science_marks,
        english_marks,
    )
    students.append(student)

print("\n--- All Student Reports ---")

for student in students:
    student.print_report()
