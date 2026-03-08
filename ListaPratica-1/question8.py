# Questão 8 
# Usando uma classe, implemente um verificador de expressões com parênteses balanceados. 
# O programa deve receber uma expressão matemática como string e verificar se os parênteses estão corretamente balanceados. 
# Teste com pelo menos 4 expressões diferentes e explique o algoritmo com comentários.

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)


def verifica_balanceamento(ex):
    s = Stack()

    for caracter in ex:
        if caracter == '(':
            s.push(caracter)
        elif caracter == ')':
            if s.isEmpty():
                return False
            s.pop()

    return s.isEmpty()


conta = "3 - 6 x 8"

if verifica_balanceamento(conta):
    print("Balanceada")
else:
    print("Não balanceada")
