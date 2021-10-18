'''Escreva um programa para aprovar o empréstimo  bancário para a
compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal. sabendo que ela nao pode exceder
30% do salário ou então
o empréstimo será negado.'''

c = float(input('Qual o valor da casa que você pretende comprar? R$'))
s = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você pretende quitar seu empréstimo? '))
print('Vamos analisar seu empréstimo....')
per = s * 30 / 100 #calcula 30% do salário colocado
meses = anos * 12 #descobre em quantos meses vai ser pago
mensal = c / meses #calcula o valor da casa pela quantidade de meses
if mensal >= per: #analisa se a mensalidade é maior que 30% do salario colocado
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(c, anos, mensal))
    print('Seu empréstimo foi NEGADO!')
elif mensal < per: #analisa se a mensalidade é menor que 30% do salario '''
    print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(c, anos, mensal))
    print('Seu empréstimo foi APROVADO!')


