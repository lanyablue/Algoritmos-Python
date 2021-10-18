'''Crie um programa que mostre na tela todos os numeros
pares que estão no intervalo entre 1 e 50.'''

from time import sleep
print('Mostrando todos os números pares entre 1 e 50...')
sleep(1)
for c in range(0, 50+1, 2):
    if c < 50:
        print(c, end=', ')
    else:
        print(c, end='.\n')
print('Sequência completa!')


