x, y = int(input()), int(input())
sum = 0
if x > y:
    x, y = y, x

for i in range(x+1, y):
    if ((i)%2 != 0):
        sum += i


print(sum)