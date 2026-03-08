# Questão 10 
# Implemente em Python um sistema integrado que combine as três estruturas do documento para simular um gerenciamento de pedidos de restaurante:
# ●	FILA → pedidos chegam em ordem de chegada (FIFO)
# ●	PILHA → pedidos prontos aguardam entrega (LIFO)
# ●	LISTA Python → histórico completo com timestamp
# Menu: 1) Novo pedido | 2) Cozinhar próximo | 3) Entregar pedido pronto | 4) Ver histórico | 5) Ver status atual | 6) Sair

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def exibir(self):
        return self.items.copy()


fila_pedidos = Queue()


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
    
    def exibir(self):
        return self.items.copy()


pilha_prontos = Stack()
historico_entregas = []  # guarda pedidos entregues


while True:
   
    opcao_menu = int(input(
        "Menu: 1 - Novo Pedido, 2 - Cozinhar Próximo 3 - Entregar pedido pronto "
        "4 - Ver Histórico 5 - Ver Status Atual 6 - Sair\n"))

    match opcao_menu:

        case 1:
            novo_pedido = input("Qual é o pedido?\n")
            fila_pedidos.enqueue(novo_pedido)  # adiciona pedido à fila

        case 2:
            if not fila_pedidos.isEmpty():
                pedido_cozinhado = fila_pedidos.dequeue()  # tira da fila
                pilha_prontos.push(pedido_cozinhado)  # vai para pilha de prontos
                print(f"Cozinhando... {pedido_cozinhado}")
            else:
                print("Fila de pedidos vazia...")

        case 3:
            if not pilha_prontos.isEmpty():
                pedido_entregue = pilha_prontos.pop()
                historico_entregas.append(pedido_entregue)
                print(f"Entregue: {pedido_entregue}")
            else:
                print("Nenhum pedido pronto para entrega.")

        case 4:
            print("Histórico de entregas:")
            print(historico_entregas)

        case 5:
            print("Status atual\n")

            if fila_pedidos.size() > 0:
                print(f"Pedidos na fila: {fila_pedidos.exibir()}")

            if pilha_prontos.size() > 0:
                print(f"Pedidos prontos: {pilha_prontos.exibir()}")

            if len(historico_entregas) > 0:
                print(f"Total entregues: {len(historico_entregas)}\n")

        case 6:
            print("Saindo...")
            break
