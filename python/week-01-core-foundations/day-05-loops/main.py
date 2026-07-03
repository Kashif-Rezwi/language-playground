# Day 05: Loops & Iterables
# Topic: for loops, while loops, range, counters, accumulators, break, continue

# For loop with range
for number in range(1, 10):
    print(f"Count: {number}")

# Accumulator example
total_marks = 0
total_subjects = int(input("Enter number of subjects: "))

for subject_number in range(1, total_subjects + 1):
    marks = float(input(f"Enter marks for subject {subject_number}: "))
    total_marks = total_marks + marks

average_marks = total_marks / total_subjects

print(f"Total marks: {total_marks:.1f} / {total_subjects * 100}")
print(f"Average marks: {average_marks:.2f}")


# Counter example
passed_count = 0
total_students = int(input("Enter number of students: "))

for student_number in range(1, total_students + 1):
    marks = float(input(f"Enter marks for student {student_number}: "))

    if marks >= 40:
        passed_count = passed_count + 1

print(f"Students passed: {passed_count}")


# While loop with break
while True:
    answer = input("Type 'yes' to practice or 'exit' to stop: ").strip().lower()

    if answer == "exit":
        print("Stopping loop.")
        break
    elif answer == "yes":
        print("Great. Keep practicing loops.")
        continue
    else:
        print("Unknown command. Try again.")
