'''Faça um programa que leia uma frase pelo teclado e mostre:
-quantas vezes aparece a letra A
-em que posição ela aparece a primeira vez
-em que posição ela aparece a ultima vez'''

'''frase = str(input('Digite uma frase: ')).strip()
frasem = frase.upper()
vezes = frasem.count('A')
first = frasem.find('A')+1
ultimo = frasem.rfind('A')+1
print('A letras A aparece {} vezes'.format(vezes))
print('A posição do primeiro A é {}'.format(first))
print('A posição do ultimo A é {}'.format(ultimo))'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))