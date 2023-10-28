def fatorial_inteiro(n: int) -> int:
    fat = 1

    for i in range(1, n+1):
        fat *= i

    return fat


def fatorial_lista(n: int) -> list:
    fat = [1]

    for i in range(1, n+1):
        fat.append(i * fat[i-1])

    return fat
