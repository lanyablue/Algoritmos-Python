'''Faça um programa que tenha uma lista chamada numeros[] e duas funções chamadas sorteia()
e somaPar(). A primeira função vai sortear 5 números e coloca-los dentro da lista e a
segunda função vai mostrar a soma entres todos os valores pares sorteados pela função anterior'''

from random import randint

números = []

def sorteia(num):
    for c in range(0, 5):
        números.append(randint(0, 10))
    print(f'A lista ficou {números}.')


def somaPar(lst):
    print(f'O números pares da lista são: ', end='')
    for i in lst:
        if i % 2 == 0 and i != 0:
            print(f'{i}', end=' ')


sorteia(números)
somaPar(números)
