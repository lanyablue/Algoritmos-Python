'''Faça um programa que leia o sexo de uma pessoa, mas só aceite
M ou F. Caso esteja errado, peça a digitação novamente ate
ter um valor correto.'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
    if sexo == 'F' or 'M':
        sexo = sexo
    if sexo != 'M' and sexo != 'F':
        print('Digite novamente um valor válido!')
print('Seu sexo {} foi registrado!'.format(sexo))


sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print('Seu sexo {} foi registrado com sucesso.'.format(sexo))