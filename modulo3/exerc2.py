n = int(input("Digite um número: "))
impares = 0
numero = 0
while impares < n:
    if numero % 2 != 0:
        print(numero)
        impares += 1
    numero += 1
