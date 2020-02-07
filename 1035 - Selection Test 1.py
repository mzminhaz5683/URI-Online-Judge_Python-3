list = input().split(" ")
A, B, C, D = int(list[0]), int(list[1]), int(list[2]), int(list[3])

if B>C and D>A and (C+D)>(A+B) and C>=0 and D>=0 and A%2==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")