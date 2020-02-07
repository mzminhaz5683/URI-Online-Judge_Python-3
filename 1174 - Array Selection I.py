X = []
c = 1
while c<=100:
    a = float(input())
    X.append(round(a, 1))
    c += 1
s = 0
while s < len(X):
    if (X[s] <= 10):
        print("A[{0}] = {1:.1f}".format(s, X[s]))
    s += 1