def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))

    while altura > 0:
        temp_larg = largura
        while temp_larg > 0:
            print("#", end="")
            temp_larg -= 1
        print()
        altura -= 1


if __name__ == '__main__':
    main()
