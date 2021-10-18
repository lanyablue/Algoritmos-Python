'''Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo'''

num = int(input('Digite um número: '))
divisao = 0
for c in range(1, num+1):
    if num % c == 0:
        divisao += 1
print('O número {} é divisível {} vezes;'.format(num, divisao))
if divisao == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO é PRIMO!')
