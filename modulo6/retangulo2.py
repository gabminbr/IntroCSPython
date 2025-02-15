def main():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))

    temp_alt = altura
    while temp_alt > 0:
        temp_larg = largura
        while temp_larg > 0:
            if (temp_alt == altura or temp_alt == 1):
                print("#", end="")
            elif (temp_larg == largura or temp_larg == 1):
                print("#", end="")
            else:
                print(" ", end="")
            temp_larg -= 1
        print()
        temp_alt -= 1


if __name__ == '__main__':
    main()
