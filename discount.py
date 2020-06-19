print("Hello!")
purchases = float(input("What is the total cost of your purchases? "))
if purchases <= 10:
    print("You have a 10% discount and you need to pay only", purchases*0.9, "dollars!")
else:
    print("You have a 20% discount and you need to pay only", purchases*0.8, "dollars!")
