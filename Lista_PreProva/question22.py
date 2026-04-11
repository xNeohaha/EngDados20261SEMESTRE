class Stack:
    def __init__(self, capacidade=10):
        self.pilha = []
        self.capacidade = capacidade

    def adicionar(self, tentativa):
        self.pilha.append(tentativa)

        if len(self.pilha) > self.capacidade:
            self.pilha.pop(0) 

    def mais_recente(self):
        return self.pilha[-1] if self.pilha else None

    def listar(self):
        return self.pilha[::-1]

historico = Stack(capacidade=2)
historico.adicionar("Otavio@gmail.com - 23/05/1996 13:00")
historico.adicionar("Jubileu@gamil.com - 12/11/2002 15:05")
historico.adicionar("Vitor@email.com - 15/02/2001 23:00") # Vai remover o do Lucas

print("Tentativas (Mais recentes primeiro):", historico.listar())