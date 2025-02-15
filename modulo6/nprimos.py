def n_primos(n):
    primos = 1
    qtd_primos = 0
    while primos < n:
        i = 2
        primo = True
        while (primos % i != 0 and i <= primos // 2):
            i += 1
        if (primos % i != 0):
            qtd_primos += 1
        primos += 1
    return qtd_primos
