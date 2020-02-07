inp = input().split(" ")
x, y = int(inp[0]), int(inp[1])
i = 1
if (1 < x < 20 and x < y < 100000):
    while i <= y:
        for j in range(1, x+1):
            if j != x:
                print(i, end=" ")
            else:
                print(i)
            i += 1