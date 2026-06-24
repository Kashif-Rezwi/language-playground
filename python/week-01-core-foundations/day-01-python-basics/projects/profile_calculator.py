# =========================================================================
# Mini-Project: Day 1 Profile + Calculator Script
# Combines user profile inputs with a study schedule projection calculator.
# =========================================================================

print("==========================================")
print("     DEVELOPER STUDY PROFILE GENERATOR    ")
print("==========================================\n")

# Get user name and goal
name = input("Enter your name: ")
goal = input("Enter your goal: ")

# Get daily and weekly goals
days_per_week_input = input("How many days per week will you study: ")
hours_per_day_input = input("How many hours per day: ")
weekly_target_input = input("What is your weekly target hours: ")

# Type casting for numerical inputs
days_per_week = int(days_per_week_input)
hours_to_study = int(hours_per_day_input)
weekly_target = int(weekly_target_input)

# Perform calculations
weekly_study_hours = days_per_week * hours_to_study
remaining_hours = weekly_target - weekly_study_hours

# Target is achieved if remaining hours are less than or equal to 0
is_target_achieved = remaining_hours <= 0

# Ensure remaining hours display doesn't show negative values (caps at 0)
remaining_hours_display = max(0, remaining_hours)

# print formatted output
print(f"\nHello {name},")
print(f"Based on your input:")
print(f"Weekly hours to study: {weekly_study_hours}")
print(f"Remaining hours needed: {remaining_hours_display}")
print(f"Target status: {'Achieved' if is_target_achieved else 'Pending'}")