'''Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado
e suas respectivas posições na lista'''

valores = []
posmaior = posmenor = maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-'*50)
print(f'Você digitou os seguintes valores: {valores}')
print(f'O maior número da lista é o {maior} nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice}...', end='')
print(f'\nO menor número da lista é o {menor} nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice}...', end='')


