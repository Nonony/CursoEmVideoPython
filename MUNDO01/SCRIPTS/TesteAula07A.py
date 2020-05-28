n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
som = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
di = n1 // n2
rdiv = n1 % n2
expo = n1 ** n2
print('A soma entre {} e {} é igual a {}.'.format(n1, n2, som))
print('{} menos {} é igual a {}.'.format(n1, n2, sub))
print('A multiplicação de {} por {} é igual a {}.'.format(n1, n2, mult))
print('A divisão entre {} e {} é igual a {:.1f}.\nA divisão inteira é igual a {}.\n'
      'O resto da divisão é igual a {}.'.format(n1, n2, div, di, rdiv))
print('A exponenciação de {} elevado a {} é igual a {}.'.format(n1, n2, expo))
