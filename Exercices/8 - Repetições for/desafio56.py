'''Desenvolva um programa que leia o nome, idade e sexo de
4 pessoas. No final do programa, mostre:
-A média de idade do grupo
-Qual o nome do homem mais velho
-Quantas mulheres têm menos de 20 anos'''

lista_nome = ['' for x in range(4)]
lista_sexo = ['' for x in range(4)]
lista_idade = ['' for x in range(4)]
nome_velho = 'nenhum'
idade_velho = 0
cuier = 0
cuier_nova = 0
sexo = 0
media = 0
macho = 0

for c in range(0, 4):
    print('{:=^25}'.format('{}ª PESSOA'.format(c+1)))
    lista_nome[c] = str(input('Nome: ')).strip().upper()
    lista_sexo[c] = str(input('Sexo [M/F]: ')).strip().upper()
    lista_idade[c] = int(input('Idade: '))
for c in range(0, 4):
    m = lista_idade[c] / 4
    media += m
for c in range(0, 4):
    if lista_sexo[c] == 'M':
        if lista_idade[c] > idade_velho:
            idade_velho = lista_idade[c]
            nome_velho = lista_nome[c]
    elif lista_sexo[c] == 'F':
        cuier += 1
for c in range(0, 4):
    if lista_sexo[c] == 'F':
        if lista_idade[c] < 20:
            cuier_nova += 1
    if lista_sexo[c] == 'M':
            macho += 1
print('A média de idade de grupo é de {} anos.'.format(media))
if cuier == 4:
    print('Não tem homens no grupo.')
else:
    print('O homem mais velho é o {} que tem {} anos.'.format(nome_velho, idade_velho))
if cuier_nova >= 1:
    print('O grupo possui {} mulheres menores de 20 anos.'.format(cuier_nova))
elif cuier_nova == 0:
    print('Todas as mulheres do grupo são maiores de 20 anos.')
elif macho == 4:
    print('Só possui homens no grupo.')
