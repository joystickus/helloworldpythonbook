tanksize = int(input("How big is your gas tank, in liters? "))
percent = int(input("How full is your tank (in percent—for example, half full = 50)? "))
litersperkm = int(input("How many liters per 100 km does your car get? "))
percent = percent/100
liters = tanksize*percent-5
distance = liters*100/litersperkm
print("You have", liters, "liters (minus 5-liter buffer in case the fuel gauge isn’t accurate)")
print("You can go another", distance, "km")
print("The next gas station is 200 km away")
if distance > 200:
    print("You can wait for the next station.")
else:
    print("Get gas now!")
