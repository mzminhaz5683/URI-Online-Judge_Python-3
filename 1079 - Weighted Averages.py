n = int(input())

for i in range(0, n):
    list = input().split(" ")
    a, b, c = round(float(list[0]), 1), round(float(list[1]), 1), round(float(list[2]), 1)
    w = (a*2 + b*3 + c*5)/10
    print(round(w, 1))