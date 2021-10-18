'''Desenvolva um programa que leia o primeiro termo e a razão
de uma PA. No final, mostre os 10 primeiros
termos dessa progressão'''

primeiro = int(input('Digite o primeiro termo da sua progressão: '))
razao = int(input('Digite o valor da razão: '))
décimo = primeiro + (10-1) * razao #formula de calcular o décimo termo da progressão
for c in range(primeiro, décimo + razao, razao):
    print(c, end=' ')
print('FIM')
