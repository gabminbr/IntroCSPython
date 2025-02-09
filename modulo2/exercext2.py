import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b ** 2 - 4 * a * c

if (delta > 0):
    raiz1 = ((b * -1) + math.sqrt(delta)) / 2 * float(a)
    raiz2 = ((b * -1) - math.sqrt(delta)) / 2 * float(a)
    if (raiz1 > raiz2):
        aux = raiz2
        raiz2 = raiz1
        raiz1 = aux
    print(f"as raízes da equação são {raiz1} e {raiz2}")
elif (delta == 0):
    raiz = (b * -1) / 2 * float(a)
    print(f"a raiz dupla desta equação é {raiz}")
else:
    print("esta equação não possui raízes reais")