from itertools import permutations
def todas_permutacoes(lista):
    return list(permutations(lista))
# n=10 → 3.628.800 permutações
# n=15 → 1.307.674.368.000
def caixeiro_forca_bruta(cidades):
    melhor = float('inf')
    for rota in permutations(cidades):
        melhor = min(melhor, custo(rota))
    return melhor  # O(n!)