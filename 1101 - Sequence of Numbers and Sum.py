dec = {}
i = 1
while True:
    inp = input().split(' ')
    x = int(inp[0])
    y = int(inp[1])
    if (x <= 0 or y <= 0 ):
        break
    dec[i] = []
    dec[i].append(x)
    dec[i].append(y)
    i += 1


for i in dec.values():
    x = i[0]
    y = i[1]
    if (x > y):
        x, y = y, x
    sum = 0
    for j in range(x, y+1):
        sum += j
        print(j, end=" ")
    print("Sum={0}".format(sum))
