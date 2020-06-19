class BankAccount:
    def __init__(self, name, number):
        self.name = str(name)
        self.number = int(number)
        self.balance = 0.0
    def showBalance(self):
        print("Your balance is", self.balance)
    def showAccount(self):
        print("The account belongs to " + name + ", it's number is " + str(number) + \
              " and the interest rate is " + str(rate*100) + "%.")
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Your balance now is", self.balance)
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance = self.balance - amount
            print("Your balance now is", self.balance)
        else:
            print("Your balance is too low for the operation. Your balance is", self.balance)
class InterestAccount(BankAccount):
    def __init__(self, name, number, rate):
        BankAccount.__init__(self, name, number)
        self.rate = rate
    def addInterest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

print("Hello! You need to create an account first.")
print()
name = input("Please enter your name: ")
import random
number = random.randint(111111, 999999)
rate = (random.randint(1, 100))/100

newAccount = InterestAccount(name, number, rate)

print("Thank you! The account is created. It belongs to " + name + ", it's number is " + str(number) + \
      " and the interest rate is " + str(rate*100) + "%.")

while True:
    userAnswer = input("""
What would you like to do next?
a - account details
b - check your balance
d - deposit
w - withdraw
i - add interest
q - quit
""")
    if userAnswer == "q":
        print("See you later!")
        break
    elif userAnswer == "a":
        newAccount.showAccount()
    elif userAnswer == "b":
        newAccount.showBalance()
    elif userAnswer == "i":
        newAccount.addInterest()
    elif userAnswer == "d":
        amount = float(input("How much would you like to deposit? - "))
        newAccount.deposit(amount)
    elif userAnswer == "w":
        amount = float(input("How much would you like to withdraw? - "))
        newAccount.withdraw(amount)
    else:
        print("I don't understand. Please try again.")
