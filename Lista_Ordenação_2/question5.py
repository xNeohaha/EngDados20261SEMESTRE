# Questão 5
# Crie uma classe Produto com atributos nome (string) e preco (float). 
# Implemente o Quick Sort para ordenar uma lista de objetos Produto primeiramente por preco (crescente) 
# e, em caso de preços iguais, por nome (alfabética crescente).
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __repr__(self):
        return f"({self.nome}: R${self.preco:.2f})"
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    
    menores = [x for x in arr if x.preco < pivot.preco or (x.preco == pivot.preco and x.nome < pivot.nome)]
    iguais = [x for x in arr if x.preco == pivot.preco and x.nome == pivot.nome]
    maiores = [x for x in arr if x.preco > pivot.preco or (x.preco == pivot.preco and x.nome > pivot.nome)]

    return quick_sort(menores) + iguais + quick_sort(maiores)


Lista = [
    Produto("Coxinha", 3.00),
    Produto("Pepsi 500ML", 5.00),
    Produto("Quibe", 3.00),
    Produto("Pastel Bauru", 7.00),
    Produto("Coca Cola 500ML", 5.50),
    Produto("Enroladinho de Salsicha", 3.00)
]
LO = quick_sort(Lista)
print("Original: ", Lista)
print("Ordenada: ", LO)