sum = c = 0
while True:
    x = int(input())
    if x >= 0:
        c += 1
        sum += x
    else:
        print("{0:.2f}".format(round(sum/c, 2)))
        break