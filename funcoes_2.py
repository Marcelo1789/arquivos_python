def calcular_pagamento (qtd_hora,valor_taxa):
    horas = float(qtd_hora)
    taxa = float(valor_taxa)
    if horas <= 40:
        salario = horas*taxa
    else:
        h_extra = horas - 40
        salario = 40 * taxa + (h_extra * (1.5*taxa))
    return salario
str_horas = input ('Digite as horas trabalhadas: ')
str_taxa = input('Digite o valor da taxa: ')
total_salario = calcular_pagamento (str_horas,str_taxa)
print('O valor dos seus rendimentos é : ', total_salario)