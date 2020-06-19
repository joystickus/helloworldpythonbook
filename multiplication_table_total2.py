for j in range(2, 10):
    i = 2
    for i in range(2, 10):
        print(j, "x", i, "=", j*i)
        if i == 9 and j != 9:
            print("----------")
        elif i == 9 and j == 9:
            break
