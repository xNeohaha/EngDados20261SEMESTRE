# Questão 1 
# Implemente o algoritmo Quick Sort para ordenar uma lista de números inteiros em ordem crescente. 
# Utilize o último elemento como pivô.

def quicK_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot  = arr[-1]
    # pivot = arr[len(arr)//2]

    menores = [x for x in arr if x < pivot]
    iguais = [x for x in arr if x == pivot]
    maiores = [x for x in arr if x > pivot]
    return quicK_sort(menores) + iguais + quicK_sort(maiores)

if __name__ == "__main__":
    lista = [10,7,8,9,1,5]
    print("Original: ", lista)
    print("Ordenada: ",quicK_sort(lista))