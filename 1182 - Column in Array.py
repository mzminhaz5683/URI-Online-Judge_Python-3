import re
x = []
sum = a = az= 0
flag = 0
p, q = int(input()), input()
for i in range(0, 12):
    x.append([])
    if az == 0:
        az = input()
    try:
        int(flag)
        for j in range(0, 12):
            y = float(az)
            x[i].insert(j, y)
            az = input()

    except:
        flag = 'a'
        lst = list(int(k) for k in re.findall(r'(-?\d+)', az))
        for j in lst:
            x[i].append(j)
        az = 0


"""              
    for i in x:
        print(i)
"""

for i in range(0, 12):
    sum += x[i][p]

if q == 'S':
    print("{0:.1f}".format(round(sum, 1)))
elif q == 'M':
    print("{0:.1f}".format(round(sum/12, 1)))