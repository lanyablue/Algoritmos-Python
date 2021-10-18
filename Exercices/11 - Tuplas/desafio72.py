'''Crie um programa que tenha uma tupla totalmente preenchida com
uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrar-lo por extenso.'''

número = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
          'dezoito', 'dezenove', 'vinte')
continuar = 'S'
while continuar in 'Ss':
    while True:
        extenso = int(input('Digite um número entre 0 e 20 para mostra-lo por extenso: '))
        if 0 <= extenso <= 20:
            break
        print('Tente novamnte.', end=' ')
    print(f'Você digitou o número {número[extenso]}.')
    continuar = str(input('Você deseja continuar? ')).upper().strip()[0]
print('Programa finalizado!')