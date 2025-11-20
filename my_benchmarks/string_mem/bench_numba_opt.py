import time, timeit
from sys import argv

from numba import jit, types
from numba.typed import Dict

@jit(nopython=True)
def word_count(text: str):
    counts = Dict.empty(key_type=types.unicode_type, value_type=types.int64)
    for word in text.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


n = int(argv[1])
runs = 5

text = ("lorem ipsum " * 10) * (n // 10)  # simulate a large text

start = time.time()
word_count(text)  # Warm up
# print(f"Warm up: {time.time() - start} seconds")
print(f"{(time.time() - start):.6f}")

t = timeit.timeit("word_count(text)", number=runs, globals=globals())
# print(f"Average over {runs = }: {(t / runs):.6f} seconds")
print(f"{(t / runs):.6f}")
