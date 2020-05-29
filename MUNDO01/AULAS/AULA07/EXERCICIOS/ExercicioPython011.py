# Escreva um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('Qual a altura da parede em metros? '))
largura = float(input('Qual a largura da parede em metros? '))
area = altura * largura
tinta = area / 2
print('Uma parede de {} x {} com área total de {}m², precisará de {}l de tinta para '
      'pinta-la.'.format(altura, largura, area, tinta))
