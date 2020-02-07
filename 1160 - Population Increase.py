x = int(input())
c = 0
while c<x:
    yc = 0
    p1, p2, g1, g2 = list(float(i) for i in input().split(" "))
    while p1 <= p2:
        p1 += ((p1*g1)//100)
        p2 += ((p2*g2)//100)
        yc += 1
        if yc>100:
            print("Mais de 1 seculo.")
            break

    if yc <= 100:
        print(yc, "anos.")
    c += 1