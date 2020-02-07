# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
N = float(input())
status = "Fora de intervalo"
if 0<= N <= 25:
    status = "Intervalo [0,25]"
elif 25< N <= 50:
    status = "Intervalo (25,50]"
elif 50< N <=75:
    status = "Intervalo (50,75]"
elif 75< N <=100:
    status = "Intervalo (75,100]"

print(status)