import time, timeit
from sys import argv

from numba import jit

@jit(nopython=True)
def matmul(n: int):
    A = [[i + j for j in range(n)] for i in range(n)]
    B = [[i - j for j in range(n)] for i in range(n)]
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C[0][0]  # just return one element so work is not optimized away

n = int(argv[1])
runs = 5

start = time.time()
matmul(n)  # Warm up
# print(f"Warm up: {time.time() - start} seconds")
print(f"{(time.time() - start):.6f}")

t = timeit.timeit("matmul(n)", number=runs, globals=globals())
# print(f"Average over {runs = }: {(t / runs):.6f} seconds")
print(f"{(t / runs):.6f}")
