# Skip Invalid Marks
# Uses continue to ignore invalid marks while processing valid ones.

print("\n==========================================")
print("             SKIP INVALID MARKS           ")
print("==========================================\n")

valid_count = 0
invalid_count = 0
total_marks = 0

total_entries = int(input("Enter number of entries: "))

for entry_number in range(1, total_entries + 1):
    marks = float(input(f"Enter marks entry {entry_number}: "))

    if marks < 0 or marks > 100:
        invalid_count = invalid_count + 1
        print("Invalid marks skipped.")
        continue

    valid_count = valid_count + 1
    total_marks = total_marks + marks

print("\n--- Validation Summary ---")
print(f"Valid entries: {valid_count}")
print(f"Invalid entries: {invalid_count}")

if valid_count > 0:
    average_marks = total_marks / valid_count
    print(f"Average valid marks: {average_marks:.2f}")
else:
    print("Average valid marks: unavailable")
