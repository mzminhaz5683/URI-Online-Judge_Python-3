N = int(input())
mul = 1
if 0 < N < 13:
    for i in range(0, N):
        mul *=(N-i)

    print(mul)