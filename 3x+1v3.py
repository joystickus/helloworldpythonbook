steps = 0
tempvar = 0
print('''Hello! This is the game called 3x+1.
You pick any whole number and I calculate it.
The rules are simple: if the number is even, it's devided by 2,
and if it's odd it's multiplied by 3 and 1 is added.''')
number = int(input("Pick your number: "))
print(number)
while number != 1: 
    tempvar = number
    if number % 2 == 0:
        number = number / 2
        print(tempvar,": 2 =",number)
    else:
        number = number * 3 + 1
        print(tempvar,"* 3 + 1 =",number)
    steps = steps + 1
if number == 1:
    print("Total steps:",steps)
