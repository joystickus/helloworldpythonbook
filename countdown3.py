countdown = int(input("Countdown timer: How many seconds? "))
import time
for i in range(countdown, 0, -1):
    print(i, " ", end='')
    for j in range(i, 0, -1):
        print("* ", end='')
    print()
    time.sleep(1)
print("BLAST OFF!")
