userinput = int(input("Which multiplication table would you like? "))
userinput2 = int(input("How high do you want to go? "))
for i in range(1, userinput2+1):
    print(userinput, "x", i, "=", userinput*i)
