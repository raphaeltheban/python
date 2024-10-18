vl = int(input('Digite a velocidade que o carro passou : '))

if vl <= 80 :
    print('Dentro da velocidade permitida!')
else:
    multa = (vl - 80) * 7
    print('Voce excedeu a velocidade limite permitida que é 80!')
    print('Deve pagar uma multa de {:.2f}'.format(multa))
    print('Dirija com cuidado para evitar as multas!')