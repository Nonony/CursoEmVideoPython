"""Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 
Exemplos de palíndromos:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA."""

# RESOLUÇÃO DO EXERCÍCIO 53 USANDO LAÇO FOR

texto = str(input('Digite um texto: ')).strip().upper()
lista = texto.split()
juntando = ''.join(lista)   
invertido = ''
for letra in range(len(juntando) -1, -1, -1):
    invertido += juntando[letra]
if invertido == juntando:
    print('O contrário de {} é {}.'.format(juntando, invertido))
    print('Temos um palindromo!')
else:
    print('O contrário de {} é {}'. format(juntando, invertido))
    print('A frase digitada não é um palindromo!')    
