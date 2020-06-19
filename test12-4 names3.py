names = []
print("Enter 5 names")
for i in range(5):
    names.append(input())
print("The names are:", names)
nameToReplace = int(input("Replace one name. Which one? (1-5): "))
names[nameToReplace-1] = input("New name: ")
print("Now the names are:", names)
