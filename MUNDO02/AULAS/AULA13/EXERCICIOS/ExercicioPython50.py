"""Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o."""

soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite o {}º numero: '.format(n)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Você informou {} números PARES e a soma entre eles é {}'.format(cont, soma))
