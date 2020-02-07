x = int(input())
c = 0
while c<x:
    sum = 0
    a = int(input())
    for i in range(1, a):
        if a%i == 0:
            sum += i

    if sum == a:
        print(a, "eh perfeito")
    else:
        print(a, "nao eh perfeito")
    c += 1