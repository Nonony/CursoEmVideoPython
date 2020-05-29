# Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, m, dm, cm, mm.

metros = float(input('Informe a medida que deseja converter em metros(m): '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
m = metros
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('A medida de {}m corresponde a:'.format(metros))
print('{:.0f}km'.format(km))
print('{:.0f}hm'.format(hm))
print('{:.0f}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
