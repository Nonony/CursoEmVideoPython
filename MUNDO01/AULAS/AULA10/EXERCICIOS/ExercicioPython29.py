"""Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite."""

vel = float(input('Informe a velocidade do veículo: '))
velexced = (vel - 80) * 7
# print(velexced)
if vel >= 80:
    print('Você foi multado por excesso de velocidade!\nVelocidade máxima da via 80Km/h.\n'
          'Sua velocidade {}km/h'.format(vel))
    print('Valor da multa: R${}'.format(velexced))
else:
    print('Tenha um bom dia!')
print('FIM!')
