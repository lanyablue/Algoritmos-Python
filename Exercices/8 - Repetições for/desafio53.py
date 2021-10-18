'''Crie um porgrama que leia uma frase qualquer e diga
se ela é um palindromo, desconsiderando os espaços.'''

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Sua frase não é um palindromo!')
