N = int(input())
while (N > 0):
    inp = input().split(" ")
    x, y = int(inp[0]), int(inp[1])
    if (y == 0):
        print("divisao impossivel")
    else:
        x = round(x / y, 1)
        print(x)
    N -= 1
