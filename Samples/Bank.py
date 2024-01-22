from Bank import BankAccount

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        # Initialize the attributes here
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, amount):
        # Implement deposit method here
         self.initial_balance += amount


    def withdraw(self, amount):
        # Implement withdraw method here
        if amount <= self.initial_balance:
            self.initial_balance -=  amount
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def get_balance(self):
        # Implement get_balance method here
        return self.initial_balance

    def __str__(self):
        # Implement __str__ method here
        return f"Account Holder: {self.account_holder}\nBalance: {self.initial_balance}"

    # Create an instance of BankAccount
account = BankAccount("John", 1000)
print(account)

# Perform some deposits and withdrawals 
account.deposit(500)
account.withdraw(200)
# Print the account information after each transaction
print(account)
