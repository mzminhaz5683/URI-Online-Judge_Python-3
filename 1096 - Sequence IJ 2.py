j = 7
i = 1
while (i < 10):
    print("I={0} J={1}".format(i, j))
    if (j == 5):
        j = 7
        i += 2
        continue
    j -= 1