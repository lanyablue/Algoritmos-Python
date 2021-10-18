'''Crie um programa onde o usuario possa digitar sete valores numéricos
e cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente.'''

valores = list()

for c in range(0, 7):
    valores.append(int(input(f'Digite o {c}º valor: ')))

sorted(valores)

print(f'Os valores pares digitados foram {valores}')
print('Os numeros pares são: ', end=' ')

for n in valores:
    if n % 2 == 0:
        print(f'{valores[n]}')
print('\n')

print(f'E os valores ímpares digitados foram: ', end=' ')
for c in valores:
    if c % 2 != 0:
        print(f'{valores[c]}')
print('\n')


