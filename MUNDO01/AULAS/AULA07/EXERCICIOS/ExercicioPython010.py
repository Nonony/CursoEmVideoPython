# Escreva um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos Dolares Americanos ele pode
# comprar.

carteira = float(input('Quantos reais votem tem em sua carteira? R$ '))
cotdolar = 1 / 5.4257
print(cotdolar)
coteuro = 1 / 6.0258
print(coteuro)
condolar = carteira * cotdolar
coneuro = carteira * coteuro
print('Com R${}, você poderá comprar US${:.2f} ou €{:.2f}'.format(carteira, condolar, coneuro))
