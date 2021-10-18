'''Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
c) quais foram os números pares'''

valores = (int(input('Digite um valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite o último valor: ')))
print(f'Seus valores são {valores}.')
vezes = tres = par = 0
for c in valores:
    if c == 9:
        vezes += 1
    if c == 3:
        tres += 1
    if c % 2 == 0:
        par += 1
if vezes > 0:
    print(f'O valor número 9 apareceu {vezes} vezes.')
if vezes == 0:
    print('Não foram digitados nenhum valor 9.')  # valores.count(9)
if tres > 0:
    print(f'O primeiro valor tres apareceu na posição {valores.index(3)+1}.')
if tres == 0:
    print('Não ha nenhum número três na lista.')
if par > 0:
    print(f'Os números pares são:', end=' ')
    for a in range(0, len(valores)):
        if valores[a] % 2 == 0:
            print(valores[a], end=' ')
if par == 0:
    print('Não há números pares.')