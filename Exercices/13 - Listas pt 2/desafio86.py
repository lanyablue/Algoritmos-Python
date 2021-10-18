'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com
valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

matrix = []
dados = list()

for c in range(0, 3):
    for a in range(0, 3):
        dados.append(int(input('Digite um valor: ')))
    matrix.append(dados[:])
    dados.clear()

for item in matrix:
    for itens in item:
        print(itens, end=' ')
    print()
