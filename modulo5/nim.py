def campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    resposta = int(input())
    print()

    placarUsuario = 0
    placarComputador = 0

    if(resposta == 1):
        ganhador = partida()
        if (ganhador == 1):
            print("O Computador ganhou!")
        else:
            print("Você ganhou!")
    else:
        print("Você escolheu campeonato!")
        i = 0
        while i < 3:
            print()
            print(f"***Rodada {i + 1}***")
            print()
            ganhador = partida()
            if(ganhador == 1):
                placarComputador += 1
            else:
                placarUsuario += 1
            i += 1
        print()
        print("Final do campeonato!")
        print(f"Placar: Você {placarUsuario} x {placarComputador} Computador")

def partida():
    '''
    (void) -> (int)
    executa a partida chamando as funções e intercalando-as de acordo com quem joga primeiro, e então, retorna
    o placar
    '''
    n = 0
    m = 0
    while(m >= n):
        n = int(input("Quantas peças? "))
        m = int(input("Limite de peças por jogada? "))  
    print()          

    ganhador = "computador"
    if (n % (m + 1) == 0):
        print("Você começa!")
        while(n != 0):
            pecas_retiradas = usuario_escolhe_jogada(n, m)
            n -= pecas_retiradas
            if(n == 0):
                ganhador = "usuario"
            pecas_retiradas = computador_escolhe_jogada(n, m)
            n -= pecas_retiradas
    else:
        print("Computador começa!")
        while(n != 0):
            if(n == 0):
                ganhador = "usuario"
            pecas_retiradas = computador_escolhe_jogada(n, m)
            n -= pecas_retiradas
            pecas_retiradas = usuario_escolhe_jogada(n, m)
            n -= pecas_retiradas
    
    if ganhador == "usuario":
        return 0
    else:
        return 1
    


def computador_escolhe_jogada(n, m):
    '''
    (int, int) -> (int)
    vai receber a quantidade de peças n e o limite de peças para retirar m, e retornar
    a quantidade de peças que o computador vai retirar de acordo com a estratégia vencedora
    '''
    if(n == 0):
        print("Você ganhou!")
        return 0
    
    possivel_jogada = 0
    i = 0
    achou_jogada = False

    while i < m: # esse loop vai buscar pelo maior valor até 'm' que é possivel fazer com que o numero de pecas restantes seja multiplo de m + 1
        if ((n - i) % (m + 1) == 0):
            possivel_jogada = i
            achou_jogada = True
        i += 1

    jogada = 0
    if achou_jogada:
        jogada = possivel_jogada
    else:
        jogada = m
    
    print(f"Computador tirou {jogada} peças")
    return jogada

def usuario_escolhe_jogada(n, m):
    '''
    (int, int) -> (int)
    recebe quantidade de peças n e limite de peças para retirar m, e recebe o input do usuario
    de qual vai ser a jogada, se for invalida ira se repetir ate ser uma jogada valida, e entao retorna
    o valor
    '''
    if (n == 0):
        print("Computador ganhou!")
        return 0

    jogada = int(input("Quantas peças você vai tirar? "))

    while (jogada > m or jogada < 1):
        print("Oops! Jogada inválida! Tente de novo.")
        jogada = int(input("Quantas peças você vai tirar? "))
    
    print(f"Você tirou {jogada} peças")
    return jogada

if __name__ == '__main__':
    campeonato()