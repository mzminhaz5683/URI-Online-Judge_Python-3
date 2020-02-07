import math
take1 = raw_input().split(' ')
take2 = raw_input().split(' ')
x1, y1 = float("{0:.1f}".format(float(take1[0]))), float("{0:.1f}".format(float(take1[1])))
x2, y2 = float("{0:.1f}".format(float(take2[0]))), float("{0:.1f}".format(float(take2[1])))

p1 = x2 - x1
p2 = y2 - y1
distance = math.sqrt((p1 * p1) + (p2 * p2))

print("{0:.4f}".format(distance))

