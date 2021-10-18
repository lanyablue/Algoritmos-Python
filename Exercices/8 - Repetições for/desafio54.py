'''Criei um programa que leia o ano de nascimento de 7 pessoas
No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores!'''

from datetime import date
atual = date.today().year
maioridade = 0
menoridade = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoas são de maior, e {} são de menor'.format(maioridade, menoridade))
