# Questão 14
# Implemente o Insertion Sort em uma lista encadeada, sem usar arrays auxiliares.


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None


def insertion_sort(head):
    sorted_head = None  # início da lista ordenada
    
    atual = head
    
    while atual:
        proximo = atual.next  # guarda o próximo
        
        # inserir atual na lista ordenada
        if sorted_head is None or atual.valor < sorted_head.valor:
            atual.next = sorted_head
            sorted_head = atual
        else:
            temp = sorted_head
            while temp.next and temp.next.valor < atual.valor:
                temp = temp.next
            
            atual.next = temp.next
            temp.next = atual
        
        atual = proximo
    
    return sorted_head

def criar_lista(valores):
    head = Node(valores[0])
    atual = head
    
    for v in valores[1:]:
        atual.next = Node(v)
        atual = atual.next
    
    return head

def imprimir_lista(head):
    atual = head
    while atual:
        print(atual.valor, end=" -> ")
        atual = atual.next
    print("None")

valores = [4, 2, 1, 3]

head = criar_lista(valores)

print("Lista original:")
imprimir_lista(head)

head = insertion_sort(head)

print("Lista ordenada:")
imprimir_lista(head)

