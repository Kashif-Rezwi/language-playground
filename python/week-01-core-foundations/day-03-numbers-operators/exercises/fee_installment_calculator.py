# Fee Installment Calculator
# Splits a total course fee into equal installments.

print("\n==========================================")
print("        FEE INSTALLMENT CALCULATOR        ")
print("==========================================\n")

total_fee = float(input("Enter total course fee: "))
installment_count = int(input("Enter number of installments: "))

amount_per_installment = total_fee / installment_count
remainder_check = total_fee % installment_count

print("\n--- Installment Summary ---")
print(f"Total fee: INR {total_fee:.2f}")
print(f"Installments: {installment_count}")
print(f"Amount per installment: INR {amount_per_installment:.2f}")
print(f"Remainder check using %: {remainder_check:.2f}")
