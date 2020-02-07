# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
import math
list = input().split(" ")
A, B, C = float(list[0]), float(list[1]), float(list[2])

try:
    r1 = (-B + math.sqrt((B * B) - 4 * A * C)) / (2 * A)
    r2 = (-B - math.sqrt((B * B) - 4 * A * C)) / (2 * A)
    print("R1 = {0}\nR2 = {1}".format(round(r1, 5), round(r2, 5)))
except:
    print("Impossivel calcular")