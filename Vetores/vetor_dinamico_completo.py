import sys
# Inicialização — vetor dinâmico vazio
vetor_din = []
# --- INSERÇÃO ---
# append(): inserção ao final — O(1) amortizado
vetor_din.append(10)
vetor_din.append(20)
vetor_din.append(30)
print(f"Após append: {vetor_din}") # [10, 20, 30]
# insert(): inserção em posição arbitrária — O(n)
vetor_din.insert(1, 15) # insere 15 na posição 1
print(f"Após insert: {vetor_din}") # [10, 15, 20, 30]
# --- REMOÇÃO ---
# pop(): remove o último elemento — O(1)
ultimo = vetor_din.pop()
print(f"Removido: {ultimo}, Lista: {vetor_din}") # 30, [10, 15, 20]
# remove(): remove por valor — O(n)
vetor_din.remove(15)
print(f"Após remove(15): {vetor_din}") # [10, 20]
# --- ACESSO E BUSCA ---
print(f"Índice 0: {vetor_din[0]}") # O(1)
print(f"Índice de 20: {vetor_din.index(20)}") # O(n)
# --- CAPACIDADE INTERNA ---
vetor_grande = list(range(100))
print(f"Tamanho lógico: {len(vetor_grande)}")
print(f"Bytes alocados: {sys.getsizeof(vetor_grande)}")