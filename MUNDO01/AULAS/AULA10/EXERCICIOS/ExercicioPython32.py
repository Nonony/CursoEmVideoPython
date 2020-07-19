"""Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""

from datetime import date
ano = int(input('Informe um ano para verificar se é bissexto ou não:\nDigite 0 (zero) para o ano atual: '))
pri = ano % 4
seg = ano % 100
if ano == 0:
    # A função date.today().year pega o ano atual.
    ano = date.today().year
if pri == 0 and seg != 0 or ano == 0:
    print('{} é bissexto.\nPortanto o mês de fevereiro tem 29 dias'.format(ano))
else:
    print('{} não é bissexto.\nPortanto o mês de fevereiro tem 28 dias'.format(ano))
print('FIM!')
