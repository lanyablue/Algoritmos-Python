'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois diso mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista'''

números = []
while True:
    números.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Sua lista tem {len(números)} valores.')
números.sort(reverse=True)
print(f'Sua lista de valores em ordem decrescente: {números}')
if 5 in números:
    print('O número 5 está nas posições: ', end='')
    for indice, valor in enumerate(números):
        if valor == 5:
            print(f'{indice}...', end='')
else:
    print('Não há número 5 na lista.')

