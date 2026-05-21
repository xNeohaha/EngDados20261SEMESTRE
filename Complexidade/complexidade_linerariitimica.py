def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esq = merge_sort(lista[:meio])
    dir = merge_sort(lista[meio:])
    return merge(esq, dir)