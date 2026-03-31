# Questão 19
# 19.	Implemente um sistema completo de ordenação de registros de alunos usando os três algoritmos. 
# Cada aluno possui: nome, matrícula, nota final e frequência. 
# Ordene por: (a) nota decrescente, 
# (b) frequência decrescente com desempate por nota, 
# (c) nome alfabético. 
# Compare o desempenho dos três algoritmos.

import random
import timeit


def bubble_sort(lista, chave):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if chave(lista[j]) > chave(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def selection_sort(lista, chave):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if chave(lista[j]) < chave(lista[min_index]):
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]


def insertion_sort(lista, chave):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and chave(lista[j]) > chave(atual):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual


def gerar_alunos(n):
    alunos = []
    for i in range(n):
        aluno = {
            "nome": "Aluno" + str(i),
            "matricula": 1000 + i,
            "nota": round(random.uniform(0, 10), 2),
            "frequencia": random.randint(50, 100)
        }
        alunos.append(aluno)
    return alunos


def por_nota(a):
    return -a["nota"]

def por_freq_nota(a):
    return (-a["frequencia"], -a["nota"])

def por_nome(a):
    return a["nome"]

def testar(algoritmo, alunos, criterio):
    tempo = timeit.timeit(
        lambda: algoritmo(alunos.copy(), criterio),
        number=3
    )
    return tempo / 3


tamanhos = [10, 50, 100]

for n in tamanhos:
    print(f"\n===== n = {n} =====")
    
    alunos = gerar_alunos(n)
    
    for descricao, criterio in [
        ("Nota decrescente", por_nota),
        ("Frequência decrescente (desempate nota)", por_freq_nota),
        ("Nome alfabético", por_nome),
    ]:
        
        print(f"\nCritério: {descricao}")
        
        for nome_alg, algoritmo in [
            ("Bubble", bubble_sort),
            ("Selection", selection_sort),
            ("Insertion", insertion_sort),
        ]:
            
            tempo = testar(algoritmo, alunos, criterio)
            print(f"{nome_alg}: {tempo:.6f} s")
