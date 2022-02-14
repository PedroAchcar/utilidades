from fatorialWhile import fatorial


def exponencial(x, m):
    i = 0
    exp = 0
    while i <= m:
        exp += x**i / fatorial(i)
        i += 1
    return exp
