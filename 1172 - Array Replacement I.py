X = []
c = 0
while c<10:
    a = int(input())
    if 0 < a:
        X.append(a)
    else:
        X.append(1)
    c += 1

s = 0
while s < len(X):
    print("X[{0}] = {1}".format(s, X[s]))
    s += 1