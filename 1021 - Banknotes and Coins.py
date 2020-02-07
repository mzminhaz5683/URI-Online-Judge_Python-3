# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

N = round(float(input()), 2)
tk = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
status = "nota(s)"
print("NOTAS:")
if (0 <= N <= 1000000.00):
    for i in tk:
        j = (N*100)//(i*100)
        N = round(N%i, 2)
        if i == 1:
            print("MOEDAS:")
            status = "moeda(s)"
        print("{0} {1} de R$ {2:.2f}".format(int(j), status, i))
