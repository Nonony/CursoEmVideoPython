"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""

nota = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
calcmed = (nota + nota2) / 2
if calcmed >= 7.0:
    print('Média 7.0 ou superior: \033[1mAPROVADO!\033[m'.format(calcmed))
elif 5 <= calcmed <= 6.9:
    print('Média entre 5.0 e 6.9: \033[1mRECUPERAÇÃO\033[m\nEstude mais!'.format(calcmed))
else:
    print('Média abaixo de 5.0: \033[1mREPROVADO!\033[m\nDedique-se mais no ano que vem.'.format(calcmed))
