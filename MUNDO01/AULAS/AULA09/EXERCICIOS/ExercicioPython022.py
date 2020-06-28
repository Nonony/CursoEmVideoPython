"""Crie um programa em python que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Total de caracteres da frase (sem considerar espaços)
Quantas letras tem o primeiro nome
"""

nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print('O total de letras no nome é: {}'.format(len(nome.replace(' ', ''))))
div = nome.split()
# print(div[1])
print('O primeiro nome tem um total de {} letras'. format(len(div[0])))
