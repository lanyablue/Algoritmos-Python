'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maioridade = homem = cuiermenor = 0
print('{:-^40}'.format('Banco de dados'))
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        cuiermenor += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]
    print('-'*40)
    if continuar == 'N':
        break
print(f'O grupo possui {maioridade} pessoas maiores de idade.')
print(f'Foram cadastrados {homem} homens no grupo.')
print(f'O grupo possui {cuiermenor} mulheres com menos de 20 anos.')

