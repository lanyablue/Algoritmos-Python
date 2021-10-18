'''Escreva um programa que pergunte o salario de um funcionario
e calcule o valor de seu aumento.
Para salários superiores a R$1250,00 calcule um aumento de 10%
Para os inferiores ou iguais o aumento é de 15%'''

s = float(input('Digite o salário do funcionário: '))
if s >= 1250.00:
    a = s * 10 / 100
    atual = s + a
    print('O salário do funcionário foi aumentado em {} reais.'.format(a))
    print('O salário atual do funcionário é {} reais.'.format(atual))
else:
    a1 = s * 15 / 100
    atual2 = s + a1
    print('O salário do funcionário foi aumentado em {} reais.'.format(a1))
    print('O salário atual do funcionário é {} reais.'.format(atual2))

