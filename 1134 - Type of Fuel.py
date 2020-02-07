a = g = d = 0
print("MUITO OBRIGADO")
while True:
    x = int(input())
    if x == 4:
        print("Alcool: {0}\nGasolina: {1}\nDiesel: {2}".format(a, g, d))
        break
    elif x == 3:
        d += 1
    elif x == 2:
        g += 1
    elif x == 1:
        a += 1
