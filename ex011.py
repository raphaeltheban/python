larg = float(input('Qual a largura da parede ? '))
alt = float (input('qual a altura da parede ? '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua area é de {}'.format(larg,alt,area))
tinta = area / 2
print ('Para pintar essa parede voce precisa de {} litros de tinta'.format(tinta))