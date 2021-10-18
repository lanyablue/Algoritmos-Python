'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior peso e o menor peso lido.'''

menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}KG e o menor foi {}KG'.format(maior, menor))
