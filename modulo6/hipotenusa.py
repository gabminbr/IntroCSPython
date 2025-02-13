def soma_hipotenusas(n):
    possivel_hipotenusa = 1
    soma = 0
    while (possivel_hipotenusa <= n):
        if (is_hipotenusa(possivel_hipotenusa)):
            soma += possivel_hipotenusa
        possivel_hipotenusa += 1
    return soma


def is_hipotenusa(n):
    i = 1
    while (i <= n):
        j = 1
        while (j <= n):
            if (n ** 2 == i ** 2 + j ** 2):
                return True
            j += 1
        i += 1
    return False
