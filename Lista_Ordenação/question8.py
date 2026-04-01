# Questão 8
# Implemente o Bubble Sort clássico para ordenar uma lista de inteiros, 
# exibindo cada passagem completa pelo array.
def bubble_sort(elemento):
    n = len(elemento)
    
    for i in range(n):
        print(f'Iteração {i+1} > {elemento}')
        
        for j in range(0, n - i - 1):
            if elemento[j] > elemento[j + 1]:
                elemento[j], elemento[j + 1] = elemento[j + 1], elemento[j]
                print("  Resultado da troca:", elemento)
                
    return elemento


lista = [2, -5, 7, 90, 1]
lo = bubble_sort(lista)
print("Lista ordenada:", lo)