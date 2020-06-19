print("Hello!")
gender = input("What is your gender? (m/f) ")
if gender == "f":
    age = int(input("And how old are you? "))
    if 10 <= age <= 12:
        print("Welcome onboard!")
    elif age < 10:
        print("Sorry, you're too young!")
    else:
        print("Sorry, you're too old!")
else:
    print("Sorry, pal, it's for girls only!")
