'''Faça um programa que leia o nome de uma pessoa, mostrando em
seguida o primeiro e o ultimo nome separadamente
Ex: Ana Maria de Souza
primeiro: Ana
ultimo: Souza'''

nome = str(input('Digite o seu nome: ')).strip()
cut = nome.split()
print('Primeiro nome: {}'.format(cut[0]))
print('Ultimo nome: {}'.format(cut[len(cut)-1]))

