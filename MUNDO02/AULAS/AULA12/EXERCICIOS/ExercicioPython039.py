"""Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

import datetime as dt

anoatual = dt.datetime.today().year
nasc = int(input('Qual o ano do seu nascimento \033[1;32maaaa\033[m: '))
print('Qual o seu sexo?')
sex = int(input('Digite 1 para Masculino ou 2 para Feminino:\n'))
idade = anoatual - nasc
if sex == 1:
    if idade < 18:
        print('Quem nasceu em {} ja fez ou fará {} anos em {}\n\033[1;32mAinda faltam {} anos para o alistamento\033[m'
              '\nSeu alistamento será em {}.'.format(nasc, idade, anoatual, 18 - idade, anoatual + (18 - idade)))
    elif idade == 18:
        print('Quem nasceu em {} ja fez ou fará {} anos em {}\nVocê deve se alistar \033[1;;44mIMEDIATAMENTE.\033[m'
              ''.format(nasc, idade, anoatual))
    else:
        print('Quem nasceu em {} ja fez ou fará {} anos em {}\n\033[1;31mVocê está atrasado {} anos para o alistamento'
              '\nSeu alistamento deveria ter ocorrido em {}.\033[m'
              .format(nasc, idade, anoatual, idade - 18, anoatual - (idade - 18)))
else:
    print('Você não precisa fazer o alistamento se não quiser!')

"""dtnasc = str(input('Qual a sua data de Nascimento: ')).strip()
data = dt.datetime.strptime(dtnasc, '%d/%m/%Y')
hoje = dt.datetime.today()
idade = hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))
# print(idade)
if idade < 18:
    print('Idade atual {} anos.\n\033[1;32mCompareça ao alistamento daqui a {} ano(s)\033[m'.format(idade, 18 - idade))
elif idade == 18:
    print('Idade atual {} anos.\n\033[1;35mEste é o momento de se alistar.\033[m'.format(idade))
else:
    print('Idade atual {} anos.\n\033[1;31mVocê deveria ter se alistado a {} ano(s)\nCompareça à junta de Serviço '
          'militar mais próxima.\033[m'.format(idade, idade - 18))
# print(type(data), data, data.day, data.month, data.year)"""
