import time, timeit
from sys import argv

from numba import jit

@jit(nopython=True)
def sum_squares(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total

n = int(argv[1])
runs = 5

start = time.time()
sum_squares(n)  # Warm up
# print(f"Warm up: {time.time() - start} seconds")
print(f"{(time.time() - start):.6f}")

t = timeit.timeit("sum_squares(n)", number=runs, globals=globals())
# print(f"Average over {runs = }: {(t / runs):.6f} seconds")
print(f"{(t / runs):.6f}")
