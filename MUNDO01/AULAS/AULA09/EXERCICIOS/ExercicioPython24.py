"""Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”."""

cidade = str(input('Informa o nome de uma cidade: ')).strip().lower()
divcid = cidade.split()
print('O nome da cidade começa com "SANTO"? {}'.format('santo' in divcid[0]))
