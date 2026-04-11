from collections import deque

class Transacoes:
    def __init__(self):

        self.fila = deque()

    def enqueue(self, transacao):

        self.fila.append(transacao)

    def dequeue(self):

        if not self.esta_vazia():
            return self.fila.popleft()
        return "Fila vazia"

    def esta_vazia(self):
        return len(self.fila) == 0

    def __str__(self):

        return f"Fila de Transações: {list(self.fila)}"


f = Transacoes()
f.enqueue("Transação #001")
f.enqueue("Transação #002")
f.enqueue("Transação #003")

print(f"Removido: {f.dequeue()}") 
print(f) 