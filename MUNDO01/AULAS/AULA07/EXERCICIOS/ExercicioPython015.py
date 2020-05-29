# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e quantidade de dias que ele
# permaneceu alugado.
# Calcule o preço a pagar sabendo que o aluguel do carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Qual a quilometragem total rodada? '))
dias = int(input('Quantidade de dias alugado? '))
valpag = ((km * 0.15) + (dias * 60))
print('Olá!\nO veículo permaneceu alugado por {} dias e percorreu um total de {:.2f} quilometros.'.format(dias, km))
print('O valor a pagar será de R${:.2f}'.format(valpag))
print('Obrigado. Tenha um bom dia!')
