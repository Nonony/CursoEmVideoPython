# Escreva um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valor = float(input('Valor do produto: '))
desc = float(input('Qual o valor de desconto que será aplicado? '))
# Calcular a percentagem de desconto
perdesc = desc / 100
# Abater o valor do desconto do valor total do produto
valdesc = valor - (valor * perdesc)
print('O produto custa R${} sem desconto e R${} com desconto.'.format(valor, valdesc))
