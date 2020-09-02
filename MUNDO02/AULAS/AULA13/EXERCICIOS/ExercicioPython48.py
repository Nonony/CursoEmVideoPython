"""Exercício Python 48:
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo
de 1 até 500."""

print('Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram '
      'no intervalo de 1 até 500.\n')
contador = []
tam = 0
soma = 0
for c in range(1, 501):  # for c in range(1, 501, 2):
    if c % 2 != 0 and c % 3 == 0:  # if c % 3 == 0:
        contador.append(c)  # soma += c
        tam = len(contador)  # quant += 1
        soma = sum(contador)
print('A soma de todos os {} valores solicitados é: {}.'.format(tam, soma))
