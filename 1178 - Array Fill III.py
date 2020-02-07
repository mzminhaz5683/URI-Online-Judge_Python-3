N = []
j = float(input())
i = 0
while i<100:
    N.insert(i, round(j, 4))
    j = j/2
    i += 1
c= 0
for i in N:
    print("N[{0}] = {1:.4f}".format(c, i))
    c += 1
