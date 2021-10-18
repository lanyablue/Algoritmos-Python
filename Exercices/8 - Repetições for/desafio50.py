'''Desenvolva um programa que leia seis numeros inteiros
e mostre a soma apenas daqueles que forem pares.
Se o valor for impar , desconsidere-o:'''

s = 0
count = 0
for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s += num
        count += 1
print('A soma de todos os {} números pares é {}.'.format(count, s))




