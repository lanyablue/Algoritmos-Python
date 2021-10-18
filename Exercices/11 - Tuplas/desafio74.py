'''Crie um porgrama que vai gerar cinco números aleatorios e colocar em
uma tupla. Depois disso mostre a listagem de números gerados e também indique
o menor e o maior valor que estão na tupla'''
from audioop import max
from random import randint
tupla = (randint(0, 9), randint(0, 9), randint(0, 9),
         randint(0, 9), randint(0, 9))
print(f'Os valores sorteados foram: {tupla}')
maior = tupla[0]
menor = tupla[0]
#maior = max(tupla)
#menor = min(tupla)
for c in tupla:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
for c in range(0, len(tupla)):
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]
print(f'O maior valor foi {maior} e o menor {menor}.')
# print(len(tupla))