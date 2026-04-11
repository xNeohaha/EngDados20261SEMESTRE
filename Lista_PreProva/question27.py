from collections import deque

class FluxoDados:
    def __init__(self):
        # Inicializa a estrutura de fila
        self.registros = deque()

    def adicionar_registro(self, dado):
        """Insere o dado ao final da fila (Enqueue)."""
        self.registros.append(dado)

    def processar_registro(self):
        """Remove e retorna o dado mais antigo (Dequeue)."""
        if not self.vazia():
            return self.registros.popleft()
        return "Fila vazia"

    def vazia(self):
        return len(self.registros) == 0

# Teste da estrutura
processador = FluxoDados()
processador.adicionar_registro("Dados_Sensor_01")
processador.adicionar_registro("Dados_Sensor_02")
print(f"Processando agora: {processador.processar_registro()}")