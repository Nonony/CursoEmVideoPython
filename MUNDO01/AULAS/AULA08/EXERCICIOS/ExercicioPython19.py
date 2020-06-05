# Escreva um programa que Leia o nome de quatro pessoas e escolha aleatoriamente um deles e escreva
# seu nome na tela

import random
nome = ['Carlos', 'Felipe', 'Marcos', 'Rogério', 'Rony']
escolha = random.choice(nome)
print('Parabéns {}, você é o escolhido!'.format(escolha))
