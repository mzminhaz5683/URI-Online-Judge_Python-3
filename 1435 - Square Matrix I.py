import re, math
x = []
while True:
    y = input()
    try:
        if int(y) == 0:
            break
        x.append(int(y))
    except:
        lst = list(int(k) for k in re.findall(r'(-?\d+)', y))
        for i in lst:
            if i == 0:
                break
            x.append(i)
        break

flag = load = 0
for a in x:
    mid = int(math.floor(a/2))
    c = 0
    for i in range(0, a):
        p = 1
        z = 0
        print("  ", end="")
        for j in range(0, a):
            if p < 10:
                z = 2
            elif 10 <= p < 100:
                z = 1
            elif 100 <= p < 1000:
                z = 0

            if j == a-1 and j != 0:
                print(" "*z,p, end="")
            elif j != 0:
                print(" "*z,p, end="")
            elif j == 0:
                print(p, end="")

            # main work start
                                                        # i/j 0 1 2 3 4 5 6     p = 1
            if i< mid:                                  # 0 = 1 1 1 1 1 1 1
                c = i                                   # 1 = 1 2 2 2 2 2 1     p!=1 & j>=(a-1)-i
            else:                                       # 2 = 1 2 3 3 3 2 1         p -= 1
                c = a-1-i                               # 3 = 1 2 3 4 3 2 1     p <= i
                                                    #   4(2)= 1 2 3 3 3 2 1         p += 1
            if (p != 1) and (j >= (a-1-c)):         #   5(1)= 1 2 2 2 2 2 1
                p -= 1                              #   6(0)= 1 1 1 1 1 1 1
            elif (p <= c):
                p += 1

            # main work End

        print("")
    print("")