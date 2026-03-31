# Questão 4
# Implemente o Selection Sort instrumentado para contar o número de trocas realizadas. 
# Exiba a lista ordenada e o total de trocas.


def selection_sort(lista):
   n = len(lista)
   count = 0
   for i in range(n):
       min_index = i
       count+=1
       for j in range(i + 1, n):
           if lista[j] < lista[min_index]:
               min_index = j
           lista[i],lista[min_index] = lista[min_index],lista[i]
   return lista, count
      
  
  
lista = [6,5,8,1,3,4,5,2,9,10,11,14,13]
lo, count = selection_sort(lista)
print("Lista ordenada:", lo, 'Quantidade: ', count)