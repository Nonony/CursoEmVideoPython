"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input('Informe o peso em KG: '))
altura = float(input('Informe a altura "Ex: 1.71": '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Seu IMC é {:.1f}\nVocê está ABAIXO do peso ideal.'.format(imc))
elif 18.5 <= imc <= 24.9:
    print('Seu IMC é {:.1f}\nVocê está no seu peso IDEAL.'.format(imc))
elif 25 < imc <= 29.9:
    print('Seu IMC é {:.1f}\nVocê está com SOBREPESO.'.format(imc))
elif 30 < imc <= 39.9:
    print('Seu IMC é {:.1f}\nVocê está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.1f}\nVocê está com OBESIDADE MORBIDA.'.format(imc))
