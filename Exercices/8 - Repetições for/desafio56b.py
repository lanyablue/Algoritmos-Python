'''Desenvolva um programa que leia o nome, idade e sexo de
4 pessoas. No final do programa, mostre:
-A média de idade do grupo
-Qual o nome do homem mais velho
-Quantas mulheres têm menos de 20 anos'''

somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0

for p in range(1, 5):
    print('--------{}ªPESSOA---------'.format(p))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('O grupo possui {} mulheres com menos de vinte anos'.format(mulher20))



