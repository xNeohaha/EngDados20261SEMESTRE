# Questão 3
# Modifique o Selection Sort para ordenar uma lista de inteiros em ordem decrescente, 
# selecionando sempre o maior elemento.

def selection_sort(lista):
   n = len(lista)
   for i in range(n):
       min_index = i
       for j in range(i + 1, n):
           if lista[j] > lista[min_index]:
               min_index = j
           lista[i],lista[min_index] = lista[min_index],lista[i]
   return lista
      
  
  
lista = [6,5,8,1,3,4,5,2,7,8,9,10,17,12]
lo = selection_sort(lista)
print("Lista ordenada:", lo)