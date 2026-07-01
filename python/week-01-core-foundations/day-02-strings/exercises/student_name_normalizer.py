# ==================================================================================
# Student Name Normalizer - Cleans messy name strings with duplicate spaces and
# irregular casings, and exports them into standard university database formats.
# ==================================================================================

print("\n==========================================")
print("          STUDENT NAME NORMALIZER         ")
print("==========================================\n")

# Get raw input
raw_name = input("Enter student's full name: ")

# Clean casing and remove duplicate internal spaces
clean_name = " ".join(raw_name.split()).title()

# Extract parts - first, last and middle names
name_parts = clean_name.split()
first_name = name_parts[0] if name_parts else "Unknown"
last_name = name_parts[-1] if name_parts else "Student"

# Join any remaining elements in the middle
middle_name = " ".join(name_parts[1:-1])

# Generate standardized database formats - LASTNAME, FIRSTNAME MIDDLENAME
standardized_name = f"{last_name.upper()}, {first_name} {middle_name}".strip()

# System username: lowercase "first.last" (e.g., mohammad.asif)
system_username = f"{first_name.lower()}.{last_name.lower()}"

# Profile username: lowercase "last_first.txt" (e.g., rezwi_mohammad.txt)
profile_filename = f"{last_name.lower()}_{first_name.lower()}.txt"

# Print the formatting dashboard
print("\n" + "=" * 45)
print("             NORMALIZATION REPORT         ")
print("=" * 45)
print(f"Original Input:   '{raw_name}'")
print(f"Normalized Name:  '{clean_name}'")
print("-" * 45)
print(f"Official Name:  {standardized_name}")
print(f"System Username:  {system_username}")
print(f"Profile Filename: {profile_filename}")
print("=" * 45 + "\n")
