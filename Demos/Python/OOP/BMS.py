class BankAccount:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("\nAccount Number :", self.account_no)
        print("Account Holder :", self.holder_name)
        print("Current Balance:", self.balance)


# Creating bank account object
account1 = BankAccount(123456, "Amit Patel", 10000)

account1.display_balance()

# Deposit money
account1.deposit(5000)

# Withdraw money
account1.withdraw(3000)

# Display final balance
account1.display_balance()