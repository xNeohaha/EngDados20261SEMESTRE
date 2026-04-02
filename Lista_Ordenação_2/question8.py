# Questão 8
# Ordene uma lista de tuplas (idade, nome) usando Merge Sort. 
# A ordenação deve ser primariamente por idade (crescente) 
# e secundariamente por nome (alfabética crescente) para idades iguais..

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"({self.nome}, {self.idade})"


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if (esquerda[i].idade, esquerda[i].nome) < (direita[j].idade, direita[j].nome):
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


Lista = [
    Pessoa("João", 18),
    Pessoa("Maria", 22),
    Pessoa("Ana", 18),
    Pessoa("Carlos", 20),
    Pessoa("Beatriz", 32),
    Pessoa("Pedro", 20)
]

LO = merge_sort(Lista)

print("Original:", Lista)
print("Ordenada:", LO)
