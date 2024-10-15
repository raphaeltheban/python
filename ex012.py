preco = float(input('Qual o preço do produto ? '))
desc = preco*5/100
preco_novo = preco - desc

print('Seu produto de {} reccebeu {} de desconto e seu preco passou a ser {} '.format(preco,desc,preco_novo
                                                                                      ))