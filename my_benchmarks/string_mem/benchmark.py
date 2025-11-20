import subprocess
import matplotlib.pyplot as plt
from joblib import Parallel, delayed

from sys import argv

proj_dir = argv[1]

pyvenv = ".venv/bin/python"
pypyvenv = ".pypyvenv/bin/pypy"

# Compile the String Memory benchmark program
subprocess.run(["clang++", "bench_c++.cpp", "-o", "string_mem_cpp.out"], check=True)

scripts = {
    "CPython": [pyvenv, "bench_basic.py"],
    "Numba": [pyvenv, "bench_numba.py"],
    "NumbaOpt": [pyvenv, "bench_numba_opt.py"],
    "Cython": [pyvenv, "bench_cython.py"],
    "PyPy": [pypyvenv, "bench_basic.py"],
    "C++": ["./string_mem_cpp.out"]
}

ns = [1e5, 2e5, 5e5, 1e6, 2e6, 5e6, 1e7]

def run_benchmark(name, script, n):
    n_int = int(n)
    if name == "C++":
        output = subprocess.run(
            [script[0], str(n_int)],
            capture_output=True,
            text=True
        ).stdout.strip().splitlines()
    else:
        output = subprocess.run(
            [f"{proj_dir}/{script[0]}", script[1], str(n_int)],
            capture_output=True,
            text=True
        ).stdout.strip().splitlines()
    return name, float(output[0]), float(output[1])

results_ini = {name: [] for name in scripts}
results = {name: [] for name in scripts}

all_tasks = [(name, script, n) for n in ns for name, script in scripts.items()]
all_results = Parallel(n_jobs=-1)(delayed(run_benchmark)(name, script, n) for (name, script, n) in all_tasks)

for n in ns:
    for name in scripts:
        for res in all_results:
            if res[0] == name and all_tasks[all_results.index(res)][2] == n:
                results_ini[name].append(res[1])
                results[name].append(res[2])
                break

# Plotting
for name, times in results.items():
    plt.plot(ns, times, marker='o', label=name)

plt.title("String Memory Benchmark Execution Time")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.savefig("string_mem_benchmark.png", dpi=300)
plt.clf()

# Plotting initial execution times
for name, times in results_ini.items():
    plt.plot(ns, times, marker='o', label=name)

plt.title("String Memory Benchmark Initial Execution Time")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.savefig("string_mem_benchmark_init.png", dpi=300)
