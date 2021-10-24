def mostraLinha():  # sem parametro
    print('-' * 30)


# programa principal
mostraLinha()
print('   CURSO EM VIDEO   ')
mostraLinha()
mostraLinha()
print('   APRENDA PYTHON   ')
mostraLinha()
mostraLinha()
print('        ERROR       ')
mostraLinha()


def soma(a, b):     # parametro
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre {a} + {b} = {s}')


soma(a=4, b=5)
soma(10, 5)


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!')


contador(5, 5, 5, 5, 5, 5, 7)
contador(2, 4)
contador(1, 2, 3, 4, 5, 6)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [9, 3, 4, 5, 7, 2]
dobra(valores)
print(valores)



def soma(* valores):
    s = 0
    for itens in valores:
        s += itens
    print(f'A soma dos valores {valores} é {s}')



soma(4, 5, 2)
soma(2, 2)



