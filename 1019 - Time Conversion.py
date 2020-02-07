N = int(input())

s = N%60
N = N//60
m = N%60
h = N//60

print("{0}:{1}:{2}".format(h, m, s))