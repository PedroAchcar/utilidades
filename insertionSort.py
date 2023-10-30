def insertion_sort(lista: list) -> list:
    for i in range(1, len(lista)):
        item = lista[i]
        j = i - 1

        while j >= 0 and item < lista[j]:
            lista[j+1] = lista[j]
            j -= 1

        lista[j+1] = item

    return lista
