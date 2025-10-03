class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
        self.amount= 0

    def deposit(self, amount):
        self.amount = amount
        self.account_balance += self.amount
        return self.account_balance

    def withdraw(self, amount):
        self.amount = self.amount
        if amount > self.account_balance:
            print("insufficient funds.")
            return self.account_balance
        else:
            self.account_balance += self.amount
            return self.account_balance
             

    def display_balance(self):
        print(f"Your current balance is {self.account_balance}") 
           
