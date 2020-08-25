"""Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

import time as tm
print('Contagem regressiva para os fogos de artificio!')
for c in range(10, -1, -1):
    tm.sleep(1)
    print(c)
tm.sleep(1)
print('KABUM!... BADUMM...! POW...!')
