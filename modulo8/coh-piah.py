import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = str(palavra).lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = str(palavra).lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(0, len(as_a), 1):
        soma += abs(as_a[i] - as_b[i])
    
    grau_similaridade = soma / 6
    return grau_similaridade

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = separa_frases(texto)
    palavras = separa_palavras(texto)

    tamanho_medio_palavras = soma_caracteres_generico(palavras) / len(palavras)
    type_token = n_palavras_diferentes(palavras) / len(palavras)
    hapax_legomana = n_palavras_unicas(palavras) / len(palavras)
    tamanho_medio_sentenca = soma_caracteres_generico(sentencas) / len(sentencas)
    complexidade_sentenca = len(frases) / len(sentencas)
    tamanho_medio_frases = soma_caracteres_generico(frases) / len(frases)

    assinatura = [tamanho_medio_palavras, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frases]

    return assinatura

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor_similaridade = compara_assinatura(ass_cp, calcula_assinatura(textos[0]))
    indice_texto = 0
    for i in range(1, len(textos), 1):
        similaridade_atual = compara_assinatura(ass_cp, calcula_assinatura(textos[i]))
        if (similaridade_atual < menor_similaridade):
            menor_similaridade = similaridade_atual
            indice_texto = i
    
    return indice_texto + 1
    

def soma_caracteres_generico(objeto):
    '''Recebe uma determinada lista e retorna o numero de caracteres'''
    soma = 0
    for i in range(0, len(objeto), 1):
        soma += len(objeto[i])

    return soma