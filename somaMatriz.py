def soma_matriz(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    C = []

    for i in range(len(A)):
        linha = []

        for j in range(len(A[0])):
            linha.append(A[i][j] + B[i][j])

        C.append(linha)
    return C
