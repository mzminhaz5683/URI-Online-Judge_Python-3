N = []
x = int(input())
i = 0
while i<1000:
    for j in range(0, x):
        if i >= 1000:
            break
        N.insert(i, j)
        i += 1
c= 0
for i in N:
    print("N[{0}] = {1}".format(c, i))
    c += 1
