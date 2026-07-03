# Multiplication Table
# Uses a for loop and range() to repeat a calculation.

print("\n==========================================")
print("           MULTIPLICATION TABLE           ")
print("==========================================\n")

number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    result = number * multiplier
    print(f"{number} x {multiplier:2} = {result}")
