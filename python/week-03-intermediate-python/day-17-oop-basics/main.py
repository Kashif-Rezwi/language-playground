# Day 17: Object-Oriented Programming Basics
# Topic: classes, objects, __init__, self, instance attributes, and methods

# class - blueprint
class LearningProfile:
    pass # pass is a placeholder for an empty class

# object - instance created from the class
profile_one = LearningProfile()
profile_one.name = "Kashif"
profile_one.completed_days = 6

profile_two = LearningProfile()
profile_two.name = "Thamizh"
profile_two.completed_days = 0


print("\n --- Basic Class and Object ---")
print(f"Learner: {profile_one.name}")
print(f"Completed days: {profile_one.completed_days}")
print(f"Learner: {profile_two.name}")
print(f"Completed days: {profile_two.completed_days}")


# class with constructor and attributes
class Course:
    # initialize attributes: __init__ is a constructor and is called automatically when an object is created
    # self is a reference to the current object
    def __init__(self, title, total_days, completed_days=0):
        self.title = title
        self.total_days = total_days
        self.completed_days = completed_days

    # instance methods - take 'self' (the current object) to access its attributes.
    # python automatically passes 'self' when the method is called.
    
    # returns the remaining days
    def calculate_remaining_days(self):
        return self.total_days - self.completed_days

    # complete a day (increase the completed_days by 1)
    def complete_day(self):
        if self.completed_days < self.total_days:
            self.completed_days = self.completed_days + 1

    # show the progress
    def show_progress(self):
        remaining_days = self.calculate_remaining_days()

        print(f"Course: {self.title}")
        print(f"Completed: {self.completed_days}/{self.total_days}")
        print(f"Remaining: {remaining_days} days")

python_course = Course("Python Learning Playground", 30, 6)

print("\n--- Constuctor, Attributes, and Methods ---")
python_course.show_progress()

# log complete another day
python_course.complete_day()

print("\n After adding another completed day by calling complete_day() method")
python_course.show_progress()

# creating another course - each object keeps its own instance attributes
oop_course = Course("OOP Basics", 2, 1)
data_course = Course("NumPy Basics", 3)

print("\n --- Multiple Independent Objects ---")
print("\n --- OOP Course ---")
oop_course.show_progress()
print("\n --- Data Course ---")
data_course.show_progress()

print("\n --- Complete one more day of OOP ---")
oop_course.complete_day()

print("\n After completing one more day of OOP:")
oop_course.show_progress()

PASSING_MARKS = 40
PASSING_PERCENTAGE = 60

class Student:
    def __init__(self, name, roll_number, math_marks, science_marks, english_marks):
        self.name = name
        self.roll_number = roll_number
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
            print(f"{self.name}: invalid marks, report cannot be calculated.")
            return
        
        total_marks = self.calculate_total()
        percentage = self.calculate_percentage()
        grade = self.calculate_grade()
        status = self.get_result_status()

        print("\n" + "=" * 46)
        print("               STUDENT REPORT              ")
        print("=" * 46)
        print(f"Student:       {self.name}")
        print(f"Roll number:   {self.roll_number}")
        print(f"Mathematics:   {self.math_marks:.1f}")
        print(f"Science:       {self.science_marks:.1f}")
        print(f"English:       {self.english_marks:.1f}")
        print("-" * 46)
        print(f"Total marks:   {total_marks:.1f} / 300")
        print(f"Percentage:    {percentage:.2f}%")
        print(f"Grade:         {grade}")
        print(f"Status:        {status}")
        print("=" * 46)


# Create Student objects
student_1 = Student("kashif rezwi", "py-017", 85, 90, 78)
student_2 = Student("Meera Sharma", "py-018", 92, 88, 95)

# Test print_report
print("\n--- OOP Student Result System ---")
student_1.print_report()
student_2.print_report()

# Test with invalid marks
student_3 = Student("Invalid Test", "inv-001", -5, 80, 90)
student_3.print_report()