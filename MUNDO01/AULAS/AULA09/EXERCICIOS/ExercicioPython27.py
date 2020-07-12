"""Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa.
Mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input('Digite um nome completo: ')).strip()
divnome = nome.split()
print('Olá {}!'.format(nome))
print('Seu primeiro nome é: {}'.format(divnome[0]))
print('O seu útimo nome é: {}'.format(divnome[len(divnome) - 1]))
