x = 0  # number of steps
a = 0  # temporary variable
print("Hello! This is the game called 3x+1.")
print("You pick any whole number and I calculate it.")
print("The rules are simple:")
print("if the number is even, it's devided by 2,")
print("and if it's odd it's multiplied by 3 and 1 is added.")
a = input("Shall we begin? (y/n)")
if a == "y":

    n = int(input("Pick your number: "))  # main variable for calculations
    # start listing every step
    print(n)
    # cycle of calculations
    while n != 1:
        a = n  # store the initial number
        if n % 2 == 0:  # check if the number is even
            n = n / 2  # devide it by 2
            print(a, ": 2 =", n)  # show the result
        else:  # if the number is odd
            n = n * 3 + 1  # multiply it by 3 and add 1
            print(a, "* 3 + 1 =", n)  # show the result
        x = x + 1  # add one step
    if n == 1:  # the final point
        print("Total steps:", x)  # show the number of steps
    elif a == "n":
        print("Suit yourself.")
    else:
        print("I don't get it. Can you just say y or n?")
