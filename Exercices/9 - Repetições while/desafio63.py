'''Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de uma
sequência de fibonacci.
Ex: 0, 1, 1, 2, 3, 5, 8'''

print('=-' * 15)
print('    Sequência de Fibonacci')
print('=-' * 15)
n = int(input('Digite quantos termos quer mostrar: '))
count = 3
t1 = 0
t2 = 1
print('{} → {} →'.format(t1, t2), end=' ')
while count <= n:
    t3 = t1 + t2
    print('{} →'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    count += 1
print('FIM')
print('=-' * 15)








