'''faça um programa que mostre na tela uma contagem regressiva para
o estouro de fogos de artifico, indo de 10 ate 0, com uma pausa de 1
segundo ele eles.'''

import emoji
from time import sleep
print('Contagem regressiva para o Ano Novo \U0001F386!')
for c in range(10, 1-1, -1):
    print(c)
    sleep(1)
print('Feliz ano novo \U0001F973 \U0001F942')