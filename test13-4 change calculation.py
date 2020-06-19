def changeCalcucaltion(userInput):
    total = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    return total

quarters = int(input("quarters: "))
dimes = int(input("dimes: "))
nickels = int(input("nickels: "))
pennies = int(input("pennies: "))
userInput = [quarters, dimes, nickels, pennies]

print("total is $", changeCalcucaltion(userInput))
