'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
imc e mostre seu status, de acordo a tabela:
-Entre 18.5 e 25: Peso ideal
-25 ate 30: sobrepeso
-30 ate 40: obesidade
-acima de 40: obesidade morbida'''

from time import sleep
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
print('Calculando seu IMC......')
sleep(3)
if imc < 18.5:
    print('Sua altura é {:.2f}cm, seu peso é {}KG, e seu IMC é {:.1f}, indicando que você está ABAIXO DO PESO!'.format(altura, peso, imc))
elif 18.5 <= imc < 25:
    print('Sua altura é {:.2f}cm, seu peso é {}KG, e seu IMC é {:.1f}, indicando que você está no PESO IDEAL!'.format(altura, peso, imc))
elif 25 <= imc < 30:
    print('Sua altura é {:.2f}cm, seu peso é {}KG, e seu IMC é {:.1f}, indicando que voce está SOBREPESO!'.format(altura, peso, imc))
elif 30 <= imc < 40:
    print('Sua altura é {:.2f}cm, seu peso é {}KG, e seu IMC é {:.1f}, indicando que você está na OBESIDADE!'.format(altura, peso, imc))
elif imc >= 40:
    print('Sua altura é {:.2f}cm, seu peso é {} KG, e seu IMC é {:.1f}, indicando que você está em estado de OBESIDADE MORBIDA!'.format(altura, peso, imc))

