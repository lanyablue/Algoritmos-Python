'''Desenvolva um programa que leia o comprimento de tres retas
e o diga  ao usuario se elas podem ou não formar um triangulo'''

r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de outra reta: '))
r3 = float(input('Digite o valor de mais uma reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Suas retas podem formar um triângulo!')
else:
    print('Suas retas não podem formar um triângulo!')



