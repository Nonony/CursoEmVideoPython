"""Escreva um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa."""

# Resolução do exercício 17 sem utilizar importação de módulos.
# Apenas utilizando formula matemática

catop = float(input('Cateto oposto: '))
catad = float(input('Cateto adjacente: '))
hip = (catop ** 2 + catad ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hip))
