'''Faça um programa que leia um ano qualquer
e mostre se ele é bissexto'''
#1 ano = 365d 5h48min 45,25seg

from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Seu ano é bissexto.')
else:
    print('Seu ano não é bissexto.')
