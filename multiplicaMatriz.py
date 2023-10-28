def multiplica_matriz(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    C = [[0 for j in range(len(A))] for i in range(len(A))]  # matriz de zeros

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                C[i][j] += A[i][k] * B[k][j]

    return C
