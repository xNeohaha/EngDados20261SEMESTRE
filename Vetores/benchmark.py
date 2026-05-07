import timeit, array, numpy as np
N = 1_000_000
setup_list = "v = list(range(N))"
setup_array = "import array; v = array.array('i', range(N))"
setup_numpy = "import numpy as np; v = np.arange(N, dtype=np.int32)"
# Teste: soma de todos os elementos
t_list = timeit.timeit("sum(v)", setup=setup_list, number=100, globals={'N':N})
t_array = timeit.timeit("sum(v)", setup=setup_array, number=100, globals={'N':N})
t_numpy = timeit.timeit("v.sum()", setup=setup_numpy, number=100, globals={'N':N})
print(f"list sum(): {t_list:.4f}s") # ~4.2s
print(f"array sum(): {t_array:.4f}s") # ~3.8s
print(f"numpy sum(): {t_numpy:.4f}s") # ~0.08s ← 50x mais rápido