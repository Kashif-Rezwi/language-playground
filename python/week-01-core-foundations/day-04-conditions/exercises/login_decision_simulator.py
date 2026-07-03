# Login Decision Simulator
# Practices cleaned text comparison and logical `and`.

print("\n==========================================")
print("          LOGIN DECISION SIMULATOR        ")
print("==========================================\n")

username = input("Enter username: ").strip().lower()
password = input("Enter password: ")

if username == "" and password == "":
    print(f"Username and Password cannot be empty.")
elif username == "":
    print("Username cannot be empty.")
elif password == "":
    print("Password cannot be empty.")
elif username == "admin" and password == "python123":
    print("Login successful.")
else:
    print("Login failed. Check username or password.")
