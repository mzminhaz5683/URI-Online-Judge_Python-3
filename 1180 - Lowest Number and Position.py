import re
b = []
i = 0

x = int(input())
while i<x:
    y = input()
    for j in list(k for k in re.findall(r'(-?\d+)', y)):
        b.append(int(j))                                         #['1 21 3', '4 5 36', '72 1 11']
    i = len(b)


j = 1
min = b[0]
loc = 0
while j < len(b):
    if b[j] < min:
        min = b[j]
        loc = j
    j += 1

print("Menor valor: {0}\nPosicao: {1}".format(min, loc))