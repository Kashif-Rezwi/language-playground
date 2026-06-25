# Day 01: Python Basics & Variables
# Topic: Print statement, variables, basic data types, input, type casting, simple calculations

# Print Hello World
print("Hello World")

# Store user name using variables
user_name = "Kashif Rezwi"
greeting = "Hello, "

# Concatenate variables and print
print(greeting + user_name)

# Better approach for printing multiple variables using f-string
print(f"{greeting}{user_name}")

# Basic data types
name = "Kashif Rezwi"       # str
age = 27                    # int
height = 6.0                # float
is_learning = True          # bool

print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))

# Input from user
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
is_learning_input = input("Are you learning Python? True/False: ")
is_learning = is_learning_input.strip().lower() == "true"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Learning Python: {is_learning}")

# Type casting - string to integer, float, and boolean
course_fee = "118500"
course_fee_integer = int(course_fee)
course_fee_float = float(course_fee)

print(f"Course Fee as string: {course_fee}, Type: {type(course_fee)}")
print(f"Course Fee as integer: {course_fee_integer}, Type: {type(course_fee_integer)}")
print(f"Course Fee as float: {course_fee_float}, Type: {type(course_fee_float)}")
print(f"Learning Python as boolean: {is_learning}, Type: {type(is_learning)}")

# Study Session Tracker - calculate the total study hours logged.

# Get inputs from user (all inputs start as strings)
days_input = input("Enter number of study days: ")
hours_per_day_input = input("Enter average study hours per day: ")

# Type cast the inputs to appropriate types
# Days must be a whole number
days = int(days_input)

# Hours per day can be a decimal
hours_per_day = float(hours_per_day_input)

# Perform calculations
total_study_hours = days * hours_per_day

# Print results using clean formatting
print("\n--- Progress Summary ---")
print(f"Total days active: {days} days (Type: {type(days).__name__})")
print(f"Hours per day: {hours_per_day} hrs (Type: {type(hours_per_day).__name__})")
print(f"Total study time: {total_study_hours} hours")
