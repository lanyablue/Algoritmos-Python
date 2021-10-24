"""Faça um programa que tenha uma função chamada area(), que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a area do terreno"""


def area(a, b):
    retangulo = a * b
    print(f'A area de {a}x{b} é de {retangulo}m².')


print('Calculo de area:')
a = float(input('Largura: '))
b = float(input('Comprimento:'))

area(a, b)


