n = int(input())
dec = {}
for i in range(1, n+1):
    inp = input().split(' ')
    dec[i] = []
    dec[i].append(int(inp[0]))
    dec[i].append(int(inp[1]))

for j in dec.values():
    x = j[0]
    y = j[1]
    if (x > y):
        x, y = y, x

    sum = 0
    for i in range(x+1, y):
        if (i%2 != 0):
            sum += i
    j.append(sum)


for j in dec.values():
    print(j[-1])