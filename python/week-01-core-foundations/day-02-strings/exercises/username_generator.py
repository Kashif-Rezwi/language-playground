# ==================================================================================
# Username Generator - Standardizes user inputs into clean developer system
# credentials (usernames and handles) without using control flow.
# ==================================================================================

import student_name_normalizer
print("\n==========================================")
print("     SYSTEM CREDENTIALS GENERATOR        ")
print("==========================================\n")

# Get ra inputs (simulating casing & spacing variations)
raw_name = input("Enter your full name: ")
raw_birth_year = input("Enter your birth year (yyyy): ")
raw_favourite_language = input("Enter your favourite programming language: ")

# Clean and standardize inputs
clean_name = raw_name.strip()
clean_birth_year = raw_birth_year.strip()
clean_favourite_language = raw_favourite_language.strip()

# Calculations and string formatting
name_length = len(clean_name.replace(" ", "")) # remove internal spaces
name_parts = clean_name.split()
initials = (name_parts[0][0] + name_parts[-1][0]).upper()
standard_username = clean_name.lower().replace(" ", "_") + f"_{clean_birth_year}"

# developer handle: initials + favourite language acronym + number of characters in full name
developer_handle = f"{initials}_{clean_favourite_language.upper()}_{name_length}"

# Print out the credentials
print("\n" + "=" * 45)
print("         GENERATED CREDENTIALS            ")
print("=" * 45)
print(f"Standard Username:  {standard_username}")
print(f"Developer Handle:   {developer_handle}")
print("=" * 45 + "\n")