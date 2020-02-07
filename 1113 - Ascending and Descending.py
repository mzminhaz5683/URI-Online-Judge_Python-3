while True:
    x = input().split(" ")
    if int(x[0]) == int(x[1]):
        break
    if int(x[0]) < int(x[1]):
        print("Crescente")
    else:
        print("Decrescente")