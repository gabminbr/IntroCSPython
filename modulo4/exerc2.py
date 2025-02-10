def maior_primo(x):
    numero_primo = x
    while (numero_primo >= 2 and not primo(numero_primo)):
        numero_primo -= 1
    return numero_primo


def primo(n):
    i = 2
    primo = True
    while (i < (n // 2) and primo):
        if n % i == 0:
            primo = False
        i += 1
    return primo
