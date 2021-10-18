'''Crie um programa que leia o nome de
uma pessoa e diga se tem SILVA no nome.'''

nome = str(input('Digite o seu nome: ')).strip()
m = nome.upper()
t = 'SILVA' in m
print('Seu nome tem Silva? {}'.format(t))


nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))







