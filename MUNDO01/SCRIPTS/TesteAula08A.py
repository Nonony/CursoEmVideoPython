import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada do número {} é {}.'.format(num, raiz))
print('A raiz quadrada do número {} é {}.'.format(num, math.floor(raiz)))  # Arredonda pra baixo
print('A raiz quadrada do número {} é {}.'.format(num, math.ceil(raiz)))  # Arredonda pra cima


"""
Outra forma de escrever o código acima é::

from math import sqrt
num = int(input('Digite um número'))
raiz = sqrt(num)
print('A raiz quadrada do número {} é {}.'.format(num, raiz))

No caso acima importamos apenas a funcionalidade sqrt da biblioteca math
e portanto podemos utilizar o comando sqrt sem a necessidade de referenciar a biblioteca
"""