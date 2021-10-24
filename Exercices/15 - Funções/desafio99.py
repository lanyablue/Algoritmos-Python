'''Faça um programa que tenha uma função chamada maior(), que receba varios parametros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é maior.'''

def maior(* nums):
    m = 0
    for valor in nums:
        if valor > m:
            m = valor
    print(f'O maior número é {m}')


maior(0, 4, 12, 7, 2)




