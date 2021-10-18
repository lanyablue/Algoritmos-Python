"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

cinquenta = 0
vinte = 0
dez = 0
um = 0
original = 0
print('{:-^40}'.format('Caixa Eletronico.'))
while True:
    sacar = int(input('Quanto você deseja sacar: R$'))
    original = sacar
    modulo50 = sacar % 50
    cinquenta = (sacar - modulo50) / 50
    sacar = modulo50
    modulo20 = sacar % 20
    vinte = (sacar - modulo20) / 20
    sacar = modulo20
    modulo10 = sacar % 10
    dez = (sacar - modulo10) / 10
    sacar = modulo10
    modulo1 = sacar
    um = modulo1
    break
print(f'Você sacou R${original:.2f}, recebendo: ')
if cinquenta != 0:
    print(f'{cinquenta:.0f} notas de R$50.00.')
if vinte != 0:
    print(f'{vinte:.0f} notas de R$20.00.')
if dez != 0:
    print(f'{dez:.0f} notas de R$10.00.')
if um != 0:
    print(f'{um} notas de R$1.00.')






