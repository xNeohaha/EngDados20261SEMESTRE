# Questão 5
# Implemente o Selection Sort instrumentado para contar o número de trocas realizadas. 
# Exiba a lista ordenada e o total de trocas.
def insertion_sort(lista):
   for i in range(1, len(lista)):
       chave = lista[i]
       j = i - 1
       print("j: ", lista[j])
       while j >= 0 and lista[j] > chave:
           lista[j + 1] = lista[j]
           print("j: ", lista[j])
           j -= 1
           print("j: ", lista[j])
       lista[j + 1] = chave
       print("j: ", lista[j])
# Exemplo de uso
lista = [5, 2, 8, 12, 1, 7]
insertion_sort(lista)
print(lista) # Output: [1, 2, 5, 7, 8, 12]