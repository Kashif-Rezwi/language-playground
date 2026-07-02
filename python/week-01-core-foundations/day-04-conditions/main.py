# Day 04: Conditions & Control Flow
# Topic: if/elif/else, comparison operators, logical operators, and validation

score = int(input("Enter the score: "))

if score >= 40:
    print("Result: Passed")
else:
    print("Result: Failed")

percentage = int(input("Enter the percentage: "))

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

print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")

marks = int(input("Enter marks: "))

if marks >= 0 and marks <= 100:
    print("Marks status: Valid")
else:
    print("Marks status: Invalid")

continue_answer = "y"

if continue_answer == "yes" or continue_answer == "y":
    print("Decision: Continue learning")
else:
    print("Decision: Pause")
