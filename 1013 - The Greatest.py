take2 = raw_input().split(' ')
a, b, c = int(take2[0]), int(take2[1]), int(take2[2])

maxab = ((a + b + abs(a - b)) // 2)
max = ((maxab + c + abs(maxab - c)) // 2)

print("{0} eh o maior".format(max))