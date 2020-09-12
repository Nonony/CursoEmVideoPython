"""Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão."""

print('=' * 35)
print('{:^35}'.format('PROGRASSÃO ARITMÉTICA'))
print('=' * 35)
termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))
quantidade = int(input('Quantidade de termos da PA: '))

# A formula matemática para calcular a PA é a+(n-1).r
# Onde a = Primeiro termo.
#      n = Posição do termo geral.
#      r = Razão da P.A.
pa = termo1 + (quantidade - 1) * razao
pa = pa + 1

for i in range(termo1, pa, razao):
    print('{}'.format(i), end='-> ')
print('FIM...')    
