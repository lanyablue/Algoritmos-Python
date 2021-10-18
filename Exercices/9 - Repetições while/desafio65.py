'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos. O programa perguntar ao usuário se ele
quer continuar ou não a digitar valores.'''

média = maior = menor = soma = count = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número inteiro: '))
    count += 1
    soma += n
    if count == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
média = soma / count
print('A média de todos os {} valores é {}'.format(count, média))
print('O maior valor digitado foi {}, e o menor {}.'.format(maior, menor))