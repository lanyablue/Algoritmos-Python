'''Refaça o desafio 009, mostrando a tabuado de um
numero que o usuario escolher, so que agora utilizando
um laço for'''

valor = int(input('Digite um valor: '))
print('A tabuada do {} é:'.format(valor))
for c in range(1, 11):
    tabuada = c * valor
    print('{} x {} = {}'.format(valor, c, tabuada))
