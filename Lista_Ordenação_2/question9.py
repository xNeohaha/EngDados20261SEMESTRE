# Questão 9
# Implemente o Quick Sort de forma iterativa (não recursiva) usando uma pilha explícita 
# para gerenciar as chamadas de partição. 
# Isso pode ajudar a evitar estouro de pilha para listas muito grandes.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]

    while stack:
        inicio, fim = stack.pop()

        if inicio < fim:
            pivot_index = partition(arr, inicio, fim)

            stack.append((inicio, pivot_index - 1))
            stack.append((pivot_index + 1, fim))

    return arr


def partition(arr, inicio, fim):
    pivot = arr[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    lista = [10,7,8,9,1,5]
    print("Original: ", lista)
    print("Ordenada: ",quick_sort(lista))