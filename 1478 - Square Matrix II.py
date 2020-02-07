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

for a in x:
    mid = int(math.floor(a/2))
    c = 0
    for i in range(0, a):
        p = i+1
        z = iz = 0
        flag = 0
       # print("  ", end="")
        for j in range(0, a):
            if p < 10:
                z = 2
                iz = 1
            elif 10 <= p < 100:
                z = 1
                iz = 0
            elif 100 <= p < 1000:
                z = 0
                iz = -1
            if j == a-1 and j != 0:
                print(" "*z,p, end="")
            elif j != 0:
                print(" "*z,p, end="")
            elif j == 0 and iz >= 0:
                print(" "*iz,p, end="")
            elif iz < 0:
                print(p, end="")

            # main work start
            if p == 1:
                flag = 1

            if p < a and flag == 1:
                p += 1
            else:
                p -= 1
            # main work End

        print("")
    print("")