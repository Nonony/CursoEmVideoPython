# Escreva um programa que leia uma temperatura em Graus Centigrados e converta para Fahrenheit
# Formula de conversão: (temp °C × 9/5) + 32

temperatura = float(input('Temperatura em °C: '))
conversao = (temperatura * (9 / 5) + 32)
print('A temperatura {}°C equivale a {:.1f}°F'.format(temperatura, conversao))
