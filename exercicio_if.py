from http.client import NOT_ACCEPTABLE
from re import M


nome = str(input('Digite seu nome: '))
nota1 = float(input('Digite a sua nota da prova 1: '))
nota2 = float(input('Digite a sua nota da prova 2: '))
faltas = int(input('Digite o numero de faltas: '))
media = (nota1 + nota2)/2
assid = 100 - (faltas/20)*100

print ("aluno(a): ",nome)
print ('Sua média foi:',media)
print ('Sua presença foi de: ', assid,'%')
if media<=6 and assid<70:
    print ('Reprovado por média e faltas')
elif media < 6:
    print ('reprovado por média')
elif assid<70:
    print('reprovado por faltas')
else:
     print ('Aprovado')
