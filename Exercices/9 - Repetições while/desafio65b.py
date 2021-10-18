'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa perguntar ao usuário se ele
quer continuar ou não a digitar valores.'''


#continuar = 'S'
n = int(input('Digite um número: '))
continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
count = 1
soma = média = maior = menor = 0
while continuar in 'S':
    n = int(input('Digite um número: '))
    soma += n
    count += 1
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if count == 2:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
soma += n
média = soma / count
print('A média dos {} valores digitados é {}.'.format(count, média))
print('O maior valor foi {} e o menor {}.'.format(maior, menor))