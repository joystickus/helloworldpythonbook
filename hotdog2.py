dog_cal = 140
bun_cal = 120
mus_cal = 20
ket_cal = 80
onion_cal = 40

print("\tDog\tBun \tKetchup\tMustard\tOnions\tCalories")
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    tot_cal = ((dog * dog_cal) + (bun * bun * bun_cal) +
                               (mustard * mus_cal) + (ketchup * ket_cal) +
                               (onion * onion_cal))
                    print("#", count, "\t", end='')
                    print(dog, "\t", bun, "\t", ketchup, "\t", end='')
                    print(mustard, "\t", onion, end='')
                    print("\t", tot_cal)
                    count = count + 1
