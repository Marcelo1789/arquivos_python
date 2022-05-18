import random
decide = 's' 
while decide == 's':
    decide = input('vamos jogar? S/N: ')
    dados = random.randint(1,6)
    print (dados)
else:
    print('fim')
