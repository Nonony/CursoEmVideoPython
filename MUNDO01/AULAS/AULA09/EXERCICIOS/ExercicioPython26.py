"""Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra “A”,
Em que posição ela aparece a primeira vez
Em que posição ela aparece a última vez."""

frase = str(input('Digite uma frase qualquer: ')).strip().lower()
print('A quantidade de letras "a" na frase é: {}'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na frase na posição: {}'.format(frase.find('a')))
print('A letra "a" aparece pela última vez na frase na posição: {}'.format(frase.rfind('a')))
