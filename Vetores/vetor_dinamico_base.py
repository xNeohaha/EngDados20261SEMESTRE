import sys

lista = []
capacidade_anterior = sys.getsizeof(lista)

print(f"{'Elementos':>10} | {'Bytes':>8}")
print("-" * 22)
for i in range(17):
    lista.append(i)
    tamanho = sys.getsizeof(lista)
    if tamanho != capacidade_anterior:
        print(f"{i+1:>10} | {tamanho:>8}")
        capacidade_anterior = tamanho

