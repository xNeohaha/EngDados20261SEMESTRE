# Questão 3 
# Usando uma classe (com métodos push, pop, peek, isEmpty, size), implemente o um gerenciador de pilha de tarefas. As tarefas são strings. O menu deve oferecer:
# ●	Opção 1: Inserir tarefa na pilha
# ●	Opção 2: Obter a próxima tarefa da pilha
# ●	Opção 3: Sair

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
    


S = Stack()
status = False
while status == False: 
    Option = input("Você quer inserir uma tarefa? T - Tarefa, O - Obter, F - Fechar \n")
    match Option:
        case "T":
            Task = input("Qual tarefa?\n")
            S.push(Task)
        case "O":
             print("Última Tarefa adicionada: ", S.peek())
        case "F":
            status = True
        case _:
            print("Entrada Inválida:", Option)