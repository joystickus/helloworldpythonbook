def postAddress(userInput):
    print("Here's your address:")
    print(name)
    print(zipcode, street)
    print(city, country)

name = input("Your full name: ")
country = input("The country you live in: ")
city = input("The city or town you live in: ")
street = input("Your address in the city or town: ")
zipcode = input("Zip or postal code: ")
userInput = [name, country, city, street, zipcode]

postAddress(userInput)
