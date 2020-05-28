# Escreva um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis
# sobre ele.

valor = input('Digite algo: ')
print('Você digitou: {}'.format(valor))
print('Tipo primitivo:\n{}'.format(type(valor)))
print('É Alphanumérico?\n{}'.format(valor.isalnum()))
print('É Alfabético?\n{}'.format(valor.isalpha()))
print('É um Caractere ASCII?\n{}'.format(valor.isascii()))
print('É Decimal?\n{}'.format(valor.isdecimal()))
print('É um Dígito?\n{}'.format(valor.isdigit()))
print('É Identificador?\n{}'.format(valor.isidentifier()))
print('Todos os caracteres são Minúsculos?\n{}'.format(valor.islower()))
print('É Numérico?\n{}'.format(valor.isnumeric()))
print('É Printável?\n{}'.format(valor.isprintable()))
print('É um Espaço?\n{}'.format(valor.isspace()))
print('A primeira letra de cada palávra é maiúscula?\n{}'.format(valor.istitle()))
print('Todos os caracteres são Maiúsculos?\n{}'.format(valor.isupper()))
