import easygui
Ftemperature = easygui.integerbox("Temperature in Fahrenheit: ", upperbound=1000)
Ctemperature = int((5 / 9 * (Ftemperature - 32)) + 0.5)
easygui.msgbox("Approximate temperature in Celsius is " + str(Ctemperature))
