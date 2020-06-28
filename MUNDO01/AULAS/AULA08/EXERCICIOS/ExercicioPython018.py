# Escreva um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
# desse angulo

import math
angulo = float(input('Informe o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
print('O Seno do ângulo {:.0f}° é: {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O cosseno do ângulo {:.0f}° é: {:.2f}.'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('A tangente do ângulo {:.0f}° é: {:.2f}.'.format(angulo, tangente))
