import math

x1 = int(input("Coordenada X do primeiro elemento: "))
y1 = int(input("Coordenada Y do primeiro elemento: "))
x2 = int(input("Coordenada X do segundo elemento: "))
y2 = int(input("Coordenada Y do segundo elemento: "))

distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if (distancia >= 10):
    print("longe")
else:
    print("perto")