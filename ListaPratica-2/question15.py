# Questão 15
# Aplique o Bubble Sort para ordenar cada linha de uma matriz 4×4 e, 
# em seguida, ordene a primeira coluna da matriz resultante.

def bubble_sort(linha):
    n = len(linha)
    for i in range(n):
        for j in range(0, n - i - 1):
            if linha[j] > linha[j + 1]:
                linha[j], linha[j + 1] = linha[j + 1], linha[j]


def ordenar_linhas(matriz):
    for linha in matriz:
        bubble_sort(linha)


def ordenar_primeira_coluna(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(0, n - i - 1):
            if matriz[j][0] > matriz[j + 1][0]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]


# Matriz 4x4
matriz = [
    [4, 3, 2, 1],
    [8, 6, 7, 5],
    [9, 12, 11, 10],
    [16, 14, 15, 13]
]

print("Matriz original:")
for linha in matriz:
    print(linha)

ordenar_linhas(matriz)

print("\nApós ordenar cada linha:")
for linha in matriz:
    print(linha)

ordenar_primeira_coluna(matriz)

print("\nApós ordenar a primeira coluna:")
for linha in matriz:
    print(linha)
