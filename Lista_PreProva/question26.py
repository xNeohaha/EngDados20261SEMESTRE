from collections import deque

class GestorProcessos:
    def __init__(self):
        self.tarefas_pendentes = deque()

    def adicionar_tarefa(self, identificador):
        self.tarefas_pendentes.append(identificador)

    def executar_proxima(self):
        if not self.esta_vazia():
            return self.tarefas_pendentes.popleft()
        return "Nenhuma tarefa na fila."

    def esta_vazia(self):
        return len(self.tarefas_pendentes) == 0

# Exemplo de uso operacional
so = GestorProcessos()
so.adicionar_tarefa("Processo_PID_104")
so.adicionar_tarefa("Processo_PID_205")
print(f"Executando agora: {so.executar_proxima()}")