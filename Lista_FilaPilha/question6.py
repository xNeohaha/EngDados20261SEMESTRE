# Questão 6 
# Implemente em Python uma classe ListaEncadeada. A implementação deve conter:
# ●	Classe Node com campos dado e proximo
# ●	Referências inicio_lista e fim_lista
# ●	Métodos: adicionar(dado), remover_inicio(), exibir(), esta_vazia()
# Demonstre com uma lista de contatos (nome, telefone): adicione 3 contatos, exiba, remova o primeiro e exiba novamente.



class Node:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio_lista = None
        self.fim_lista = None

    def esta_vazia(self):
        return self.inicio_lista is None

    def adicionar(self, nome, telefone):
        dadoContato = f"{nome} - {telefone}"
        novoNode = Node(dadoContato)
        
        if self.esta_vazia():
            self.inicio_lista = novoNode
            self.fim_lista = novoNode
        else:
            self.fim_lista.proximo = novoNode
            self.fim_lista = novoNode

    def exibir(self):
        atual = self.inicio_lista
        if self.esta_vazia():
            print("Lista está vazia!")
            return
        
        print("Lista de contatos:")
        while atual:
            print(f"- {atual.dado}")
            atual = atual.proximo

    def removerInicio(self):
        if self.esta_vazia():
            print("Lista está vazia! Nada para remover.")
            return None
        
        removed = self.inicio_lista.dado
        self.inicio_lista = self.inicio_lista.proximo
        
      
        if self.inicio_lista is None:
            self.fim_lista = None
            
        return removed


ListaContatos = ListaEncadeada()
ListaContatos.adicionar("Anthony", "312516-78")
ListaContatos.adicionar("João", "129723-41")
ListaContatos.adicionar("Alberto", "24487-94")

# EXTRA: Manipulação da lista de contatos
status = False
while status == False:
    print("\nEscolha uma opção:")
    print("SHOW  \t-\t Exibir lista atual")
    print("REMOVE\t-\t Remover primeiro contato")
    print("CHECK \t-\t Verificar se está vazia")
    print("INSERT\t-\t Adicionar novo contato")
    print("EXIT  \t-\t Sair")
    
    opcao = input("\nDigite SHOW, REMOVE, CHECK, INSERT ou EXIT: ")
   
    match opcao:
        case "SHOW":
            print("\n--- Exibindo lista ---")
            ListaContatos.exibir()
        case "REMOVE":
            removido = ListaContatos.removerInicio()
            if removido:
                print(f"\nContato removido: {removido}")
        case "CHECK":
            if ListaContatos.esta_vazia():
                print("\nA lista ESTÁ vazia.")
            else:
                print("\nA lista NÃO está vazia.")
        case "INSERT":
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            ListaContatos.adicionar(nome, telefone)
            print("Contato adicionado!")
        case "EXIT":
            print("\nSaindo...")
            status = True
        case _:
            print("Entrada inválida! Escolha SHOW, REMOVE, CHECK, INSERT ou EXIT.")
