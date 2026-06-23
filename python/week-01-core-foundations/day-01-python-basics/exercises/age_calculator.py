
# ========================================================================
# Age Calculator - Calculate the user's age based on their date of birth.
# Result format: Age: 27 years, 2 months, 4 days
# ========================================================================

# Get inputs from user
date_of_birth = input("Enter your date of birth in yyyy-mm-dd format: ")
current_date = input("Enter the current date in yyyy-mm-dd format: ")

# Split the date strings
birth_year_str, birth_month_str, birth_day_str = date_of_birth.split('-')
current_year_str, current_month_str, current_day_str = current_date.split('-')

# Convert string inputs to integers for calculation
birth_year = int(birth_year_str)
birth_month = int(birth_month_str)
birth_day = int(birth_day_str)

current_year = int(current_year_str)
current_month = int(current_month_str)
current_day = int(current_day_str)

# 1. Convert dates to approximate total days (assuming 365 days/year and 30 days/month)
birth_total_days = (birth_year * 365) + (birth_month * 30) + birth_day
current_total_days = (current_year * 365) + (current_month * 30) + current_day

# 2. Calculate the difference in total days
total_days = current_total_days - birth_total_days

# 3. Convert total days back to years, months, and days
# // finds the quotient (floor division), % finds the remainder (modulo)
age_years = total_days // 365
remaining_days = total_days % 365

age_month = remaining_days // 30
age_day = remaining_days % 30

print(f"Age: {age_years} years, {age_month} months, {age_day} days")