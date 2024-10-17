from itertools import count

frase = input('Digite seu nome completo : ').strip()
print('Seu nome completo com as letras maiusculas : {}'.format(frase.upper()))
print('Seu nome completo em letras minusculas : {}'.format(frase.lower()))
print('Seu nome tem {} letras'.format(len(frase) - frase.count(' ')))
print('Seu primerio nome tem {} letras'.format(frase.find(' ')))