list = []
for i in range(0, 5):
    list.append(float(input()))

counter = 0
for i in list:
    if (i%2 == 0):
        counter += 1


print("{0} valores pares".format(counter))