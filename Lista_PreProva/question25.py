from collections import deque

class SistemaPedidos:
    def __init__(self):
        # Fila de pedidos (FIFO)
        self.fila = deque()

    def registrar_entrada(self, item):
        """Adiciona um novo pedido ao fim da fila."""
        self.fila.append(item)

    def atender_pedido(self):
        """Remove o pedido mais antigo para processamento."""
        if not self.esta_vazia():
            return self.fila.popleft()
        return "Nenhum pedido pendente."

    def esta_vazia(self):
        return len(self.fila) == 0

# Exemplo operacional
ecommerce = SistemaPedidos()
ecommerce.registrar_entrada("Pedido #101 - Smartphone")
ecommerce.registrar_entrada("Pedido #102 - Fone Bluetooth")
print(f"Processando: {ecommerce.atender_pedido()}")