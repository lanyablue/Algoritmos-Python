'''Faça um programa que jogue par ou impar com o computador.
O jogo só sera interrompido quando o jogador PERDER, mostrando o total de
vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
vitorias = partida = 0
par = ''
número = ''
impar = ''
print('~'*40)
print('Vamos brincar de ímpar ou par!')
print('~'*40)
while True:
    computador = randint(0, 10)
    jogador = int(input('Digite seu valor: '))
    escolha = str(input('Impar ou Par? ')).strip().upper()[0]
    while escolha not in 'PpIi':
        escolha = str(input('Impar ou Par? ')).strip().upper()[0]
    partida = jogador + computador
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    soma = jogador + computador
    if partida % 2 == 0:
        partida = 'P'
        número = 'par'
    else:
        partida = 'I'
        número = 'impar'
    print(f'A soma deu {soma}, sendo considerado {número}!!!')
    if escolha == partida:
        print('{:+^45}'.format('\033[1;36mVocê ganhou!!!\033[m'))
        print('Parabéns, jogue novamente!')
        print('=' * 40)
        vitorias += 1
    if escolha != partida:
        print('{:x^45}'.format('\033[1;31mGAME OVER!!!\033[m'))
        print(f'Você venceu {vitorias} vezes')
        break
