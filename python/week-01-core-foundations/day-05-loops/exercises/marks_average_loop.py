# Marks Average Loop
# Collects marks for multiple subjects using a loop and calculates the average.

print("\n==========================================")
print("            MARKS AVERAGE LOOP            ")
print("==========================================\n")

subject_count = int(input("Enter number of subjects: "))
total_marks = 0
valid_subjects = 0

for subject_number in range(1, subject_count + 1):
    marks = float(input(f"Enter marks for subject {subject_number}: "))

    if marks < 0 or marks > 100:
        print("Invalid marks skipped. Marks must be between 0 and 100.")
        continue

    total_marks = total_marks + marks
    valid_subjects = valid_subjects + 1

if valid_subjects == 0:
    print("No valid marks were entered.")
else:
    average_marks = total_marks / valid_subjects

    print("\n--- Marks Summary ---")
    print(f"Valid subjects: {valid_subjects}")
    print(f"Total marks: {total_marks:.1f}")
    print(f"Average marks: {average_marks:.2f}")
