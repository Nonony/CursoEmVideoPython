"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
"""

print('{:=^40}'.format(' RONY ELETRO '))
valprod = float(input('Qual o valor do produto? R$ '))
print('Qual a forma de pagamento desejada?\n1 - à vista dinheiro/cheque.\n2 - à vista no cartão de crédito.'
      '\n3 - 2x no cartão.\n4 - 3 ou mais x no cartão.')
pg = int(input('Digite a forma de pagamento: '))
if pg > 4:
    print('Opção inválida.\nRefaça a transação.')
elif pg == 1:
    fgpto = 'à vista dinheiro/cheque'
    print('Valor do produto R${:.2f}.\n'
          'Forma de pagamento selecionada: {} 10% de desconto.\n'
          'Valor a ser pago R${:.2f}'.format(valprod, fgpto, valprod - (0.1 * valprod)))
elif pg == 2:
    fgpto = 'à vista no cartão de crédito'
    print('Valor do produto R${:.2f}.\n'
          'Compra realizada Á VISTA NO CARTÃO COM DESCONTO.\n'
          'Valor final R${:.2f}'.format(valprod, (valprod - (0.05 * valprod))))
elif pg == 3:
    fgpto = 'cartão de crédito parcelado 2x'
    print('Valor do produto R${:.2f}.\n'
          'Sua compra será parcelada em 2x de R${:.2f}.\n'
          'Valor final R${:.2f}'.format(valprod, (valprod / 2), valprod))
else:
    fgpto = 'cartão de crédito parcelado 3x ou mais'
    quant = int(input('Quantas parcelas? '))
    print('Valor do produto R${:.2f}.\n'
          'Sua compra será parcelada em {}x de R${:.2f} COM JUROS.\n'
          'Valor final R${:.2f}'.format(valprod, quant, ((valprod + (0.2 * valprod)) / quant), ((valprod + (0.2 * valprod)) * quant)))
