def bubbleSort(lista):
    n = len(lista)
    j = 0

    while j < n-1:
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
        j += 1
    return lista
