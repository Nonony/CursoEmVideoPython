"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""

import datetime as dt

hoje = dt.date.today().year
# print(hoje)
ano = int(input('Ano de nascimento do atleta: '))
idade = hoje - ano
# print(idade)
if idade > 25:
    print('O atleta nascido em {}, tem {} anos e pertence a categoria \033[1mMASTER.\033[m'.format(ano, idade))
elif 19 < idade <= 25:
    print('O atleta nascido em {}, tem {} anos e pertence a categoria \033[1mSÊNIOR.\033[m'.format(ano, idade))
elif 14 < idade <= 19:
    print('O atleta nascido em {}, tem {} anos e pertence a categoria \033[1mJÚNIOR.\033[m'.format(ano, idade))
elif 9 < idade <= 14:
    print('O atleta nascido em {}, tem {} anos e pertence a categoria \033[1mINFANTIL.\033[m'.format(ano, idade))
else:
    print('O atleta nascido em {}, tem {} anos e pertence a categoria \033[1mMIRIM.\033[m'.format(ano, idade))
