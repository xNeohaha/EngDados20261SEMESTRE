def multiplica_matrizes(A, B, n):
    C = [[0]*n for _ in range(n)]
    for i in range(n):       # O(n)
        for j in range(n):   # O(n)
            for k in range(n): # O(n)
                C[i][j] += A[i][k] * B[k][j]
    return C
# Complexidade total: O(n³)