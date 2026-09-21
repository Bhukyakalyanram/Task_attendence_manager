class BankAccount:

    def __init__(self, account_number, balance, user):
        self.balance = balance
        self.user = user
        self.account_number = account_number

    def getbalance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "the amount is greater"
        else:
            self.balance = self.balance - amount
            return "the amount is withdrawal"

    def deposit(self, amount):
        if amount < 100:
            return "We cant deposit less than 100 amount"
        else:
            self.balance = self.balance + amount
            return "the amount is withdrawal"


account1 = BankAccount("123456", 5000, "Kalyan")

print(account1.account_number)
print(account1.balance)
print(account1.user)
