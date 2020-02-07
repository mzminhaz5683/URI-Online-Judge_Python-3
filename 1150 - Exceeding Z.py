flag = c = sum = 0
while True:
    x = int(input())
    if flag == 0:
        a = x
        flag = 1
    if (a < x):
        for i in range(a, x+1):
            c += 1
            sum += i
            if sum > x:
                flag = 2
                break

    if flag == 2:
        print(c)
        break