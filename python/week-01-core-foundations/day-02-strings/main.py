# Day 02: Strings & Manipulation
# Topic: string methods, indexing, slicing, and f-strings

language = "python"
learning_goal = "  learning string methods, indexing, slicing, and f-strings  "

# Print first character of the langauge
print("First character:", language[0])

# Print last character of the langauge
print("Last character:", language[-1])

# Print first three characters of the langauge
print("First three characters:", language[:2])

# Print from index two onward of the langauge
print("From index two onward:", language[1:])

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

# find the domain name from the email address
email = input("Enter you email address: ")
index_at = email.find('@')
index_dot = email.rfind('.', index_at, len(email))

# Extract the domain using index_at and last index_dot from email
domain = email[index_at+1:index_dot]
print(f"Your email domain is: {domain}")

# Ask for a sentence and replace a "restriced" word with asteriks (*)
sentence = input("Enter a sentence: ")
censored_sentence = sentence.replace("bad", "***").replace("error", "*****")
print(f"Censored message: {censored_sentence}")