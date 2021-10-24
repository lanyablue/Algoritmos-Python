'''faça um programa que tenha uma função chamada contador(), que receba tres parametros:
inicio, fim, e passo e realize a contagem.Seu programa tem que realizar tres contagens avraves da função
criada:
a) de 1 ate 10, de 1 em 1
b) de 10 ate 0, de 2 em 2
c) Uma contagem personalizada'''

from time import sleep


def contador(inicio, fim, passo):
    for c in range(inicio, fim + passo, passo):
        print(f'{c}', end=' ')
        sleep(0.2)
    print('FIM!')


contador(inicio=1, fim=10, passo=1)
contador(inicio=10, fim=0, passo=2)
