# Questão 17
# Implemente um Selection Sort genérico 
# que aceite uma função de comparação customizada. Aplique-o para ordenar palavras por: 
# (a) comprimento crescente, 
# (b) número de vogais decrescente, 
# (c) ordem alfabética reversa.

def selection_sort(lista, compare):
    n = len(lista)
    
    for i in range(n):
        selected_index = i
        
        for j in range(i + 1, n):
            if compare(lista[j], lista[selected_index]):
                selected_index = j
        
        lista[i], lista[selected_index] = lista[selected_index], lista[i]
    
    return lista


palavras = ["banana", "uva", "abacaxi", "kiwi", "morango", "figo"]

def comp_tamanho(a, b):
    return len(a) < len(b)


def contar_vogais(p):
    return sum(1 for c in p.lower() if c in "aeiou")

def comp_vogais(a, b):
    return contar_vogais(a) > contar_vogais(b)


def comp_reverso(a, b):
    return a > b


print("Comprimento crescente:")
print(selection_sort(palavras.copy(), comp_tamanho))

print("\nVogais decrescente:")
print(selection_sort(palavras.copy(), comp_vogais))

print("\nOrdem alfabética reversa:")
print(selection_sort(palavras.copy(), comp_reverso))
