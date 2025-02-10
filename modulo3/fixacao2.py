numero = int(input("Digite um número: "))
is_adjacente = False
while (numero != 0 and not is_adjacente):
    digito = numero % 10
    numero = numero // 10
    if (numero % 10 == digito):
        is_adjacente = True
if (is_adjacente):
    print("sim")
else:
    print("não")
