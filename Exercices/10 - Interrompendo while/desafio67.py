'''Faça um programa que mostre a tabuada de vários números, um de cada
vez, para cada valor digitado pelo usuário. O programa será intenrrompido quando o número
solicitado for negativo.'''

tabuada = count = 0
while True:
    n = int(input('Digite um valor para obter sua tabuada: '))
    print('~'*15)
    if n < 0:
        break
    while True:
        count += 1
        print(f'{n} x {count} = {n*tabuada}')
        if count == 10:
            count = 0
            break
    print('~' * 15)
print('Acabou')