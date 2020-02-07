# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
take1 = raw_input().split(' ')
take2 = raw_input().split(' ')
code1, unit1, price1 = int(take1[0]), int(take1[1]), float(take1[2])
code2, unit2, price2 = int(take2[0]), int(take2[1]), float(take2[2])

t1 = unit1*price1
t2 = unit2*price2


print("VALOR A PAGAR: R$ {0:.2f}".format(t1+t2))