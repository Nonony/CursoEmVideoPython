# Escreva um programa que leia uma temperatura em Graus Centigrados e converta para Fahrenheit
# Formula de conversão: (0 °C × 9/5) + 32 = 32 °F

temperatura = float(input('Temperatura em °C: '))
conversao = (temperatura * (9 / 5) + 32)
print('A temperatura {}°C equivale a {}°F'.format(temperatura, conversao))
