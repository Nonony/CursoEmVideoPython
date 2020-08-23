"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma
mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais"""

num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num > num2:
    print('O número {} é maior que o número {}'.format(num, num2))
elif num < num2:
    print('O número {} é menor que o número {}'.format(num, num2))
else:
    print('Os dois números são iguais!')
print('Fim!')
