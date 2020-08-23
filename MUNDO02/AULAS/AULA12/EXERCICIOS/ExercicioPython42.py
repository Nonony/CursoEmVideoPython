"""Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""

r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))
if (r2 + r3) > r1 > (r2 - r3):
    # Expressão antes de ser simplificada if r1<(r2+r3) and r1>(r2-r3):
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('As medidas {}, {} e {} formarão um triangulo ESCALENO.'.format(r1, r2, r3))
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('As medidas {}, {} e {} formarão um triangulo ISÓSCELES.'.format(r1, r2, r3))
    else:
        print('As medidas {}, {} e {} formarão um triangulo EQUILÁTERO.'.format(r1, r2, r3))
else:
    print('As medidas {}, {} e {} não podem formar um triângulo.'.format(r1, r2, r3))
