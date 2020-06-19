class BankAccount:
    def __init__(self, name, accountNumber):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = 0.0
    def showBalance(self):
        print("Your balance is", self.balance)
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Thank you! Your balance now is", self.balance)
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Thank you! Your balance now is", self.balance)
        else:
            print("I'm sorry, you don't have enough money. Your balance is", self.balance)
class InterestAccount(BankAccount):
    def __init__(self, name, accountNumber, rate):
        BankAccount.__init__(self, name, accountNumber)
        self.rate = rate
    def addInterest(self):
        interest = self.balance * self.rate
        print("adding interest to the account,", self.rate * 100, "percent")
        self.deposit (interest)
        




myAccount = InterestAccount("Dmitry Nasyrov", 112233445566, 0.11)
print("Account name:", myAccount.name)
print("Account number:", myAccount.accountNumber)
myAccount.showBalance()
myAccount.deposit(34.52)
myAccount.addInterest()
