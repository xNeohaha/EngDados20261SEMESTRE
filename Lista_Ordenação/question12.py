# Questão 12
# Implemente os três algoritmos e compare-os em termos de tempo de execução, 
# número de comparações e número de trocas para diferentes tamanhos de entrada.
import time
import random

def selection_sort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)
    
    for i in range(n):
        min_index = i
        
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[min_index]:
                min_index = j
        
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
            trocas += 1
            
    return comparacoes, trocas


def insertion_sort(lista):
    comparacoes = 0
    trocas = 0
    
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0:
            comparacoes += 1
            if lista[j] > chave:
                lista[j + 1] = lista[j]
                trocas += 1
                j -= 1
            else:
                break
                
        lista[j + 1] = chave
        
    return comparacoes, trocas


def bubble_sort(lista):
    comparacoes = 0
    trocas = 0
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                
    return comparacoes, trocas


def testar_algoritmo(algoritmo, lista):
    copia = lista.copy()
    
    inicio = time.perf_counter()
    comparacoes, trocas = algoritmo(copia)
    fim = time.perf_counter()
    
    tempo = fim - inicio
    
    return tempo, comparacoes, trocas

tamanhos = [10, 100, 500]

for tamanho in tamanhos:
    print(f"\n===== Tamanho da lista: {tamanho} =====")
    
    lista = random.sample(range(10000), tamanho)
    
    for nome, algoritmo in [
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Bubble Sort", bubble_sort),
    ]:
        
        tempo, comparacoes, trocas = testar_algoritmo(algoritmo, lista)
        
        print(f"\n{nome}:")
        print(f"  Tempo de execução: {tempo:.6f} segundos")
        print(f"  Comparações: {comparacoes}")
        print(f"  Trocas: {trocas}")
