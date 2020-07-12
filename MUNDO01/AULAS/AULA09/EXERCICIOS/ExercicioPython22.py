"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

nome = str(input('Informe seu nome completo: ')).strip()
divnome = nome.split()
nospace = nome.replace(' ', '')
print('Convertendo o nome para letras maiúsculas: {}'.format(nome.upper()))
print('Convertento o nome para letras minúsculas: {}'.format(nome.lower()))
totCar = len(nospace)
print('O total de letras no nome é {}'.format(totCar))
print('O total de letras do primeiro nome é igual a: {}'.format(len(divnome[0])))
