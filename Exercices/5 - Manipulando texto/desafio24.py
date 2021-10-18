'''Crei um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome SANTO'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
n = cidade.upper().split()
r = 'SANTO' == n[0]
print('O nome da cidade começa com Santo? {}'.format(r))



cid =  str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
