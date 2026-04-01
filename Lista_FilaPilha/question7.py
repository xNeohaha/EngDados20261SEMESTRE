# Questão 7 
# Implemente em Python uma Fila de Prioridades. 
# Cada item possui uma prioridade inteira (menor número = maior prioridade). 
# Métodos obrigatórios: enqueue (item, prioridade), dequeue(), exibir(), isEmpty().
# Demonstre com uma fila de atendimento médico: pacientes com prioridades 1 (urgente), 2 (moderado) e 3 (normal), chamando-os em ordem de prioridade.

class Queue:
    def __init__(self):
        self.items = []

        # transforma os numeros da proioridade em uma String.
        self.prioridades = {
            1: "Urgente",
            2: "Moderado",
            3: "Normal"
        }

    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, nome, prioridade):
        self.items.append((prioridade, nome))
        self.items.sort()  # organiza pela prioridade
    
    def dequeue(self):
        prioridade, nome = self.items.pop(0)
        return nome
    
    def exibir(self):
        lista = []
        for prioridade, nome in self.items:
            lista.append((nome, self.prioridades[prioridade]))
        return lista
    
    def size(self):
        return len(self.items)


q = Queue()

print(q.isEmpty())

q.enqueue("Matheus", 1)
q.enqueue("Gabriel", 2)
q.enqueue("Gustavo", 3)
q.enqueue("Lucas", 3)

print(q.isEmpty())
print(q.exibir())