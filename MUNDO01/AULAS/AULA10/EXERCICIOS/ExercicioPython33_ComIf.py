"""Exercício Python 33:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
# Testando o menor valor
minvalue = a
if b < a and b < c:
    minvalue = b
if c < a and c < b:
    minvalue = c
# Testando o maior valor
maxvalue = a
if b > a and b > c:
    maxvalue = b
if c > a and c > b:
    maxvalue = c
print('O menor valor digitado foi {}'.format(minvalue))
print('O maior valor digitado foi {}'.format(maxvalue))
