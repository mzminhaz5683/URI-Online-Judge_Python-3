while True:
    inp = input().split(" ")
    x, y = int(inp[0]), int(inp[1])
    if (x == 0 or y == 0):
        break
    elif (x > 0 and y > 0):
        print("primeiro")
    elif (x < 0 and y > 0):
        print("segundo")
    elif (x < 0 and y < 0):
        print("terceiro")
    elif (x > 0 and y < 0):
        print("quarto")