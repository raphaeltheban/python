salario = float(input('Digite seu salario para receber o aumento: '))

if salario > 1250.00:
    print('Seu aumento vai ser de 10% que sera de {:.2f}'.format(salario*10/100))
else:
    print('Seu aumento vai ser de 15% que sera de {:.2f}'.format(salario*15/100))