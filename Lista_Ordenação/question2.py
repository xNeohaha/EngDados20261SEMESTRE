
# Questão 2 
# Utilize o Selection Sort para ordenar uma lista de nomes em ordem alfabética crescente.

def selection_sort(lista):
   n = len(lista)
   for i in range(n):
       min_index = i
       for j in range(i + 1, n):
           if lista[j] < lista[min_index]:
               min_index = j
           lista[i],lista[min_index] = lista[min_index],lista[i]
   return lista
       
   
  
lista = ["Leandro", "Otavio", "Moises", "Anderson"]
lo = selection_sort(lista)
print("Lista ordenada:", lo)