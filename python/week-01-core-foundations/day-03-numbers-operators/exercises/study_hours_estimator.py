# Study Hours Estimator
# Estimates total study time and weekly average from daily practice inputs.

print("\n==========================================")
print("          STUDY HOURS ESTIMATOR           ")
print("==========================================\n")

study_days = int(input("Enter total study days: "))
hours_per_day = float(input("Enter average hours per day: "))

total_hours = study_days * hours_per_day
weekly_average = total_hours / 7

print("\n--- Study Estimate ---")
print(f"Study days: {study_days}")
print(f"Hours per day: {hours_per_day:.2f}")
print(f"Total hours: {total_hours:.2f}")
print(f"Weekly average: {weekly_average:.2f} hours")
