x = 0
a = 0
print('''Hello! This is the game called 3x+1.
You pick any whole number and I calculate it.
The rules are simple:
if the number is even, it's devided by 2,
and if it's odd it's multiplied by 3 and 1 is added.''')
a = input("Shall we begin? (y/n): ")
if a == "y":
    n = int(input("Pick your number: "))
    print(n)
    while n != 1: 
        a = n
        if n % 2 == 0:
            n = n / 2
            print(a,": 2 =",n)
        else:
            n = n * 3 + 1
            print(a,"* 3 + 1 =",n)
        x = x + 1
        if n == 1:
            print("Total steps:",x)
elif a == "n":
    print("Suit yourself.")
else:
    print("I don't get it. Can you just say 'y' or 'n'?")
    
