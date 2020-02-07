def asa():
    y = ''
    while True:
        x = round(float(input()), 2)
        if (x < 0.00 or x > 10.00):
            print("nota invalida")
            continue
        try :
            print("media = {0:.2f}".format(round((x+y)/2, 2)))
            while True:
                print("novo calculo (1-sim 2-nao)")
                T = int(input())
                if (T == 1):
                    asa()
                    return
                elif (T == 2):
                    return
        except:
            y = x
            continue

x = asa()