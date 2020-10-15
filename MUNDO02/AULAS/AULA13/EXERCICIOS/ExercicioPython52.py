"""Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

num = int(input('Digite um número: '))
div1 = []
ndiv = '\33['
for i in range(1, num + 1 ):
    if num % i == 0:
        div1.append(i)
        contador = len(div1)
        print('\033[34m', end = '')
    else:
        print('\033[m', end = '')
    print('{} \033[m'.format(i), end = '')
if contador > 2:
    print('\nO número {} foi divisível {} vezes.'.format(num, len(div1)))
    print('Por isso ele não é um número primo!')
else:
    print('\nO número {} foi divisível {} vezes.'.format(num, len(div1)))
    print('Por isso ele é um número primo!')
