list = input().split(" ")
ao = [0, 0, 0]
x, y, z = int(list[0]), int(list[1]),int(list[2])


if (x <= y and x <= z):
    if (y <= z):
        ao[0], ao[1], ao[2] = x, y, z
    else:
        ao[0], ao[1], ao[2] = x, z, y

elif (y <= x and y <= z):
    if (x <= z):
        ao[0], ao[1], ao[2] = y, x, z
    else:
        ao[0], ao[1], ao[2] = y, z, x

elif (z <= x and z <= y):
    if (x <= y):
        ao[0], ao[1], ao[2] = z, x, y
    else:
        ao[0], ao[1], ao[2] = z, y, x

for i in ao:
    print(i)

print("\n{0}\n{1}\n{2}".format(x, y, z))