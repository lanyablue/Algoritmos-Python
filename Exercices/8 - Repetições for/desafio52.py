'''Faça um programa que leia um número inteiro e diga
se ele é ou não um número primo'''

#não pode ser multiplo de tres nem de 2 nem de 7 nem de 5

is_prime = True

num = int(input('Digite um número: '))
for c in range(2, num):
    if num % c == 0:
        is_prime = False
if is_prime:
    print('Seu número é primo.')
elif not is_prime:
    print('Seu número não é primo.')

'''numero = int(input("Digite um numero"))
divisores = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        divisores = divisores + 1'''