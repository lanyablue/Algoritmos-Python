'''faça um programa que tenha uma função chamada contador(), que receba tres parametros:
inicio, fim, e passo e realize a contagem.Seu programa tem que realizar tres contagens avraves da função
criada:
a) de 1 ate 10, de 1 em 1
b) de 10 ate 0, de 2 em 2
c) Uma contagem personalizada'''

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('=-' * 20)
    print(f'Contagem de {fim} até {passo} de {passo} em {passo}:')
    #sleep(1.5)


    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            #sleep(0.5)
            cont += passo
        print('Fim!')

    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            #sleep(0.5)
            cont -= passo
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, fim, pas)

