import time, timeit
from sys import argv

def word_count(text: str):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
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
