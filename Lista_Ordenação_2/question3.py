# Questão 3
# Modifique a implementação do Quick Sort para escolher um pivô aleatoriamente.

import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    print("Pivot: ", pivot)

    menores = [x for x in arr if x < pivot]
    iguais = [x for x in arr if x == pivot]
    maiores = [x for x in arr if x > pivot]

    return quick_sort(menores) + iguais + quick_sort(maiores)


if __name__ == "__main__":
    lista = [10,7,8,9,1,5]
    print("Original: ", lista)
    print("Ordenada: ",quick_sort(lista))