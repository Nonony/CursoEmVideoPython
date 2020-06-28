# Escreva um programa que Leia o nome de quatro pessoas e escolha
# aleatoriamente um deles e escreva seu nome na tela

import random

nome1 = str(input('Informe o primeiro nome: '))
nome2 = str(input('Informe o segundo nome: '))
nome3 = str(input('Informe o terceiro nome: '))
nome4 = str(input('Informe o quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
print(lista)
escolha = random.choice(lista)
print('Parabéns {}, você é o escolhido!'.format(escolha))
