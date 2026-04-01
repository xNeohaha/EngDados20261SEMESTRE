# Questão 13
# Ordene uma lista de tuplas representando produtos (nome, preço, estoque) 
# usando Selection Sort, primeiro por preço crescente e depois por estoque decrescente.

def call_priority(produto):
    return (produto[1], -produto[2])


def selection_sort(lista):
    n = len(lista)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            if call_priority(lista[j]) < call_priority(lista[min_index]):
                min_index = j
        
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    
    return lista


lista = [
    ("Produto A", 10.99, 50),
    ("Produto B", 5.49, 30),    
    ("Produto C", 15.99, 20),
    ("Produto D", 8.99, 40),
]

ordenada = selection_sort(lista)

print("Lista ordenada:")
for produto in ordenada:
    print(produto)
