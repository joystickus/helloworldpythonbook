print('''Hello! This is the game called 3x+1.
You pick any whole number and I calculate it.
The rules are simple:
if the number is even, it's devided by 2,
and if it's odd it's multiplied by 3 and 1 is added.
The game ends once calculations reach 1 because it leads to the loop "1-4-2-1"
Shall we play? (y/n)''')
while True:
    steps = 0
    useranswer = input()
    if useranswer == "n":
        print("Suit yourself.")
        break
    elif useranswer == "y":
        number = int(input("Ok then. Pick your number: "))
        while number != 1:
            prenumber = number
            if number % 2 == 0:
                number = int(number / 2)
                print( prenumber , ": 2 =" , number )
            else:
                number = int(number * 3 + 1)
                print( prenumber ,"* 3 + 1 =", number )
            steps += 1
        if number == 1:
            print("Total steps:", steps , ". Would you like to play again? (y/n)" )
    else:
        print("I don't get it. Can you just say 'y' or 'n'?")
