'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço  da passagem, cobrando R$0,50 por KM para viagens
de até 200km e R$0,45 para viagens mais longas.'''

d = float(input('Qual a distancia da sua viagem? '))
curta = d * 0.50
longa = d * 0.45
print('Sua viagem terá {}km'.format(d))
if d <= 200:
    print('O valor da passagem de sua viagem será R${:.2f}.'.format(curta))
else:
    print('O valor da passagem de sua viagem será R${:.2f}.'.format(longa))
print('Boa viagem!')


'''d = float(input('Qual a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {}km.'.format(d))
preco = d * 0.50 if d <= 200 else d * 0.45
print('E o preço de sua passagem será R${:.2f}.'.format(preco))
