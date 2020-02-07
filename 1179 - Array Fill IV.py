j = k = 0
E = []
O = []

for i in range(0, 15):
    n = int(input())
    if n%2 == 0:
        E.insert(j, n)
        j += 1
        if j == 5:
            for i in range(0, 5):
                print("par[{0}] = {1}".format(i, E[i]))
            E[:] = []
            j = 0
    else:
        O.insert(k, n)
        k += 1
        if k == 5:
            for i in range(0, 5):
                print("impar[{0}] = {1}".format(i, O[i]))
            O[:] = []
            k = 0

for i in range(0, len(O)):
    print("impar[{0}] = {1}".format(i, O[i]))

for i in range(0, len(E)):
    print("par[{0}] = {1}".format(i, E[i]))