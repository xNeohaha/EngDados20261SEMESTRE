def soma_lista(lista):
    total = 0
    for num in lista:  # percorre todos os n elementos
        total += num
    return total
def encontrar_maximo(lista):
    maximo = lista[0]
    for num in lista:  # O(n)
        if num > maximo:
            maximo = num
    return maximo