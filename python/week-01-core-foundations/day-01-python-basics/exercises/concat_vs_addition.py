# ==================================================================================
# Data Type Confusion - Demonstrates string concatenation vs. mathematical addition
# using explicit type casting.
# Result format: String Concatenation: 1020, Mathematical Addition: 30
# ==================================================================================

# Get inputs from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# string concatenation
num1 = str(num1)
num2 = str(num2)
concat_result = num1 + num2

# mathematical addition
num1 = int(num1)
num2 = int(num2)
add_result = num1 + num2

print(f"String Concatenation: {concat_result}, Mathematical Addition: {add_result}")
