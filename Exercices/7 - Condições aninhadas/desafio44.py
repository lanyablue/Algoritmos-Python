'''Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de pagamento:
-a vista dinheiro/cheque: 10% de desconto:
-a vista no cartão: 5% de desconto:
-em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format('LOJAS QUE DIABO É IZOLDA'))
preco = float(input('Qual o preço da sua compra? '))
pagamento = int(input('''Qual será o meio de pagamento? 
[ 1 ] A vista no dinheiro ou cheque;
[ 2 ] A vista no cartão;
[ 3 ] Até duas parcelas no cartão;
[ 4 ] Três parcelas ou mais no cartão;
Escolha uma opção: '''))
print('Processando sua compra....')
if pagamento == 1:
    per = preco * 10 / 100
    valor = preco - per
    print('Sua compra de R${:.2f} ficou em um valor de R${:.2f}.'.format(preco, valor))
elif pagamento == 2:
    per = preco * 5 / 100
    valor = preco - per
    print('Sua compra de R${:.2f} ficou em um valor de RS{:.2f}'.format(preco, valor))
elif pagamento == 3:
    parcelas = preco / 2
    print('Sua compra ficou no valor de R${:.2f} contabilizando duas parcelas de R${:.2f} no cartão sem juros!'.format(preco, parcelas))
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas você deseja pagar? '))
    per = preco * 20 / 100
    valor = preco + per
    vpar = valor / parcelas
    print('Sua compra de R${:.2f} ficou no valor de R${:.2f}, contabilizando em {} parcelas de R${:.2f} com juros.'.format(preco, valor, parcelas, vpar))
else:
    print('Opção de pagamento invalida.')
print('Obrigado pela preferencia!')

