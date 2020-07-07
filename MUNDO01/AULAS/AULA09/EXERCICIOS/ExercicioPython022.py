"""Crie um programa em python que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Total de caracteres da frase (sem considerar espaços)
Quantas letras tem o primeiro nome.
"""
import time
nome = str(input('Digite seu nome completo: '))
print('Analisando o nome informado...')
time.sleep(2)
print('Seu nome em letras maiúsculas fica assim: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas fica assim: {}'.format(nome.lower()))
print('O total de letras no nome em contar espaços é: {}'.format(len(nome.replace(' ', ''))))
div = nome.split()
# print(div[1])
print('O primeiro nome tem um total de {} letras'. format(len(div[0])))
