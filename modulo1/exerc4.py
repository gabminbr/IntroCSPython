segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias_em_segundos = 86400
horas_em_segundos = 3600
minutos_em_segundos = 60

# ao pegar a parte inteira da divisao de segundos pela unidade em questao,
# achamos quantas vezes ela coube dentro do total de segundos, e depois
# subtraimos de segundos a quantidade da unidade que foi possivel
dia_convertido = segundos // dias_em_segundos
segundos = segundos - dias_em_segundos * dia_convertido

hora_convertida = segundos // horas_em_segundos
segundos = segundos - horas_em_segundos * hora_convertida

minuto_convertido = segundos // minutos_em_segundos
segundos = segundos - minutos_em_segundos * minuto_convertido

print(f"{dia_convertido} dias, {hora_convertida} horas, {minuto_convertido} minutos e {segundos} segundos")