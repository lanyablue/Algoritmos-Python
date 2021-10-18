'''Faça um programa que leia um numero de 0 a 9999 e
mostre na tela cada um dos digitos separados
Ex:
Digite um numero: 1834
unidade: 4
dezena: 3
centena: 3
milhar: 1 '''

num = str(input('Digite um número: '))
print('Lendo o seu número....')
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
