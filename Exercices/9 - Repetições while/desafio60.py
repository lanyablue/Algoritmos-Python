'''Faça um programa que leia um número qualquer e msotre
o seu fatorial.
ex: 5! = 5x4x3x2x1 = 120'''


'''n = int(input('Digite um número: '))
c = n
f = 1 #sempre que for um contador de mutiplicação, o valor inicil é 1, pois nao se multiplica por 0
print('Calculando {}! ='.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))'''

n = int(input('Digite um número: '))
f = 1
for c in range(n, 0, -1):
    f *= c
print(f)