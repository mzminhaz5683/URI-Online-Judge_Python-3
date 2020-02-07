N = int(input())
list = []
flag = 0

for i in range(0, N):
    list.append(int(input()))

"""
import csv
fl = open("+.py", "r")
asa = csv.reader(fl, delimiter = "\n")
for i in asa:
    list.append(int(i[0]))

fl.close()
"""

for x in list:

    if (x != 0):
        if (x%2 != 0):
            if (flag):
                print(" ", end="")
            print("ODD", end="")
            flag = 1

        if (x%2 == 0):
            if (flag):
                print(" ", end="")
            print("EVEN", end="")
            flag = 1

        if (x < 0):
            if (flag):
                print(" ", end="")
            print("NEGATIVE", end="")
            flag = 1

        if (x > 0):
            if (flag):
                print(" ", end="")
            print("POSITIVE", end="")
            flag = 1


    elif (x == 0):
        print("NULL", end="")

    print("")
    flag = 0