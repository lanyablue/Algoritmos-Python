'''Crie um programa onde o usuário digita uma expressão qualquer que
use parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos
e fechados na ordem correta.'''

pilha = []
expressão = str(input('Digite uma expressão: '))
aconteceu_erro = False
for letra in expressão:
    if letra == '(':
        pilha.append(letra)
    elif letra == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            aconteceu_erro = True
if len(pilha) == 0 and not aconteceu_erro:
    print('Expressão correta.')
else:
    print('Expressão errada.')
