# Questão 2
# Implemente o algoritmo Merge Sort para ordenar uma lista de números inteiros em ordem crescente.

# merge_sort argumento
# se a len do argumento for maior ou igual a 1, retorna arr
# meio default: len(arr) //2
# esquerda merge_sort(arr[:meio])
# direita merge_sort(arr[meio:])
# return merge(esquerda,direita)

def merge_sort(arr):
    if len(arr) <= 1:
        return (arr)
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    return merge(esquerda,direita)
# merge
# resultado
# i = j = 0
    # while i menor que len esquerda e menor que j len direita
# se a esquerda for MENOR que a direita
# appen esquerda no resultado
# esquerda I sobe

# se não, #append direita j
# j sobe um
# extender para esquerda
# extender para direita

# retornar resultado
def merge(esquerda,direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
         resultado.append(direita[j])
         j +=1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


if __name__ == "__main__":
    lista = [9,6,4,3,8,7,1,2,0,5]
    ordenada = merge_sort(lista)
    print("Original: ",lista)
    print("Ordenada: ",ordenada)