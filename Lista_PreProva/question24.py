from collections import deque

class MonitorSeguranca:
    def __init__(self):
        self.fluxo_eventos = deque()

    def registrar_alerta(self, descricao):
        self.fluxo_eventos.append(descricao)

    def atender_alerta(self):
        if not self.esta_vazia():
            return self.fluxo_eventos.popleft()
        return "Sem alertas no momento."

    def esta_vazia(self):
        return len(self.fluxo_eventos) == 0

# Exemplo de uso:
rede = MonitorSeguranca()
rede.registrar_alerta("Tentativa de invasão - IP 192.168.1.1")
rede.registrar_alerta("Falha de autenticação - Usuário Admin")