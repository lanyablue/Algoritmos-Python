'''Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.'''

'''from random import randint
x = randint(0, 10)
n = 0
tentativas = 0
print('Pensei em um número entre 0 e 10, tente adivinhar!')
while n != x:
    n = int(input('Qual numero eu pensei? '))
    tentativas += 1
    if n < x:
        print('Mais.... Tente novamente!')
    if n > x:
        print('Menos... Tente novamente!')
    if n == x:
        print('PARABÉNS!!! Eu pensei em {}, você acertou na {}ª tentativa.'.format(x, tentativas))'''

from random import randint
computador = randint(0, 10)
print('Pensei em um número entre 0 e 10, tente adivinhar!')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.... Tente novamente!')
        elif jogador > computador:
            print('Menos... Tente novamente!')
print('Acertou com {} tentaivas. Parabéns!'.format(tentativas))



