x = int(input())
while x != 0:
    sum = i = 0
    while i < 5:
        if x % 2 == 0:
            sum += x
            i += 1
        x += 1
    print(sum)
    x = int(input())