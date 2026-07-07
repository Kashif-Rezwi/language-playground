# Bank Account
# Protects balance changes with validation and masks the account number.


class BankAccount:
    def __init__(self, account_holder, account_number, opening_balance):
        self.account_holder = " ".join(account_holder.split()).title()
        self.account_number = account_number.strip()
        self.balance = opening_balance

    def deposit(self, amount):
        if amount <= 0:
            return {
                "status": "FAILED",
                "message": "Invalid deposit amount."
            }
        
        self.balance = self.balance + amount
        return {
            "status": "SUCCESS",
            "message": f"Deposit of INR {amount} successful. New balance: INR {self.balance}",
            "balance": self.balance,
            "deposited_amount": amount
        }

    def withdraw(self, amount):
        if amount <= 0:
            return {
                "status": "FAILED",
                "message": "Invalid withdrawal amount."
            }
        elif amount > self.balance:
            return { 
                "status": "FAILED",
                "message": "Insufficient balance."
            }
        else:
            self.balance = self.balance - amount
            return {
                "status": "SUCCESS",
                "message": f"Withdrawal of INR {amount} successful. Remaining balance: INR {self.balance}",
                "balance": self.balance,
                "withdrawn_amount": amount
            }
        

    def get_balance(self):
        return {
            "status": "SUCCESS",
            "balance": self.balance
        }

    def get_masked_account_number(self):
        last_four_digits = self.account_number[-4:]
        masked_account_number = "*" * (len(self.account_number) - 4) + last_four_digits
        return masked_account_number

    def __str__(self):
        return (
            f"Account Holder: {self.account_holder}\n"
            f"Account Number: {self.get_masked_account_number()}\n"
            f"Balance: INR {self.balance:,.2f}"
        )


print("\n==========================================")
print("               BANK ACCOUNT               ")
print("==========================================\n")

my_account = BankAccount("kashif rezwi", "123456789012", 5000)
print(f"{my_account}\n")

# deposit 500 and print the message
deposit_result = my_account.deposit(500)
print(f"Transaction 1: {deposit_result['status']} - {deposit_result['message']}")

# withdraw 1500 and print the message
withdraw_result = my_account.withdraw(1500)
print(f"Transaction 2: {withdraw_result['status']} - {withdraw_result['message']}")

# withdraw 10000 and print the message
withdraw_result = my_account.withdraw(10000)
print(f"Transaction 3: {withdraw_result['status']} - {withdraw_result['message']}")

# print the final account details
print(f"\n{my_account}")
