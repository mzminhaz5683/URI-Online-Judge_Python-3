N = int(input())
cIn = cOut =0

for i in range(0, N):
    X = int(input())
    if (10 <= X <= 20):
        cIn += 1
    else:
        cOut += 1


print("{} in\n{} out".format(cIn, cOut))