x = int(input())
f1 = 0
f2 = 1
if 0<x<46:
    for i in range(1, x + 1):

        if i < x:
            print(f1, end=" ")
        else:
            print(f1)
        f2, f1 = f1, f1 + f2
        