cores = {'vermelho':'red','verde':'green','amarelo':'yellow'}
escolha = str(input('Escolha uma cor para traduzir: ')).lower()
print (cores.get( escolha,'esta cor não consta' ))