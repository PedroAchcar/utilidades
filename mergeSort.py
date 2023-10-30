def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0

    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1

        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1

        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1

        else:
            lista[k] = right[top_right]
            top_right += 1


def merge_sort(lista: list, inicio: int = 0, fim: int = None) -> list:
    if fim is None:
        fim = len(lista)

    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

    return lista
