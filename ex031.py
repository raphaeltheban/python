km = float(input('Digite quantos KM sera a viagem : '))

if km <= 200:
    print('Esta viagem de {} km ficara {:.2f}'.format(km , km * 0.50))

else:
    print('Esta viagem de {} km ficara {:.2f}'.format(km , km * 0.45))