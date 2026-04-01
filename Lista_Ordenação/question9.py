# Questão 9
# Implemente o Bubble Sort com a otimização da flag que interrompe o algoritmo quando nenhuma troca é realizada em uma passagem, 
# melhorando o desempenho no melhor caso.
def bubble_sort(elemento):
    n = len(elemento)
    for i in range(n):
        change = False
        print(f'Iteração {i+1} > {elemento}')
        
        for j in range(0, n - i - 1):
            if elemento[j] > elemento[j + 1]:
                elemento[j], elemento[j + 1] = elemento[j + 1], elemento[j]
                change = True
                print("  Resultado da troca:", elemento)
        if not change:
            print("Nenhuma troca realizada, lista já ordenada.")
            break      
    return elemento


lista = [1, 2, 3, 4, 5]
lo = bubble_sort(lista)
print("Lista ordenada:", lo)