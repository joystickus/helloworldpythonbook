import easygui
easygui.msgbox("I'll ask you your mailing address")
name = easygui.enterbox("Please enter your full name")
country = easygui.enterbox("What country are you from?")
city = easygui.enterbox("What city are you from?")
street = easygui.enterbox("What street do you live in?")
building = easygui.enterbox("What is the number of your building?")
appartment = easygui.enterbox("What is the number of your appartment?")
zipcode = easygui.enterbox("And zipcode?")
easygui.msgbox("""So your address is:""" + "\n" + str(name) + "\n" + str(zipcode) + "\n" + str(street) + ", "+ str(building) + "-" + str(appartment) + "\n" + str(city) + ", " + str(country))

'''
# address.py
# Enter parts of your address and display the whole thing
import easygui
name = easygui.enterbox("What is your name?")
addr = easygui.enterbox("What is your street address?")
city = easygui.enterbox("What is your city?")
state = easygui.enterbox("What is your state or province?")
code = easygui.enterbox("What is your postal code or zip code?")
whole_addr = name + "\n" + addr + "\n" + city + ", " + state + "\n" + code
easygui.msgbox(whole_addr, "Here is your address:")
'''
