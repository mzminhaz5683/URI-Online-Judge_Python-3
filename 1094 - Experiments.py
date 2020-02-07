dec = {}
n = int(input())
total = counter = 0
for i in range(0, n):
    x = input().split(" ")
    try:
        dec[x[1]].append(int(x[0]))
    except:
        dec[x[1]] = []
        dec[x[1]].append(int(x[0]))

for a, b in dec.items():
    temp = 0
    for i in b:
        temp += i
    dec[a] = temp

for a, b in dec.items():
    total += b
    counter += 1

print("Total: {0} cobaias".format(total))
print("Total de coelhos: {0}".format(dec["C"]))
print("Total de ratos: {0}".format(dec["R"]))
print("Total de sapos: {0}".format(dec["S"]))
print("Percentual de coelhos: {0:.2f} %".format(round((dec["C"]/total)*100, 2)))
print("Percentual de ratos: {0:.2f} %".format(round((dec["R"]/total)*100, 2)))
print("Percentual de sapos: {0:.2f} %".format(round((dec["S"]/total)*100, 2)))

