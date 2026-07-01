# ==================================================================================
# CSV Data Parser - Takes a single comma-separated string from the user,
# splits the data, casts each item to its correct type, and performs calculations.
# Result format: Name: Kashif, Age: 27, Balance (with 10% interest): INR 137500.0, Active: True
# ==================================================================================

# Get inputs from user
raw_csv_data = input("Enter record (Name, Age, Balance, IsActive): ")

# 1. Split the string by comma
name_raw, age_raw, balance_raw, active_raw = raw_csv_data.split(",")

# 2. Strip surrounding whitespaces and cast types
name = name_raw.strip()
age = int(age_raw.strip())
balance = float(balance_raw.strip())
is_active = active_raw.strip().lower() == "true"

# 3. Perform calculations using the casted values
interest_rate = 10
balance_plus_interest = balance * (1 + interest_rate / 100)

# 4. Display results matching the required format
print(f"Name: {name}, Age: {age}, Balance (with {interest_rate}% interest): INR {balance_plus_interest:.2f}, Active: {is_active}")
