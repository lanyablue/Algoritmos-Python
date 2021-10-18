'''Escreve um programa que leia dois numeros inteiros
e compare-os, mostrando na tela uma mensage:
-O primeiro valor é maior:
-O segundo valor é maior:
-Não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um segundo valor: '))
if n1 > n2:
    print('O maior número é o {}, e o menor é {}.'.format(n1, n2))
elif n2 > n1:
    print('O maior número é o {}, e o menor é o {}.'.format(n2, n1))
else:
    print('Não existe valor maior ou menor, os dois são iguais.')
