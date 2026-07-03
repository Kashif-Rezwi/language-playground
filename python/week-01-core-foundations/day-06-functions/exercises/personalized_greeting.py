# Personalized Greeting
# Uses parameters to create reusable welcome messages.


def greet_student(name, course):
    clean_name = name.strip().title()
    clean_course = course.strip().title()
    print(f"Hello, {clean_name}! Welcome to {clean_course}.")


print("\n==========================================")
print("           PERSONALIZED GREETING          ")
print("==========================================\n")

student_name = input("Enter student name: ")
course_name = input("Enter course name: ")

greet_student(student_name, course_name)
