"""Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é
PAR ou ÍMPAR.
Para saber se um número é par ou impar divida-o por 2. Se o resto da divisão for 0 o número é PAR,
senão é IMPAR
"""

num = int(input('Informe um número: '))
validacao = num % 2
if validacao == 0:
    print('O número {} é PAR.'.format(num))
else:
    print('O número {} é IMPAR.'.format(num))
print('FIM!')
