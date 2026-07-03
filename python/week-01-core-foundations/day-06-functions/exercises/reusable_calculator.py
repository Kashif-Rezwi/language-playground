# Reusable Calculator
# Uses separate functions that return arithmetic results.


def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def multiply(number_1, number_2):
    return number_1 * number_2


def divide(number_1, number_2):
    if number_2 == 0:
        return "Cannot divide by zero."

    return number_1 / number_2


print("\n==========================================")
print("            REUSABLE CALCULATOR           ")
print("==========================================\n")

first_number = float(input("Enter first number: "))
operator = input("Choose +, -, *, or /: ").strip()
second_number = float(input("Enter second number: "))

if operator == "+":
    result = add(first_number, second_number)
elif operator == "-":
    result = subtract(first_number, second_number)
elif operator == "*":
    result = multiply(first_number, second_number)
elif operator == "/":
    result = divide(first_number, second_number)
else:
    result = "Unknown operator."

print(f"Result: {result}")
