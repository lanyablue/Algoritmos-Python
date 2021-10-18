'''Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.'''

matrix = []
dados = list()
soma = somaterceira = maior = 0


for c in range(0, 3):
    for a in range(0, 3):
        dados.append(int(input('Digite um valor: ')))
    matrix.append(dados[:])
    dados.clear()

print('=-'*20)

for item in matrix:
    for itens in item:
        print(itens, end=' ')
        soma += itens
    print()

for c in range(0, len(matrix)):
    for i in range(0, len(matrix[c])):
        if i == 2:
            somaterceira += matrix[c][i]

for c in range(0, len(matrix)):
    for i in range(0, len(matrix[c])):
        if c == 1:
            if i == 1:
                maior = matrix[c][i]
            if matrix[c][i] > maior:
                maior = matrix[c][i]
print('=-'*20)
print(f'A soma de todos os itens é {soma}.')
print(f'A soma da terceira coluna é {somaterceira}.')
print(f'O maior valor da segunda linha é {maior}.')
