N = int(input())
tk = [100, 50, 20, 10, 5, 2, 1]
print(N)
if (0 < N < 1000000):
    for i in tk:
        j = N//i
        N = N%i
        print("{0} nota(s) de R$ {1},00".format(j, i))
