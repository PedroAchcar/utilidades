def bubble_sort(lista: list) -> list:
    for i in range(1, len(lista)):
        for j in range(1, len(lista)):
            if lista[j] < lista[j-1]:
                lista[j-1], lista[j] = lista[j], lista[j-1]

    return lista
