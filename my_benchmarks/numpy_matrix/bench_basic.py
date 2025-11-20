import time, timeit
import numpy as np
from sys import argv

def matmul(n: int):
    A = np.fromfunction(lambda i, j: i + j, (n, n), dtype=int)
    B = np.fromfunction(lambda i, j: i - j, (n, n), dtype=int)
    C = np.dot(A, B)
    return C[0, 0]  # avoid optimization

n = int(argv[1])
runs = 5

start = time.time()
matmul(n)  # Warm up
print(f"{(time.time() - start):.6f}")

t = timeit.timeit("matmul(n)", number=runs, globals=globals())
print(f"{(t / runs):.6f}")
