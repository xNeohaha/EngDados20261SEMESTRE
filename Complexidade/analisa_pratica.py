def exemplo(lista):
    n = len(lista)           # O(1)
    soma = 0
    for i in range(n):       # O(n)
        soma += lista[i]
    for i in range(n):       # O(n)
        for j in range(n):   # O(n)
            if lista[i] == lista[j]:
                print(i, j)
    return soma