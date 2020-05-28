# Crie um programa que leia um número
# Mostre seu dobro, triplo e raiz quadrada

n = int(input('Digite um número: '))
print('O número digitado foi o {}\n'
      'Seu dobro é {}\n'
      'Seu triplo é {}\n'
      'Ele tem raiz quadrada igual a {:.2f}'.format(n, n * 2, n * 3, n ** (1/2)))
# A raiz quadrada também pode ser obtida utilizando a função pow(n, (1/2))
