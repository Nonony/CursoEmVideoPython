"""Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""

num = int(input('Digite um número para ver sua tatuada: '))
print('=' * 13)
print('=' * 2, 'TABUADA', '=' * 2)
for c in range(1, 11):
    print('{} X {:2} = {:2}'.format(num, c, (num * c)))
print('=' * 13)