def busca_linear(lista, alvo):
    for i, item in enumerate(lista):
        if item == alvo:
            return i
    return -1
# n=1.000.000 → até 1M comparaçõe

def busca_binaria(lista, alvo):
    esq, dir = 0, len(lista)-1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esq = meio + 1
        else: dir = meio - 1
    return -1
# n=1.000.000 → apenas 20 comparações!