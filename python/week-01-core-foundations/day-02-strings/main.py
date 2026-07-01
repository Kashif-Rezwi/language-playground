# Day 02: Strings & Manipulation
# Topic: string methods, indexing, slicing, and f-strings

language = "python"
learning_goal = "  learning string methods, indexing, slicing, and f-strings  "

# Print first character of the language
print("First character:", language[0])

# Print last character of the language
print("Last character:", language[-1])

# Print first three characters of the language
print("First three characters:", language[:3])

# Print from index two onward of the language
print("From index two onward:", language[2:])

# Remove leading and trailing spaces from learning goal and print in title case
clean_title = language.title()
clean_goal = learning_goal.strip()

# Use f-string to print the language and learning goal together
print(f"Today I am practicing {clean_title} focus on {clean_goal}")

# Strip spaces, convert to lowercase, and replace internal spaces with underscores
full_name = input("Enter your full name: ")
username = full_name.strip().lower().replace(" ", "_")

# Suggest email based on first name and last name
first_name, last_name = username.split("_")
suggested_email = f"{first_name}{last_name}850@gmail.com"
print(f"Suggested email: {suggested_email}")

# Find the domain name from the email address
email = input("Enter your email address: ").strip().lower()
index_at = email.find("@")

# Extract the full domain after the @ symbol
domain = email[index_at + 1:] if index_at != -1 else "missing-domain"
print(f"Your email domain is: {domain}")

# Ask for a sentence and replace restricted words with asterisks (*)
sentence = input("Enter a sentence: ")
censored_sentence = sentence.replace("bad", "***").replace("error", "*****")
print(f"Censored message: {censored_sentence}")
