# Questão 7
# Use o Insertion Sort para ordenar uma lista de nomes de cidades brasileiras em ordem alfabé
def insertion_sort(lista): # insertion sort
   for i in range(1,len(lista)):
       chave = lista[i]
       j = i-1
       while j >= 0 and lista[j] > chave:
           lista[j+1] = lista[j]
           j -= 1
           lista[j+1] = chave
 
 
 
lista = ["São Paulo", "Santos", "Brumado", "Praia Grande", "Atibaia", "Osasco"]       
insertion_sort(lista)
print(lista)