def hanoi(n: int, origem: str, destino: str, trabalho: str):
    if n > 0:
        hanoi(n-1, origem, trabalho, destino)
        print(f'{n} : {origem} -> {destino}')
        hanoi(n-1, trabalho, destino, origem)


hanoi(3, 'A', 'C', 'B')
