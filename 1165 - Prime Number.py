x = int(input())
c = 0
while c<x:
    flag = 1
    a = int(input())
    for i in range(2, a):
        if a%i == 0:
            flag = 0
            break

    if flag :
        print(a, "eh primo")
    else:
        print(a, "nao eh primo")
    c += 1