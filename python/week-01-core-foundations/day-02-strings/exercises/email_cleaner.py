# ==================================================================================
# Email Cleaner & Parser - Sanitizes a raw email input, normalizes it,
# and extracts the local part, domain, and company/organization name.
# ==================================================================================

print("\n==========================================")
print("          EMAIL SANITIZER & PARSER        ")
print("==========================================\n")

# Get raw email input and clean up
raw_email = input("Enter your email address: ")
email = raw_email.strip().lower()

# Detect separator '@' position using find
at_index = email.find("@")

# Extract parts using slicing
username_part = email[: at_index-1] # or email[0:at_index-1]

# Extract domain part
domain = email[at_index + 1:] # or email[at_index + 1:-1]

# Find first dot
dot_index = domain.find(".")

# Slice out the organization name from domain
org_name = domain[:dot_index].title()

# 6. Print the parsed summary
print("\n" + "=" * 45)
print("               PARSED RESULT              ")
print("=" * 45)
print(f"Raw Input:       '{raw_email}'")
print(f"Sanitized Email: '{email}'")
print(f"Username:        '{username_part}'")
print(f"Full Domain:     '{domain}'")
print(f"Organization:    '{org_name}'")
print("=" * 45 + "\n")
