# Enunciado: Implemente o método find() na classe DynamicArray 
# que retorna o índice da primeira ocorrência de um objeto usando igualdade (==).
# Analise a complexidade e teste com uma lista de objetos Aluno.

import ctypes

class DynamicArray:
    """Vetor dinâmico similar à list do Python."""

    def __init__(self):
        self._n = 0           # Número de elementos reais
        self._capacity = 1    # Capacidade total do array
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('Índice inválido')
        return self._A[k]

    @property
    def capacity(self):
        return self._capacity

    def _make_array(self, c):
        """Aloca array de capacidade c usando ctypes."""
        return (c * ctypes.py_object)()

    def _resize(self, c):
        """
        Realoca o array interno para nova capacidade c.
        Complexidade: O(n) — copia todos os elementos.
        """
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def append(self, obj):
        """Adiciona um elemento ao final do vetor."""
        if self._n == self._capacity:
            # Dobra a capacidade se estiver cheio
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def remove(self, value):
        """
        Remove a primeira ocorrência de value.
        Complexidade: O(n) — busca + deslocamento.
        """
        for k in range(self._n):
            if self._A[k] == value:
                # Desloca os elementos para a esquerda
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                
                self._A[self._n - 1] = None  # Ajuda o Garbage Collector
                self._n -= 1

                # Encolher o array se o uso for inferior a 25%
                if 0 < self._n < self._capacity // 4:
                    self._resize(self._capacity // 2)
                return
        
        raise ValueError(f'Valor {value} não encontrado')
    
    def find(self, value):
        for i in range(self._n):
            # O enunciado pede igualdade (==). 
            # Como você implementou __eq__ na classe Aluno, 
            # self._A[i] == value funcionará comparando com o nome.
            if self._A[i] == value:
                return i
        return -1  # Retorna -1 caso não encontre nada
# --- Classes de Suporte e Exemplo de Uso ---

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __repr__(self):
        return f'Aluno(Nome: {self.nome}, Matrícula: {self.matricula})'

    def __eq__(self, value):
        """Necessário para que o método remove() encontre o objeto por valor."""
        return self.nome == value


# Criando a turma
turma = DynamicArray()

# Adicionando alunos
turma.append(Aluno('Ana', '2024001'))
turma.append(Aluno('Bruno', '2024002'))
turma.append(Aluno('Carla', '2024003'))

print(f"Tamanho da turma: {len(turma)}")
print(f"Capacidade atual: {turma.capacity}")

indice = turma.find("Ana")
print(f"Índice da Ana: {indice}") 

indice = turma.find("Bruno")
print(f"Índice do Bruno: {indice}") 

indice = turma.find("Carla")
print(f"Índice da Carla: {indice}") 
