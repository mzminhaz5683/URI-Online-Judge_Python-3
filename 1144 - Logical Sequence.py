x = int(input())
i = j = k = flag = c = 1
while i <= x:
    if c%2 != 0:
        j = i*i
        k = i*i*i
    else:
        j = (i*i)+1
        k = (i*i*i)+1
    print("{0} {1} {2}".format(i, j, k))
    c += 1
    if flag == 0:
        i += 1
        flag = 1
    else:
        flag = 0