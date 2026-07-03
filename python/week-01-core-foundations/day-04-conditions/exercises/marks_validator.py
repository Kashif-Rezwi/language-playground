# Marks Validator
# Validates a single subject score before deciding pass or fail.

print("\n==========================================")
print("              MARKS VALIDATOR             ")
print("==========================================\n")

marks = float(input("Enter subject marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks. Enter a value from 0 to 100.")
elif marks >= 40:
    print("Status: Passed")
else:
    print("Status: Failed")
