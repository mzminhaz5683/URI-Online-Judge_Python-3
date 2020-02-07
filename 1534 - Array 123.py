import re
x = []
while True:
    try:
        y = input()
        if y == '':
            break
        try:
            x.append(int(y))
        except:
            lst = list(int(k) for k in re.findall(r'(-?\d+)', y))
            for i in lst:
                x.append(i)

    except EOFError:
        break

for i_array in x:
    for i in range(1, i_array+1):
      for j in range(1, i_array+1):
        common_v = 3

        if j == ((i_array+1)-i):
          common_v = 2
        elif j == i:
          common_v = 1

        print(common_v, end="")
      print("")