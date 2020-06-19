numLines = int(input('How many lines of stars do you want? '))
numStars = int(input('How many stars per line? '))
for line in range(numLines):
    for star in range(numStars):
        print('* ', end='')
    print()
