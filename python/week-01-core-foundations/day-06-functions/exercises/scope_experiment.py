# Scope Experiment
# Demonstrates the difference between global and local variables.

passing_marks = 40


def show_passing_marks():
    passing_marks = 50

    print("\nInside the function:")
    print(f"Local passing marks: {passing_marks}")


print("\n==========================================")
print("              SCOPE EXPERIMENT            ")
print("==========================================")

show_passing_marks()

print("\nOutside the function:")
print(f"Global passing marks: {passing_marks}")

# The local value is used inside show_passing_marks().
# The global value remains unchanged outside the function.
# A local variable exists only while its function is running.
