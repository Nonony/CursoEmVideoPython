# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Informe a medida que deseja converter mara cm e mm: '))
cm = metros * 100
mm = metros * 1000
print('{}m equivalem a {}cm e {}mm'.format(metros, cm, mm))
