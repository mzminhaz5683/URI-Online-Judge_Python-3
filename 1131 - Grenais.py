c = e = i = g = 0
while True:
    c += 1
    inp = input().split(" ")
    ci, cg = int(inp[0]), int(inp[1])
    T = int(input("Novo grenal (1-sim 2-nao)\n"))
    if (ci == cg):
        e += 1
    elif (ci > cg):
        i += 1
    elif (ci < cg):
        g += 1

    if (T == 1):
        continue
    elif (T == 2):
        print("{0} grenais\nInter:{1}\nGremio:{2}\nEmpates:{3}\nInter venceu mais".format(c, i, g, e))
        break
