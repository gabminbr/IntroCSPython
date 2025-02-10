def maximo(x, y, z):
    if (x > y and x > z):
        return x
    if (y > z):
        return y
    else:
        return z
