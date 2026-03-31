# Questão 11
# Instrumente o Bubble Sort para contar separadamente o número de comparações e trocas, 
# e exiba um relatório de desempenho.
def bubble_sort(elemento):
    n = len(elemento)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        print(f'Iteração {i+1} > {elemento}')
        
        for j in range(0, n - i-1):
            comparacoes += 1
            if elemento[j] < elemento[j + 1]:
                elemento[j], elemento[j + 1] =  elemento[j + 1],elemento[j]
                trocas += 1
                print("  Resultado da troca:", elemento)
    print(f"Relatório de desempenho:")
    print(f"  Número de comparações: {comparacoes}")
    print(f"  Número de trocas: {trocas}")
    return elemento

lista = [1, 2, 3, 4, 5]
lo = bubble_sort(lista)
print("Lista ordenada:", lo)