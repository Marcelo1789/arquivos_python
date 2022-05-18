import random
chute  = 0
choose = random.randint(0,1)
print ('Bem Vindo')
while chute != choose:
    chute = int(input('Chute um numero: '))
    if chute < choose:
        print ('baixo')
    elif chute > choose:
            print('alto')
else:
    print('acertou')
print ('fim do jogo')
    
            

