numero = int(input("Digite um número: "))

soma = 0
while (numero != 0):
    soma = soma + (numero % 10)
    numero = numero // 10
print(soma)
