"""
Exercício Python 35:
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triângulo."""

r1 = float(input('Segmento 1: '))
r2 = float(input('Segmento 2: '))
r3 = float(input('Segmento 3: '))
# Expressão simplificada:
if (r2 + r3) > r1 > (r2 - r3):
    # Expressão antes de ser simplificada if r1<(r2+r3) and r1>(r2-r3):
    print('As medidas {}, {} e {} podem formar um triângulo.'.format(r1, r2, r3))
else:
    print('As medidas {}, {} e {} não podem formar um triângulo.'.format(r1, r2, r3))
print('Fim!')
