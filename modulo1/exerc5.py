numero = int(input("Digite um número inteiro: "))

# pega os numeros correspondentes a dezena e unidade respectivamente
# do numero original, e depois pega apenas o valor de dezena
dezena = numero % 100
digito_dezena = dezena // 10

print(f"O dígito das dezenas é {digito_dezena}")