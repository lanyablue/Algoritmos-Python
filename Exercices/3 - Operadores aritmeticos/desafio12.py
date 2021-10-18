p = float(input('Qual o preço do seu produto?'))
per = p * 5 / 100
ds = p - per
print('O produto com 5% de desconto equivale a {} reais, com um desconto de {} reais'.format(ds,per))

