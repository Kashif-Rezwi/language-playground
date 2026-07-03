# Student Marks Collector
# Repeats student result entry until the user chooses to stop.

print("\n==========================================")
print("          STUDENT MARKS COLLECTOR         ")
print("==========================================\n")

student_count = 0
passed_count = 0
failed_count = 0
total_class_percentage = 0

while True:
    student_name = input("Enter student name: ").strip().title()
    math_marks = float(input("Enter Mathematics marks: "))
    science_marks = float(input("Enter Science marks: "))
    english_marks = float(input("Enter English marks: "))

    marks_are_valid = (
        0 <= math_marks <= 100
        and 0 <= science_marks <= 100
        and 0 <= english_marks <= 100
    )

    if not marks_are_valid:
        print("Invalid marks. Student skipped.")
    else:
        total_marks = math_marks + science_marks + english_marks
        percentage = total_marks / 3
        subject_failed = (
            math_marks < 40
            or science_marks < 40
            or english_marks < 40
        )
        status = "FAILED" if percentage < 60 or subject_failed else "PASSED"

        student_count = student_count + 1
        total_class_percentage = total_class_percentage + percentage

        if status == "PASSED":
            passed_count = passed_count + 1
        else:
            failed_count = failed_count + 1

        print("\n--- Student Summary ---")
        print(f"Student:    {student_name}")
        print(f"Total:      {total_marks:.1f} / 300")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Status:     {status}")

    continue_answer = input("\nAdd another student? yes/no: ").strip().lower()

    if continue_answer != "yes":
        break

print("\n" + "=" * 44)
print("             CLASS SUMMARY                ")
print("=" * 44)
print(f"Students processed: {student_count}")
print(f"Passed students:    {passed_count}")
print(f"Failed students:    {failed_count}")

if student_count > 0:
    class_average = total_class_percentage / student_count
    print(f"Class average:      {class_average:.2f}%")
else:
    print("Class average:      unavailable")

print("=" * 44)
