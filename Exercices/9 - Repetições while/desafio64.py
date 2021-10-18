'''Crie um programa que leia vários números inteiros pelo teclado.
O programa so vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando o flag)'''

soma = 0  #GAMBIARRA MALDITA, DONT DO IT
n = 0
count = 0
while n < 999:
    n = int(input('Digite um número: '))
    soma += n
    count += 1
soma -= 999
count -= 1
print('Sua repetição acabou, e a soma de todos os {} números é {}'.format(count, soma))


fim = False
soma = 0
count = 0
while not fim:
    n = int(input('Digite um valor para somar [999 para finalizar]: '))
    if n == 999:
        fim = True
    else:
        soma +=n
        count += 1
print('Sua repetição acabou, e a soma de todos os {} valores é {}.'.format(count, soma))


n = soma = count = 0   #SOLUÇÃO DO PROF
n = int(input('Digite um valor para somar [999 finaliza]: '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um valor para somar [999 finaliza]: '))
print('A soma de todos os {} valores informados é {}.'.format(count, soma))











