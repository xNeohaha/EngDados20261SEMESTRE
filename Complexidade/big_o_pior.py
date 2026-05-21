def busca_linear(lista, alvo):
    for item in lista:      # n iterações
        if item == alvo:
            return True
    return False
# Complexidade: O(n)
# Exemplo de uso    
lista = [1, 2, 3, 4, 5]
print(busca_linear(lista, 3))  # True
print(busca_linear(lista, 6))  # False