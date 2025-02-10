numero = int(input("Digite um número inteiro: "))
i = 2
primo = True
while (i <= numero // 2 and primo):
    if (numero % i == 0):
        primo = False
    i += 1
if (primo):
    print("primo")
else:
    print("não primo")
