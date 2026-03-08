# Questão 4 
# Usando uma classe (com métodos enqueue, dequeue, isEmpty, size), implemente uma fila de contatos para call center. O menu deve oferecer:
# ●	Opção 1: Inserir Contato (solicitar nome e telefone)
# ●	Opção 2: Chamar próximo contato (dequeue e exibir dados)
# ●	Opção 3: Sair

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
Q = Queue()
status = False
while status == False:
    Option = input("Você quer inserir um contato? C - Contato, O - Obter, F - Fechar \n")
    match Option:
        case "C":
            Name = input("Qual nome do contato?\n")
            Phone = input("Qual telefone do contato?\n")
            Contact = (Name, Phone)
            Q.enqueue(Contact)
        case "O":
             print("Próximo contato: ", Q.dequeue())

        case "F":
            status = True
        case _:
            print("Entrada Inválida:", Option)