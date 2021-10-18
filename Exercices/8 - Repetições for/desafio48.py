'''Faça um programa que calcule a soma entre todos os numeros
impares que são multiplos de tres e que se encontram
no intervalo de 1 ate 500'''

s = 0
cont = 0
for c in range(1, 500):
    if c % 3 == 0:
        if c % 2 != 0:
            s += c
            cont += 1
print('A soma entre todos os {} valores impares multiplos de 3 entre 1 e 500 é {}'.format(cont, s))






