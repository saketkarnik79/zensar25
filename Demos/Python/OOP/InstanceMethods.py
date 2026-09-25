class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print(f"Account: {self.account_number}")
        print(f"Balance: {self.balance}")

account = BankAccount("ACC1001", 5000)
account.deposit(2000)
account.display_balance()