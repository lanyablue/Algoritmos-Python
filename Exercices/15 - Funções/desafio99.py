'''Faça um programa que tenha uma função chamada maior(), que receba varios parametros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é maior.'''

def maior(* nums):
    tam = len(nums)
    m = 0

    print('=-' * 20)
    print(f'Foram analisados {tam} números')
    for valor in nums:
        print(f'{valor} ', end='')
        if valor > m:
            m = valor
    print(f'\nO maior número é {m}')




maior(0, 4, 12, 7, 2)
maior(5, 6, 2, 4)
maior(4, 2)
maior()




