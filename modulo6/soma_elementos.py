def soma_elementos(lista):
    '''
    (int Lista -> int)
    recebe como parâmetro uma lista de números inteiros
    e retorna a soma desses elementos
    '''

    soma = 0
    for i in range(0, len(lista), 1):
        soma += lista[i]
    
    return soma