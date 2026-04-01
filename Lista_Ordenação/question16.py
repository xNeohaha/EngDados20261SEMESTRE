# Questão 16
# Realize uma análise de desempenho comparativa dos três algoritmos para 
# diferentes tamanhos de entrada 
# (n = 10, 50, 100, 500), usando o módulo timeit para medições precisas.

import random
import timeit

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

def testar(algoritmo, lista):
    copia = lista.copy()
    tempo = timeit.timeit(lambda: algoritmo(copia), number=1)
    return tempo


tamanhos = [10, 50, 100, 500]

for n in tamanhos:
    print(f"\n===== n = {n} =====")
    
    lista_base = random.sample(range(10000), n)
    
    for nome, algoritmo in [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
    ]:
        
        tempo = testar(algoritmo, lista_base)
        print(f"{nome}: {tempo:.6f} segundos")
