def inverte_sequencia():
    n = int(input("Digite um numero terminado em 0: "))
    numeros = []
    while (n != 0):
        numeros.append(n)
        n = int(input("Digite um numero terminado em 0: "))

    i = len(numeros) - 1
    while (i >= 0):
        print(numeros[i])
        i -= 1

if __name__ == '__main__':
    inverte_sequencia()