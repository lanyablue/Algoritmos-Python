'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

escolha = 0
soma = 0
maior = ''

from time import sleep
print('=-'*20)
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
while escolha != 5:
    print('=-' * 20)
    print('''Escolha uma opção:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa!''')
    escolha = int(input('Digite a opção desejada: '))
    print('=-' * 20)
    if escolha == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}.'.format(v1, v2, soma))
        print('=-' * 20)
    elif escolha == 2:
        multi = v1 * v2
        print('A multiplicação entre {} e {} é {}.'.format(v1, v2, multi))
        print('=-' * 20)
    elif escolha == 3:
        if v1 > v2:
            maior = v1
        if v1 < v2:
            maior = v2
            print('O maior valor é {}.'.format(maior))
        if v1 == v2:
            print('Os dois valores são iguais.')
        print('=-' * 20)
    elif escolha == 4:
        print('Insira novos valores!')
        v1 = int(input('Digite um valor: '))
        v2 = int(input('Digite outro valor: '))
        print('=-'*20)
    elif escolha == 5:
        print('Programa finalizado.')
        break
    else:
        print('Escolha invalida, reiniciando o programa e tente novamente!')
    sleep(2)



'''while escolha == 1:
    soma = v1 + v2
while escolha == 2:
    multiplicação = v1 * v2
while escolha == 3:
    v1 = maior '''
