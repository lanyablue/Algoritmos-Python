'''Crie uma tupla preechida com os 20 primeiros colocados da tabela do
campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os ultimos 4 colocados da tabela
c) Uma lista com os times em ordem alfabética
d) em que posição na tabela está o time de Corinthians.'''

colocação = ('Palmeiras', 'Atlético - MG', 'Fortaleza', 'Bragantino', 'Athletico - PR', 'Flamengo',
             'Ceará', 'Bahia', 'Fluminense',
             'Santos', 'Atlético - GO', 'Corinthians', 'Internacional',
             'Juventude', 'São Paulo', 'Sport', 'América - MG',
             'Cuiabá', 'Grêmio', 'Chapecoense')
print(f'Lista de times do Campeonato Brasileiro: {colocação}')
print('='*80)
print(f'Os cinco primeiros colocados foram: {colocação[0:5]}')
print('='*80)
print(f'Os quatros ultimos colocados foram: {colocação[-4:]}')
print('='*80)
print(f'Os times em ordem alfabética apresentam-se: {sorted(colocação)}')
print('='*80)
#coripos = colocação.index('Corinthians')
print(f'O time Corinthians está na {colocação.index("Corinthians")+1}ª posição da colocação.')
