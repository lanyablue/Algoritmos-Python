"""Faça um programa que tenha uma função chamada escreva(), que recebe
um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel
Ex:
escreva('Olá mundo')
Saida:
------------
 Olá mundo
------------
"""



def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'{msg:^{tam}}')
    print('-' * tam)


escreva('Oi')
escreva('Infernal do caralho')