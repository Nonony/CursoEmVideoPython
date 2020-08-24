"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""

# importa a biblioteca emoji
import emoji
import random as ran
import time as t
# Definição das variáveis pedra, papel e tesoura, para mostrar emojis correspondentes a cada uma das opções
pedra = emoji.emojize(':gem:', use_aliases=True)
papel = emoji.emojize(':page_facing_up:', use_aliases=True)
tesoura = emoji.emojize(':scissors:', use_aliases=True)
print('Olá, vamos jogar pedra, papel e TESOURA?')
# Aguarda 2 segundos antes de mostrar a mensagem do jogador (Linha 19) na tela
t.sleep(2)
comp = ran.randint(0, 2)
print('Eu já sei o que vou jogar e você?')
t.sleep(2)
print(emoji.emojize('0 -> :gem:', use_aliases=True))
print(emoji.emojize('1 -> :page_facing_up:', use_aliases=True))
print(emoji.emojize('2 -> :scissors:', use_aliases=True))
jogador = int(input('Então, qual a sua jogada? '))
if jogador > 2:
    print('Opção inválida.\nTENTE NOVAMENTE...')
else:
    t.sleep(0.5)
    print('JO...')
    t.sleep(0.5)
    print('KEN...')
    t.sleep(0.5)
    print('PO...')
    if comp == 0:
        if jogador == 0:
            comp = pedra
            jogador = pedra
            # print(comp, jogador)
            print('Ummm, não foi dessa vez!\nA {} empata com {}'.format(comp, jogador))
        elif jogador == 1:
            comp = pedra
            jogador = papel
            # print(comp, jogador)
            print('UHHUUUU! VOCÊ VENCEU!\nO {} ganha da {}.'.format(jogador, comp))
        elif jogador == 2:
            comp = pedra
            jogador = tesoura
            # print(comp, jogador)
            print('AHHHHH, VOCÊ PERDEU!\nA {} perde para a {}'.format(jogador, comp))
    if comp == 1:
        if jogador == 0:
            comp = papel
            jogador = pedra
            # print(comp, jogador)
            print('AHHHHH, VOCÊ PERDEU!\nA {} perde para o {}'.format(jogador, comp))
        elif jogador == 1:
            comp = papel
            jogador = papel
            # print(comp, jogador)
            print('Ummm, não foi dessa vez!\nO {} empata com {}'.format(comp, jogador))
        elif jogador == 2:
            comp = papel
            jogador = tesoura
            # print(comp, jogador)
            print('UHHUUUU! VOCÊ VENCEU!\nA {} ganha do {}.'.format(jogador, comp))
    if comp == 2:
        if jogador == 0:
            comp = tesoura
            jogador = pedra
            # print(comp, jogador)
            print('UHHUUUU! VOCÊ VENCEU!\nA {} ganha da {}.'.format(jogador, comp))
        elif jogador == 1:
            comp = tesoura
            jogador = papel
            # print(comp, jogador)
            print('AHHHHH, VOCÊ PERDEU!\nO {} perde para a {}'.format(jogador, comp))
        elif jogador == 2:
            comp = tesoura
            jogador = tesoura
            print('Ummm, não foi dessa vez!\nA {} empata com {}'.format(comp, jogador))
    print('Até mais!')
