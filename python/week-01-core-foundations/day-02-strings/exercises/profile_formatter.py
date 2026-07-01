# ==================================================================================
# Profile Formatter - Gathers messy user profile inputs and cleans, aligns,
# and formats them into a clean, visually aligned text profile card.
# Result format: A boxed profile card with aligned labels and title-cased values.
# ==================================================================================

# Get raw, unformatted inputs from the user (simulating copy-paste errors)
print("Enter your profile details (extra spaces and mixed casing are fine):")
raw_name = input("Enter full name: ")
raw_age = input("Enter age: ")
raw_profession = input("Enter profession: ")
raw_city = input("Enter city: ")
raw_country = input("Enter country: ")

# Clean and format each field using string methods
name = raw_name.strip().title()
age = raw_age.strip()
profession = raw_profession.strip().title()
city = raw_city.strip().title()
country = raw_country.strip().title()

# Extract initials from name (e.g., "Kashif Rezwi" -> "KR")
name_parts = name.split()
first_initials = name_parts[0][0]
last_initials = name_parts[-1][0]
initials = f"{first_initials}{last_initials}"

# Print formatted profile card
print("\n" + "=" * 45)
print(f"| {name.upper() + ' (ID)':^41} |")
print("=" * 45)
print(f"| Name:      {name:<30} |")
print(f"| Initials:  {initials:<30} |")
print(f"| Age:       {age:<30} |")
print(f"| Profession: {profession:<30} |")
print(f"| City:      {city:<30} |")
print(f"| Country:   {country:<30} |")
print("=" * 45)