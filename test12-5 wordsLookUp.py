words = {}
while True:
    addOrLookUp = input("Add or look up a word? ('a' to add, 'l' to look up, 'q' to quit): ")
    if addOrLookUp == "a":
        wordToAdd = input("Type the word: ")
        definition = input("Type the definition: ")
        words[wordToAdd] = definition
        print("Word added!")
    elif addOrLookUp == "l":
        wordToLookUp = input("Type the word: ")
        if wordToLookUp in words:
            print(words[wordToLookUp])
        else:
            print("That word isn't in the dictionary yet.")
    elif addOrLookUp == "q":
        print("Goodbye!")
        break
    else:
        print("Are you dumb?")
