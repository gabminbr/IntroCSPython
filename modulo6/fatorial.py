def main():
    n = int(input("Digite um número inteiro: "))
    while n >= 0:
        resultado_fatorial = fatorial(n)
        print(resultado_fatorial)
        n = int(input("Digite um número inteiro: "))


def fatorial(n):
    '''
    (int) -> (int)
    retorna o fatorial do numero 'n'
    '''
    fatorial = 1
    while n > 1:
        fatorial *= n
        n -= 1
    return fatorial


if __name__ == '__main__':
    main()
