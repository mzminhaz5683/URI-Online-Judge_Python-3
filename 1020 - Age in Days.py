N = int(input())

y = N//365
N = N%365
m = N//30
d = N%30

print("{0} ano(s)\n{1} mes(es)\n{2} dia(s)".format(y, m, d))