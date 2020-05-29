# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Distância em metros(m): '))
cm = metros * 100
mm = metros * 1000
print('{}m equivalem a {}cm e {}mm'.format(metros, cm, mm))
