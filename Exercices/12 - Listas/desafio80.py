'''Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre=os em uma lista, ja na posição correta de inserção (sem usar sort()).
No final, mostre a lista ordenada na tela.'''

valores = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[len(valores)-1]:   #valores[-1]
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n < valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print(f'Sua lista ficou {valores}')
