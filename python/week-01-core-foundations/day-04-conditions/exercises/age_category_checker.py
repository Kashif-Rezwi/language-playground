# Age Category Checker
# Uses conditions to classify an age into a simple life-stage category.

print("\n==========================================")
print("          AGE CATEGORY CHECKER            ")
print("==========================================\n")

age = int(input("Enter age: "))

if age < 0:
    category = "Invalid"
    message = "Age cannot be negative."
elif age < 13:
    category = "Child"
    message = "Category selected: child."
elif age < 18:
    category = "Teen"
    message = "Category selected: teen."
elif age < 40:
    category = "Adult"
    message = "Category selected: adult."
else:
    category = "Senior"
    message = "Category selected: senior."

print(f"Age: {age}")
print(f"Category: {category}")
print(message)
