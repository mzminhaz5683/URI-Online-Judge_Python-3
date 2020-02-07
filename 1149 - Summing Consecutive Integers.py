while True:
    inp = list(filter(lambda a : a>0, list(int(i) for i in input().split(" "))))
    x, y = inp[0], inp[1]
    sum = 0
    for i in range(0, y):
        sum += x
        x += 1
    print(sum)
    break