a = float(input('Qual a altura da sua parede?' ))
l = float(input('Qual a largura da sua parede?'))
ar = a * l
print('A dimensão de sua parede é de {}x{} e sua area equivale a {}m2'.format(a,l,ar))
t = ar / 2
print('Você precisará de {}l de tinta para pintar essa parede'.format(t))

