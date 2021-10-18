'''Escreva um programa que leia um numero inteiro qualquer
e peça ao usuario para escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal'''

num = int(input('Digite um número: '))
print('''Escolha qual tipo de conversão você deseja realizar no seu número:
[ 1 ] Número binário;
[ 2 ] Número octal;
[ 3 ] Número hexadecimal;''')
escolha = int(input('Qual conversão deseja realizar? '))
if escolha == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção de conversão inválida!')




