sd = input("").split(" ")
sdate =int(sd[1])
list1 = input().split(" : ")
sh, sm, ss = int(list1[0]), int(list1[1]), int(list1[2])

ed = input("").split(" ")
edate =int(ed[1])
list2 = input().split(" : ")
eh, em, es = int(list2[0]), int(list2[1]), int(list2[2])

d = (edate - sdate)-1
sts = (24*60*60)-(sh*60*60 + sm*60 + ss)
ets = (eh*60*60 + em*60 + es)

ts = sts + (d*24*60*60) + ets

fs = ts%60
tm = ts//60
fm = tm%60
th = tm//60
fh = th%24
td = th//24


print("{0} dia(s)\n{1} hora(s)\n{2} minuto(s)\n{3} segundo(s)".format(td, fh, fm, fs))