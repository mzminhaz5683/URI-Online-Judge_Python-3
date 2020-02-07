x = int(input())
c = 1
for i in range(1, x+1):
    print("{0} {1} {2}".format(c, c*c, c*c*c))
    c += 1