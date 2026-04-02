# Questão 4
# Implemente o Merge Sort para ordenar uma lista encadeada simples. 
# A função deve receber o nó cabeça da lista e retornar o nó cabeça da lista ordenada.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def __repr__(self):
        return str(self.valor)


def merge_sort(cabeca):
    if cabeca is None or cabeca.proximo is None:
        return cabeca

    meio = dividir(cabeca)

    esquerda = merge_sort(cabeca)
    direita = merge_sort(meio)

    return merge(esquerda, direita)


def dividir(cabeca):
    lento = cabeca
    rapido = cabeca.proximo

    while rapido and rapido.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo

    meio = lento.proximo
    lento.proximo = None
    return meio


def merge(esquerda, direita):
    if esquerda is None:
        return direita
    if direita is None:
        return esquerda

    if esquerda.valor < direita.valor:
        resultado = esquerda
        resultado.proximo = merge(esquerda.proximo, direita)
    else:
        resultado = direita
        resultado.proximo = merge(esquerda, direita.proximo)

    return resultado


# Criando lista: 4 -> 2 -> 1 -> 3

n1 = No(4)
n2 = No(2)
n3 = No(1)
n4 = No(3)

n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

print("Original:")
atual = n1
while atual:
    print(atual.valor, end=" -> ")
    atual = atual.proximo

cabeca_ordenada = merge_sort(n1)

print("\nOrdenada:")
atual = cabeca_ordenada
while atual:
    print(atual.valor, end=" -> ")
    atual = atual.proximo
