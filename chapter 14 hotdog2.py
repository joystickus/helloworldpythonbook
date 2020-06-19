class Meat:
    def __init__(self, name):
        self.name = name
        self.cooked_level = 0
        self.cooked_string = "Raw"
    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"
    def cut(self, direction):
        pass
        # put code here to cut along or across
class HotDog(Meat):
    def __init__(self):
        Meat.__init__(self, "hotDog")
        self.condiments = []
    def __str__(self):
        msg = "hot dog"
        lastCondiment = ""
        wordAndBeforeLastCondiment = ""
        if len(self.condiments) > 0:
            msg = msg + " with "
            lastCondiment = self.condiments.pop()
            wordAndBeforeLastCondiment = " and "
        for i in self.condiments:
            msg = msg+i+", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + wordAndBeforeLastCondiment + lastCondiment + "."
        return msg
    def addCondiments(self, condiment):
        self.condiments.append(condiment)

myDog = HotDog()
print(myDog)
print()
print("Now I'm going to cook the hot dog for 4 minutes.")
myDog.cook(4)
print()
print(myDog)
print()
print("Now I'm going to add some mustard, ketchup and cheese on my hot dog.")
myDog.addCondiments("mustard")
myDog.addCondiments("ketchup")
myDog.addCondiments("cheese")
print()
print(myDog)









'''
class HotDog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = "Raw"
        self.condiments = []
    def __str__(self):
        msg = "hot dog"
        lastCondiment = ""
        wordAndBeforeLastCondiment = ""
        if len(self.condiments) > 0:
            msg = msg + " with "
            lastCondiment = self.condiments.pop() # this is my addition to the lesson
            wordAndBeforeLastCondiment = " and " # and this one too
        for i in self.condiments:
            msg = msg+i+", "
        msg = msg.strip(", ")
        msg = self.cooked_string + " " + msg + wordAndBeforeLastCondiment + lastCondiment + "."
        # I added those two additional variables to the line above so that the whole message looks
        # nicer, like "...one, two, three AND four."
        return msg
    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = "Charcoal"
        elif self.cooked_level > 5:
            self.cooked_string = "Well-done"
        elif self.cooked_level > 3:
            self.cooked_string = "Medium"
        else:
            self.cooked_string = "Raw"
    def addCondiment(self, condiment):
        self.condiments.append(condiment)
myDog = HotDog()
print(myDog)
print("Cooking hot dog for 4 minutes...")
myDog.cook(4)
print(myDog)
print("Cooking hot dog for 3 more minutes...")
myDog.cook(3)
print(myDog)
print("What happens if I cook it for 10 more minutes?")
myDog.cook(10)
print(myDog)
print("Now, I'm going to add some stuff on my hot dog")
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")
myDog.addCondiment("cheese")
print(myDog)
'''


'''
that part was for the beginning of the lesson

myDog = HotDog()
print(myDog.cooked_level)
print(myDog.cooked_string)
print(myDog.condiments)

print("Now I'm going to cook the hot dog")
myDog.cook(4)
print(myDog.cooked_level)
print(myDog.cooked_string)
'''
