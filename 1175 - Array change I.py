X = []
c = 1
while c<=20:
    a = int(input())
    X.append(a)
    c += 1

i =0
j = 1
while i != 10:
    X[i], X[(j*-1)] = X[(j*-1)], X[i]
    i += 1
    j += 1
s = 0
while s < len(X):
    print("N[{0}] = {1}".format(s, X[s]))
    s += 1