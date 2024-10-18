import random
from random import randint

print('Jogo da sorte!')
nm = int(input('Digite um numero de 0 a 5 : '))
sorteio = randint(0, 5)

if nm == sorteio :
    print('Parabens voce ganhou!')
else:
    print('O computador vence! o numero sorteado foi {}'.format(sorteio))