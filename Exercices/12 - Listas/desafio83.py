'''Crie um programa onde o usuário digita uma expressão qualquer que
use parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos
e fechados na ordem correta.'''

expressão = input('Digite uma expressão para ser validada: ')
lista = []
pilha = []
for letra in expressão:
    lista.append(letra)
for c in lista:
    if c == '(':
        pilha.append(c)
    elif c == ')':
        if len(pilha) >= 1:
            pilha.pop()
        else:
            pilha.append(c)
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Expressão inválida.')
