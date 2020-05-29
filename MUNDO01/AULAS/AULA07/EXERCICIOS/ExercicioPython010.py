# Escreva um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos Dolares Americanos ele pode
# comprar.

carteira = float(input('Quantos reais votem tem em sua carteira? R$ '))
cot = 1 / 5.3405
conversao = carteira * cot
print('Com R${}, você poderá comprar US${:.2f}'.format(carteira, conversao))
