'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
que ele foi multado
A multa vai custar R$7,00 por cada km acima do limite'''

v = int(input('Qual a sua velocidade em km/h na pista? '))
if v <= 80:
    print('Boa viagem')
else:
    print('Voce excedeu o limite de velocidade!')
    m = (v - 80) * 7
    print('Você foi multado em R${:.2f}!'.format(m))

