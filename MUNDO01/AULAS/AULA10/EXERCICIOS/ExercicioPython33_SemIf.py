"""Exercício Python 33:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))
maxvalue = max(num1, num2, num3)
minvalue = min(num1, num2, num3)
print('O maior valor digitado é: {}'.format(maxvalue))
print('O menor valor digitado é: {}'.format(minvalue))
