# Questão 10
# Implemente o Bubble Sort para ordenar uma lista de floats (notas de alunos) em ordem decrescente.
def bubble_sort(elemento):
    n = len(elemento)
    for i in range(n):
        print(f'Iteração {i+1} > {elemento}')
        
        for j in range(0, n - i-1):
            if elemento[j] < elemento[j + 1]:
                elemento[j], elemento[j + 1] =  elemento[j + 1],elemento[j]
                print("  Resultado da troca:", elemento)
    return elemento

lista = [1, 2, 3, 4, 5]
lo = bubble_sort(lista)
print("Lista ordenada:", lo)