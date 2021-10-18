'''Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:
-Se ele ainda vai se alistar no serviço militar
-Se é a hora de se alistar
-Se ja passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo
que falta ou que passou do prazo'''

from datetime import date
data = int(input('Digite a data de nascimento desejada: '))
atual = date.today().year
idade = atual - data
tempo = 18 - idade
print('Quem nasceu em {} tem {} anos em {}'.format(data, idade, atual))
if idade == 18:
    print('Está na hora de você se alistar ao serviço militar!')
elif idade < 18:
    ano = atual + tempo
    print('Ainda falta {} anos para você precisar se alistar ao serviço militar!'.format(tempo))
    print('Você ira se alistar em {}.'.format(ano))
elif idade > 18:
    atraso = idade - 18
    ano1 = atual - atraso
    print('Já passou da hora de voce se alistar!!! Você está {} anos atrasado!'.format(atraso))
    print('Você deveria ter se alistado em {}'.format(ano1))

