N = []
N.insert(0, 0)
N.insert(1, 1)
for i in range(2, 61):
    load = N[i-1]+N[i-2]
    N.insert(i, load)

x = int(input())
for i in range(0, x):
    y = int(input())
    if 0<= y <= 60:
        print("Fib({0}) = {1}".format(y, N[y]))
