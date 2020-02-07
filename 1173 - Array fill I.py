a = int(input())
X = []
c = i= 1
while c<=10:
        X.append(a*i)
        i *= 2
        c += 1
s = 0
while s < len(X):
    print("N[{0}] = {1}".format(s, X[s]))
    s += 1