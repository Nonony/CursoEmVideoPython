"""Exercício Python 34:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores  a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

sal = float(input('Qual o valor do salário: '))
calc1 = 0.1
calc2 = 0.15
val = ''
if sal <= 1250.00:
    val = (sal * calc1) + sal
if sal > 1250.00:
    val = (sal * calc2) + sal
print('O novo valor do salário é R${:.2f}'.format(val))
