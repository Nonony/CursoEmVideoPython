"""Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome."""

nome = str(input('Digite um nome: ')).strip().lower()
print('O nome informado possui "SILVA"? {}'.format('silva' in nome))
