j = 7
i = 1
while (i < 10):
    jp = j
    for k in range(0, 3):
        print("I={0} J={1}".format(i, j))
        j -= 1

    j = jp + 2
    i += 2