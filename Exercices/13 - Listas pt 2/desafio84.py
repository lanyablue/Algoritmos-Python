'''Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves'''

pessoas = []
dado = []

while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    pessoas.append(dado[:])
    dado.clear()
    continuar = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print(f'Ao todo foram cadatradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas acima de 100kg foram: ', end='')
for p in pessoas:
    if p[1] >= 100:
        print(f'{p[0]}', end=' ')

print(f'\nAs pessoas mais leves com menos de 70kg foram: ', end='')
for p in pessoas:
    if p[1] <= 70:
        print(f'{p[0]}', end=' ')
