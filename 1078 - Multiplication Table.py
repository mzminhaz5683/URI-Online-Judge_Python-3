n = int(input())

if (1 < n < 1000):
    for i in range(1, 11):
        print("{0} x {1} = {2}".format(i, n, i*n))