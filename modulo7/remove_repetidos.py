def remove_repetidos(lista):
    '''
    (int List -> int List)
    recebe uma lista de números inteiros e devolve a lista
    sem numeros repetidos
    '''
    
    
    lista_sem_repeticao = []
    
    for i in range(0, len(lista), 1):
        repetido = False
        if lista[i] in lista_sem_repeticao:
            repetido = True
        
        if(not repetido):
            lista_sem_repeticao.append(lista[i])
    
    return sorted(lista_sem_repeticao)