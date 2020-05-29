# Escreva um programa que leia o valor de um produto.
# Calcule o mostre na tela o valor dele com x% de desconto na compra a vista
# Calcule e mostre na tela o valor dele com x% de aumento na compra a prazo

valor = float(input('Valor do Produto: R$ '))
vista = float(input('Desconto nas compras à vista: '))
prazo = float(input('Aumento nas compras à prazo: '))
percentv = vista / 100
percentp = prazo / 100
calcvista = valor - (valor * percentv)
calcprazo = valor + (valor * percentp)
print('O produto que custa R${:.2f}, sai por R${:.2f} nas compras à vista e por R${:.2f} nas compras à prazo'
      .format(valor, calcvista, calcprazo))
