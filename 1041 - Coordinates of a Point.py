list = input().split(" ")
x, y = float(list[0]), float(list[1])

if (x == 0.0 and y == 0.0):
    print("Origem")
elif (x == 0.0 and y != 0.0):
    print("Eixo Y")
elif (y == 0.0 and x != 0.0):
    print("Eixo X")

elif (x > 0.0):
   if (y > 0.0):
       print("Q1")
   else:
       print("Q4")

else :
    if (y > 0.0):
        print("Q2")
    else:
        print("Q3")