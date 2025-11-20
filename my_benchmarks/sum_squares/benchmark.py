import subprocess
import matplotlib.pyplot as plt
from joblib import Parallel, delayed

from sys import argv

proj_dir = argv[1]

pyvenv = ".venv/bin/python"
pypyvenv = ".pypyvenv/bin/pypy"

# Compile the C++ sum of squares program
subprocess.run(["clang++", "bench_c++.cpp", "-o", "sq_sum_cpp.out"], check=True)

scripts = {
    "CPython": [pyvenv, "bench_basic.py"],
    "Numba": [pyvenv, "bench_numba.py"],
    "Cython": [pyvenv, "bench_cython.py"],
    "PyPy": [pypyvenv, "bench_basic.py"],
    "C++": ["./sq_sum_cpp.out"]
}

ns = [10**4, 10**5, 10**6, 2*10**6, 5*10**6, 10**7, 2*10**7, 5*10**7]

def run_benchmark(name, script, n):
    if name == "C++":
        output = subprocess.run(
            [script[0], str(n)],
            capture_output=True,
            text=True
        ).stdout.strip().splitlines()
    else:
        output = subprocess.run(
            [f"{proj_dir}/{script[0]}", script[1], str(n)],
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

plt.title("Sum of Squares Execution Time")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.savefig("sq_sum_benchmark.png", dpi=300)
plt.clf()

# Plotting initial execution times
for name, times in results_ini.items():
    plt.plot(ns, times, marker='o', label=name)

plt.title("Sum of Squares Initial Execution Time")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.savefig("sq_sum_benchmark_init.png", dpi=300)
