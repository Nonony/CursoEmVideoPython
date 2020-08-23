"""Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não
pode exceder 30% do salário ou então o empréstimo será negado."""

valimovel = float(input('Qual o valor do imóvel: R$ '))
salcomp = float(input('Qual o seu salário: R$ '))
# Calculando 30% do salário do comprador
percentsal = ((30 / 100)*salcomp)
#print(percentsal)
tempo = int(input('Tempo de financiamento em anos: '))
# Convertendo o tempo para meses
tm = tempo * 12
tempo = tm
# print(tempo)
# Calculando o valor da prestação
valpres = valimovel / tempo
if valpres > percentsal:
    print('Para pagar uma casa novalor de R${:.2f} em {} meses, a prestação será de R${:.2f}'
          '\nEmprestimo \033[1;31mNEGADO!\033[m'.format(valimovel, tempo, valpres))
else:
    print('Para pagar uma casa novalor de R${:.2f} em {} meses, a prestação será de R${:.2f}.'
          '\nEmprestimo \033[1;32mAPROVADO!\033[m'.format(valimovel, tempo, valpres))
