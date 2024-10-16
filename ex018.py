import math
ang = float(input('Digite o angulo que voce deseja : '))
seno = math.sin(math.radians(ang))
print('O angulo {} tem o seno de {:.2f}'.format(ang, seno))
cose = math.cos(math.radians(ang))
print('O angulo {} tem o cosseno de {:.2f}'.format(ang, cose))
tang = math.tan(math.radians(ang))
print('O angulo {} tem a tangente de {:.2f}'.format(ang, tang))

