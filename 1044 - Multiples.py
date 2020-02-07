list = input().split(" ")
a, b = int(list[0]), int(list[1])

if a > b:
    a, b = b, a

if b%a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
