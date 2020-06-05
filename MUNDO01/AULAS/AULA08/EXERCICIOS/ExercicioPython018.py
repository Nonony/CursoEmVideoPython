# Escreva um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse angulo

import math
angulo = float(input('Informe o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
print(seno)
coseno = math.cos(math.radians(angulo))
print(coseno)
tangente = math.tan(math.radians(angulo))
print(tangente)
