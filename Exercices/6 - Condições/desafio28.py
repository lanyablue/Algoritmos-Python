'''Escreva uma programa que faça o computador 'pensar' em um número
inteiro entre 0 e 5 e peça para o usuario tentar
descobrir qual foi o numero pensando pelo computador.

O programa deverá escrever na tela se o usuário
venceu ou perdeu!'''

from random import randint
from time import sleep
x = randint(0, 5)
n = int(input('Qual numero eu pensei? '))
print('PROCESSANDO!')
sleep(3)
if n == x:
    print('Você acertou!')
else:
    print('Você errou!')
print('Eu pensei em {}!'.format(x))

