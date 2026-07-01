# Marks Percentage Calculator
# Calculates total marks and percentage for three subjects.

print("\n==========================================")
print("        MARKS PERCENTAGE CALCULATOR       ")
print("==========================================\n")

math_marks = float(input("Enter Mathematics marks: "))
science_marks = float(input("Enter Science marks: "))
english_marks = float(input("Enter English marks: "))

total_marks = math_marks + science_marks + english_marks
percentage = total_marks / 3

print("\n--- Result Summary ---")
print(f"Mathematics: {math_marks:.1f} / 100")
print(f"Science:     {science_marks:.1f} / 100")
print(f"English:     {english_marks:.1f} / 100")
print(f"Total Marks: {total_marks:.1f} / 300")
print(f"Percentage:  {percentage:.2f}%")
