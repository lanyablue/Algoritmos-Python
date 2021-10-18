'''Crie um programa que faça o computador
jogar jokenpo com você'''

from random import randint
from time import sleep
print('=-' * 10)
print('Vamos jogar Jokenpô!')
print('=-' * 10)
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
print('=-' * 10)
escolha = int(input('Pedra, papel ou tesoura??? Faça sua escolha: '))
print('jo')
sleep(1)
print('ken')
sleep(1)
print('pô...')
sleep(1)
lista = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)
if computador == 0:    # computador jogou pedra
    if escolha == 0:
        print('Empatamos!')
    elif escolha == 1:
        print('Você venceu!')
    elif escolha == 2:
        print('Você perdeu!')
elif computador == 1:    # computador jogou papel
    if escolha == 0:
        print('Você perdeu!')
    elif escolha == 1:
        print('Empatamos!')
    elif escolha == 2:
        print('Você ganhou!')
elif computador == 2:   # computador jogou tesoura
    if escolha == 0:
        print('Você ganhou!')
    elif escolha == 1:
        print('Você perdeu!')
    elif escolha == 2:
        print('Empatamos!')
print('Você escolheu {}.'.format(lista[escolha]))
print('Eu escolhi {}.'.format(lista[computador]))
print('=-' * 10)





