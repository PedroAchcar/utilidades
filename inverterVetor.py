from math import ceil


def inverter_vetor(vetor: list) -> list:
    n = len(vetor)

    for i in range(ceil(n/2)-1):
        temp = vetor[i]
        vetor[i] = vetor[n-i-1]
        vetor[n-i-1] = temp

    return vetor
