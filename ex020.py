import random
n1 = str(input('Nome do Primeiro aluno : '))
n2 = str(input('Nome do Segundo aluno : '))
n3 = str(input('Nome do Terceiro aluno : '))
n4 = str(input('Nome do Quarto aluno : '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação é ;')
print(lista)
