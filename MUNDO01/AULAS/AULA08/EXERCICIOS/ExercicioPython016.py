# Escreva um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex: Digite um Número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(num, trunc(num)))
# Obtendo a parte inteira de um número sem utilizar o módulo math
print('O número {} tem a parte inteira {}.'.format(num, int(num)))
