from collections import deque

class GestorNuvem:
    def __init__(self):
        self.fila_requisicoes = deque()

    def nova_demanda(self, id_maquina):

        self.fila_requisicoes.append(id_maquina)

    def alocar_recurso(self):

        if not self.esta_vazia():
            return self.fila_requisicoes.popleft()
        return "Fila de alocação vazia."

    def esta_vazia(self):
        return len(self.fila_requisicoes) == 0

nuvem = GestorNuvem()
nuvem.nova_demanda("VM-PROD-01")
nuvem.nova_demanda("VM-DEV-02")
print(f"Processando: {nuvem.alocar_recurso()}")