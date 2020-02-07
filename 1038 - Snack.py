list = input().split(" ")
X, Y = int(list[0]), int(list[1])

dec = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

for i in dec:
    if X == i:
        print("Total: R$ {0:.2f}".format(dec[i]*Y))
        break