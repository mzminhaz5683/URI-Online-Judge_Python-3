while True:
    y = int(input())
    if y == 0:
        break
    for j in range(1, y+1):
        if j != y:
            print(j, end=" ")
        else:
            print(j)