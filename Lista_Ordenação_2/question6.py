# Questão 6
# Implemente o Merge Sort para ordenar uma lista de strings em ordem alfabética crescente.

# merge_sort argumento
# se a len do argumento for maior ou igual a 1, retorna arr
# meio default: len(arr) //2
# esquerda merge_sort(arr[:meio])
# direita merge_sort(arr[meio:])
# return merge(esquerda,direita)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    meio = len(arr) //2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    return merge(esquerda,direita)

def merge(esquerda,direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i+=1
        else:
            resultado.append(direita[j])
            j+=1
          
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])                               
    return resultado

Lista = ["Liberto", "Junior", "Anthony", "Otavio", "Diego"]
LO = merge_sort(Lista)
print("Original: ",Lista)
print("Ordenada: ",LO)

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