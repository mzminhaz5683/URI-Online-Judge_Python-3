j = 1
sum = 0
for i in range(1, 40, 2):
    sum += (i/j)
    j = j*2
print("{0:.2f}".format(round(sum, 2)))