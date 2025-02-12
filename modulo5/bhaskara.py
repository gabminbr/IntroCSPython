import math

def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)

def delta(b, a, c):
    '''
    (float, float, float) -> (float)
    recebe os 3 parametros da funcao quadratica, e calcula o valor de delta e retorna seu valor.
    '''
    delta = b ** 2 - 4 * a * c
    return delta

def imprime_raizes(a, b, c):
    '''
    (float, float, float) -> print
    essa função recebe os 3 parametros e calcula o valor das raizes de acordo com o valor de delta fornecido pela funcao
    delta()
    '''
    delta = delta(a, b, c)
    if delta < 0:
        print("Esta função não possui raízes no campo dos reais!")
    elif delta == 0:
        raiz = -b / 2*a
        print("Esta função tem a raíz dupla com o valor de:", raiz)
    else:
        raiz1 = -b + math.sqrt(delta) / 2 * a
        raiz2 = -b - math.sqrt(delta) / 2 * a
        if (raiz2 < raiz1):
            aux = raiz2
            raiz2 = raiz1
            raiz1 = aux
        print("As raizes são:", raiz1, raiz2)

if __name__ == '__main__':
    main()
