# Escreva um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
catop = float(input('Cateto oposto: '))
catad = float(input('Cateto adjacente: '))
hip = hypot(catop, catad)
print('A hipotenusa é igual a: {:.2f}'.format(hip))
