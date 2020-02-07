list = []
for i in range(1, 101):
    list.append(int(input()))

counter = 1
max = list[1]
for i in range(1, 100):
    if (max < list[i]):
        max = list[i]
        counter = i+1

print("{0}\n{1}".format(max, counter))