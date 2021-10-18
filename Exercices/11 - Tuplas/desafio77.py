'''Crie um programa que tenha uma tupla com várias palavras (sem acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais'''

Palavras = ('Cafe', 'Arroz', 'Leite', 'Ovo', 'Carne',
            'Frango', 'Batata', 'Cenoura', 'Fruta')

for pos in Palavras:
    print(f'\nNa palavra {pos.upper()} temos as vogais:', end=' ')
    for vogais in pos:
        if vogais.lower() in 'aeiou':
            print(vogais.lower(), end=' ')




