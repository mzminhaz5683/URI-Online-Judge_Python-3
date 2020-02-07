list = []
for i in range(0, 6):
    list.append(float(input()))

counter = sum = 0
for i in list:
    if (0 <= i):
        sum += i
        counter += 1


print("{0} valores positivos\n{1:.1f}".format(counter, round(sum/counter, 1)))