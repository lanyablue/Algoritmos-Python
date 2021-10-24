def título(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


# programa principal
título('   CURSO EM VIDEO')  # colocou dentro do parametro msg
título('   PYTHON É MUITO BOM!')   # ''
título('   Oi')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


# programa principal
soma(4, 5)
soma(8, 9)
soma(a=2, b=1)  # explicitação


def contador(*núm):   # desempacotamento
    # for valor in núm:
    #    print(f'{valor} ', end='')
    # print('FIM!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 4, 4, 4)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]  *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)



def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(4, 5)
soma(9, 2, 3, 4)





