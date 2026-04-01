# Questão 9 
# Implemente em Python uma Lista Duplamente Encadeada (campos: dado, proximo, anterior). A classe deve conter:
# ●	Node com dado, proximo e anterior
# ●	Métodos: adicionar_fim(), adicionar_inicio(), remover_fim(), remover_inicio(), exibir_frente_para_tras(), exibir_tras_para_frente(), tamanho()
# Demonstre com uma agenda de contatos (nome, telefone, email) realizando todas as operações.

# Questão 9

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar_inicio(self, nome, telefone, email):
        dado = f"{nome} - {telefone} - {email}"
        novo = Node(dado)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def adicionar_fim(self, nome, telefone, email):
        dado = f"{nome} - {telefone} - {email}"
        novo = Node(dado)

        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo

    def remover_inicio(self):
        if self.inicio is None:
            return None

        removido = self.inicio.dado
        self.inicio = self.inicio.proximo

        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None

        return removido

    def remover_fim(self):
        if self.fim is None:
            return None

        removido = self.fim.dado
        self.fim = self.fim.anterior

        if self.fim:
            self.fim.proximo = None
        else:
            self.inicio = None

        return removido

    def exibir_frente_para_tras(self):
        atual = self.inicio
        while atual:
            print(atual.dado)
            atual = atual.proximo

    def exibir_tras_para_frente(self):
        atual = self.fim
        while atual:
            print(atual.dado)
            atual = atual.anterior

    def tamanho(self):
        contador = 0
        atual = self.inicio
        while atual:
            contador += 1
            atual = atual.proximo
        return contador


# Demonstração (agenda de contatos)

agenda = ListaDupla()

agenda.adicionar_inicio("Luiz", "94519-9921", "luiz@email.com")
agenda.adicionar_fim("Anthony", "85788-8118", "anthony@email.com")
agenda.adicionar_fim("Marcos", "72377-7234", "marcos@email.com")

print("Frente para trás:")
agenda.exibir_frente_para_tras()

print("\nTrás para frente:")
agenda.exibir_tras_para_frente()

print("\nRemovido do início:", agenda.remover_inicio())
print("Removido do fim:", agenda.remover_fim())

print("\nTamanho da lista:", agenda.tamanho())
