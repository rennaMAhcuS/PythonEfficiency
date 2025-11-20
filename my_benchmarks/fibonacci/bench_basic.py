import time, timeit
from sys import argv

def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(argv[1])
runs = 5

start = time.time()
fib(n)  # Warm up
# print(f"Warm up: {time.time() - start} seconds")
print(f"{(time.time() - start):.6f}")

t = timeit.timeit("fib(n)", number=runs, globals=globals())
# print(f"Average over {runs = }: {(t / runs):.6f} seconds")
print(f"{(t / runs):.6f}")
