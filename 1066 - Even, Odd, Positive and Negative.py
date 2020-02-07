list = []
for i in range(0, 5):
    list.append(float(input()))

ce = co = cp = cn = 0
for i in list:
    if (i%2 == 0):
        ce += 1
    if (i%2 != 0):
        co += 1

    if (0 < i):
        cp += 1
    if (0 > i):
        cn += 1

print("{0} valor(es) par(es)\n{1} valor(es) impar(es)\n{2} valor(es) positivo(s)\n{3} valor(es) negativo(s)".format(ce, co, cp, cn))