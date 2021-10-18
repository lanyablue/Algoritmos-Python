'''Refaça o desafio 35 dos triangulos, acrecentando o
recurso de mostrar que tipo de triangulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes'''

r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de outra reta: '))
r3 = float(input('Digite o valor de mais uma reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Suas retas podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('ESCALENO!')
    elif r1 != r2 == r3 or r2 != r1 == r3 or r3 != r1 == r2: #else ficaria mais pratico
        print('ISÓSCELES!')
else:
    print('Suas retas não podem formar um triângulo!')
