'''Faça um programa que leia três números e mostre
qual é o maior e qual é o menor'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o último número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior numero é {}'.format(maior))
print('O menor número é {}'.format(menor))



'''lista = [n1, n2, n3]
m1 = max(lista)
m2 = min(lista)'''
