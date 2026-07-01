
# ==================================================================================
# Course Fee Split - Calculates the remaining balance of a course fee after a partial payment.
# Result format: Remaining Balance: 30000 INR
# ==================================================================================

# Get inputs from user
total_fee = int(input("Enter the total fee of the course: "))
partial_payment = int(input("Enter the partial payment amount: "))

# Calculate the remaining balance
remaining_balance = total_fee - partial_payment

# print the remaining balance
print(f"Remaining Balance: {remaining_balance} INR")