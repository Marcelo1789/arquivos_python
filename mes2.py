meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubto','novembro','dezembro')
data_nasc = input('Digite a sua data de nascimento no formato DD-MM-AAAA:')
indice = int (data_nasc[3:4])
mes = meses[indice]
print ('Voce nasceu no mês de', mes)
