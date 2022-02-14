def insertionSort(lista):
    for i in range(1, len(lista)):
        j = i-1
        prox_elemento = lista[i]

        while (lista[j] > prox_elemento) and (j >= 0):
            lista[j+1] = lista[j]
            j = j-1
            lista[j+1] = prox_elemento
    return lista
