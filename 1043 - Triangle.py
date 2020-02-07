list = input().split(" ")
a, b, c = float(list[0]), float(list[1]),float(list[2])

if (a < b + c and b < a + c and c < a + b):
    print("Perimetro = {0}".format(round((a + b + c), 1)))
else:
    print("Area = {0}".format(round((c * (a + b) / 2), 1)))