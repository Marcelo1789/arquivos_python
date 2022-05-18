meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubto','novembro','dezembro')
nasc = input('Digite a data do seu nascimento no formato DD-MM-AAAA: ')
indice = int(nasc[3:4])
mes = meses[indice]
print ('Você nasceu no mes de',mes)
