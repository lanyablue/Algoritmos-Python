'''Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
mostrando so 10 primeiros termos da progressão usando
a estrutura while'''

primeiro = int(input('Digite o primeiro termo da sua progressão: '))
razao = int(input('Digite o valor da razão: '))
décimo = primeiro + (10-1) * razao #formula de calcular o décimo termo da progressão
c = 0

while primeiro < décimo+1: #(primeiro, décimo + razao, razao):
    print(primeiro, end=' ')
    primeiro += razao
print('FIM')


primeiro = int(input('Digite o primeiro termo da sua progressão: '))
razao = int(input('Digite o valor da razão: '))
termo = primeiro
count = 1
while count <= 10:
    print('{}'.format(termo), end=' ')
    termo += razao
    count += 1
print('FIM')