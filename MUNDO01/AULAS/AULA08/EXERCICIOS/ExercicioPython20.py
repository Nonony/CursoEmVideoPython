# Escreva um programa em Python que leia uma lista de nomes e os mostre aleatoreamente na tela.

import random
nome = ['Carlos', 'Felipe', 'Marcos', 'Rogério', 'Rony']
lista = random.shuffle(nome)
print('A ordem dos nomes ficou assim: {}'.format(nome))
