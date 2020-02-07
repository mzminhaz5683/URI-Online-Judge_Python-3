x = int(input())
for i in range(0, x):
    x, y = list(int(i) for i in input().split(" "))
    sum = i = 0
    while i<y:
        if x%2 != 0:
            sum += x
            i += 1
        x += 1
    print(sum)