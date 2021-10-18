"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

print('{:=^40}'.format('Lojas fé nas malukas'))
tot = caros = count = 0
barato = ' '
preçodobarato = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    preço = float(input('Digite o valor do produto: R$'))
    count += 1
    tot += preço
    if preço >= 1000:
        caros += 1
    if count == 1:
        barato = produto
        preçodobarato = preço
    else:
        if preço < preçodobarato:
            preçodobarato = preço
            barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]
    print('-'*40)
    if continuar == 'N':
        break
print('{:=^40}'.format('COMPRA FINALIZADA!'))
print(f'O total da sua compra deu R${tot:.2f}.')
print(f'Você comprou um total de {caros} produtos acima de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${preçodobarato:.2f}.')
