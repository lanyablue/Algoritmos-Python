'''Crie um programa que leia o nome
completo de umas pessoa e mostre:
-O nome com todas as letras maiusculas
-O nome com todas as letras minisculas
-Quantas letras tem ao todo (sem espaço)
-Quantas letras tem o primeiro nome'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('O seu nome em letra maiusculas fica: {}'.format(nome.upper()))
print('O seu nome em letras minusculas fica: {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
s = nome.split()
print('O seu primeiro nome tem {} letras'.format(len(s[6])))