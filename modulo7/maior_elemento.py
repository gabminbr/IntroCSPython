def maior_elemento(lista):
    '''
    (int List -> int)
    recebe como parâmetro uma lista de inteiros e devolve
    o maior dentre eles
    '''
    maior = lista[0]
    for i in range(1, len(lista), 1):
        if (lista[i] > maior):
            maior = lista[i]
    
    return maior