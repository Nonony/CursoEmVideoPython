"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[1] Converter para \033[1mBINÁRIO\033[m\n[2] Converter para \033[1mOCTAL'
      '\033[m\n[3] Converter para \033[1mHEXADECIMAL\033[m')
opt = int(input('Sua opção: '))
if opt == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif opt == 2:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, oct(num)[2:]))
elif opt == 3:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('{} não é uma opção válida!'.format(opt))
