"""Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

import random
import time
print('Vou pensar em um número entre 0 e 5')
randomnum = random.randint(0, 5)
time.sleep(2)
# print(randomnum)
num = int(input('Vamos lá! Me diga qual número eu pensei: '))
if num == randomnum:
    print('Parabéns, você acertou!\nEu pensei no número {}'.format(randomnum))
else:
    print('Há, há, há, você errou!\nEu havia pensado no número {}'.format(randomnum))
print('FIM!')
