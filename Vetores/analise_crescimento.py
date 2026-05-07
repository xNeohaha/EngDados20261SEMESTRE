import math

def contar_realocacoes(n: int, capacidade_inicial: int = 1) -> dict:
    capacidade = capacidade_inicial
    realocacoes = 0
    total_copias = 0
    historico = []
    while capacidade < n:
        total_copias += capacidade # copia todos os elementos atuais
        capacidade *= 2 # dobra a capacidade
        realocacoes += 1
        historico.append(capacidade)
    return {
        "realocacoes": realocacoes,
        "total_copias": total_copias,
        "capacidade_final": capacidade,
        "historico": historico
}

# Testando para n = 100 elementos
resultado = contar_realocacoes(100)
print(f"Realocações: {resultado['realocacoes']}") # 7
print(f"Total cópias: {resultado['total_copias']}") # 127
print(f"Capacidade final: {resultado['capacidade_final']}") # 128
print(f"Histórico: {resultado['historico']}")
# Prova matemática: total cópias = 2^k - 1 ≈ n → O(n) amortizado