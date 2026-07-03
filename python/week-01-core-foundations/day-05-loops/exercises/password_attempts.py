# Password Attempts
# Gives the user three attempts and stops early when the password is correct.

print("\n==========================================")
print("             PASSWORD ATTEMPTS            ")
print("==========================================\n")

correct_password = input("Enter password: ")
max_attempts = int(input("Enter number of attempts: "))

for attempt_number in range(1, max_attempts + 1):
    password = input(f"Attempt {attempt_number}/{max_attempts} - Enter password: ")

    if password == correct_password:
        print("Login successful.")
        break

    remaining_attempts = max_attempts - attempt_number

    if remaining_attempts > 0:
        print(f"Incorrect password. Attempts left: {remaining_attempts}")
    else:
        print("Login failed. No attempts left.")
