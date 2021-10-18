'''Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores impares digitados, respectivamente.
No final, mostre o conteudo das três listas geradas.'''

valores = []
impar = []
par = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Sua lista ficou: {valores}')
print(f'A lista de números pares é {par}')
print(f'A lista de número impares é {impar}')
