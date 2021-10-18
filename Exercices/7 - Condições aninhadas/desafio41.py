'''A confederação nacional de natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
-Ate 9 anos:  mirim
-Ate 14 anos: infantil
-Ate 19 anos: junior
-Ate 20 anos: senior
-Acima: Master'''

from datetime import date
print('Seja bem vindo!')
ano = int(input('Digite o ano de nascimento do atleta desejado: '))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('Seu atleta tem {} anos e está na categoria MIRIM!'.format(idade))
elif 9 < idade <= 14:
    print('Seu atleta tem {} anos e está na categoria INFANTIL!'.format(idade))
elif 14 < idade < 19:
    print('Seu atleta tem {} anos e está na categoria JUNIOR!'.format(idade))
elif idade == 19 or ano == 20:
    print('Seu atleta tem {} anos e está na categoria SENIOR!'.format(idade))
else:
    print('Seu atleta tem {} anos e está na categoria MASTER!'.format(idade))
