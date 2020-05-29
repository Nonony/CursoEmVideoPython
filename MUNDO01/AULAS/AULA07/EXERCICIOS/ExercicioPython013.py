# Escreva um programa que leia o salário de um duncionário e mostre seu novo salário com 15% de aumento.

valor = float(input('Valor antigo do salário: R$ '))
aumento = float(input('Qual o percentual de aumento que será aplicado? '))
# Calcular a percentagem de aumento
perdaumento = aumento / 100
# Soma o valor do aumento no salário do funcionário
valaumento = valor + (valor * perdaumento)
print('O salário antigo era R${:.2f} e com o aumento é R${:.2f}.'.format(valor, valaumento))
