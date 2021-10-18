'''Crie um programa que tenha uma tupla unica com nomes de produtos
e seus respectivos preços na sequencia. No final, mostre uma listagem
de preços, organizando os dados em forma tabular.'''

maquiagemfentybeauty = ('Base Líquida', 179.00, 'Blush', 129.00, 'Corretivo', 145.00,
                        'Contorno', 159.00, 'Pincel', 129.00, 'Gloss', 119.00,
                        'Iluminador', 229.00, 'Paleta de Sombras', 159.00,
                        'Batom', 139.00, 'Máscara de Cílius', 79.00, 'Primer', 209.00,
                        'Esponja', 129.00, 'Delineador', 139.00, 'Pó Compacto', 199.00)
print('-'*40)
print(f"{'MAQUIAGENS FENTYBEAUTY':^40}")
print('-'*40)

for pos in range(0, len(maquiagemfentybeauty)):
    if pos % 2 == 0:
        print(f'{maquiagemfentybeauty[pos]:.<30}', end='')
    else:
        print(f'R${maquiagemfentybeauty[pos]:>7.2f}')
print('-'*40)
