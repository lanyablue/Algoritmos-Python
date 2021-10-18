'''Crie um programa onde o usuário possa digitar vários valores
númericos e cadestre-os em uma lista. Caso o número já exista lá dentro,
ele não sera adicionado. No final, serão exibidos todos os valores unicos digitados
em ordem crescente'''

valores = []
while True:
    valor_escolhido = int(input('Digite um valor: '))
    if valor_escolhido not in valores:
        valores.append(valor_escolhido)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor repetido, não irei adicionar!')
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'Nn':
        break
print(f'Sua lista é {sorted(valores)}')
