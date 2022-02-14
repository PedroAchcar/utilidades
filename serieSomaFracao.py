def somaFracoes(n):
    serie = 0

    if n == 0:
        return 0

    for i in range(n):
        serie += 1/(i+1)
    return serie
