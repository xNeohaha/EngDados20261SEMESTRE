# Questão 7
# Implemente o Quick Sort utilizando a "mediana de três" como estratégia para escolher o pivô. 
# Isso envolve selecionar o elemento do meio, o primeiro e o último, e usar a mediana desses três como pivô, 
# trocando-o para a posição final antes do particionamento.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Mediana de três
    primeiro = arr[0]
    meio = arr[len(arr) // 2]
    ultimo = arr[-1]

    pivot = sorted([primeiro, meio, ultimo])[1]
    arr.remove(pivot)
    arr.append(pivot)

    menores = []
    maiores = []


    for x in arr[:-1]:
        if x <= pivot:
            menores.append(x)
        else:
            maiores.append(x)

    return quick_sort(menores) + [pivot] + quick_sort(maiores)

if __name__ == "__main__":
    lista = [10,7,8,9,1,5]
    print("Original: ", lista)
    print("Ordenada: ",quick_sort(lista))