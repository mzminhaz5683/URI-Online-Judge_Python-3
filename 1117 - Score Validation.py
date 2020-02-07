y = ''
while True:
    x = round(float(input()), 2)
    if (x < 0.00 or x > 10.00):
        print("nota invalida")
        continue
    try :
        print("media = {0:.2f}".format(round((x+y)/2, 2)))
        break
    except:
        y = x
        continue