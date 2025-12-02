# Benchmarking - Notes

- CPython - The default python interpreter which you see everywhere.
- Cython - The compiler.
- Numba - Custom JIT.
- PyPy - Detects usecases and uses JIT wherever possible.

## First Test - Fibonacci

### Numba

The first run of numba took a lot of time, but the time shown by the "Time" module is less. - Why?

Also, about the function calls - compiles the first time (when running), and runs the compiled version, to run at near C speed.

`@jit(nopython=True)` disables Python object overhead.

For `fib(40)` - the normal one took ~13 sec, the numba JIT one took around 0.5 sec.

### Cython

Surprisingly, the Cython one, which I thought would be the fastes, wasn't. It tooke ~5.1 sec for the same `fib(40)`.

**Cython's Claim** - Works well for numeric-heavy, recursive, or loop-heavy code.

### PyPy

Finally, PyPy - the one which "automatically" JIT-compiles "hot" loops and recursive calls, does `fib(40)` (with the basic `fib.py`) in ~1.2 sec.

Well, that was just the first test, maybe too soon for calling in a judgement.

## Tests

- Pure recursion - call-heavy, compute-bound: Fibonacci.
- Tight numeric loops - arithmetic-heavy single loops: sum of squares.
- Nested loops / matrix ops - cache- and memory-sensitive: manual matrix multiply.

- String & I/O processing - text parsing, file I/O (I/O-bound).
- NumPy / vectorized - library-bound, C-backed array ops.

### Info

- Get info on Startup / short-lived scripts - measures interpreter startup and import overhead.

- Versions of the tools used in `my_benchmarks`:

```
python==3.13
pypy==3.11
Cython==3.1.4
numba==0.62.0
numpy==2.3.3
```

## To Do

- Learn more on Numba JIT.
- Run some actual benchmarks.

## Benchmarking with standard benchmarking tests

### Some notes

- Pyperf / Pyperformance
- airspeed velocity - benchmarking Python PyPI packages
- numba, cython can't be directly compared with cpython
- cpython and pypy can be compared, as the benchmark suite is the same. (No code modification required.)
- Couldn't find any standard benchmark suite for cython to work on, directly.
- The computed benchmarking for numba was done with python 3.6 - Results in the numba benchmark results link.

### References

- [Pyperformance](https://pyperformance.readthedocs.io): pyperf - engine, pyperformance - full suite
- [Numba benchmark suite](https://github.com/numba/numba-benchmark)
- [Numba bechmark results](https://numba.pydata.org/numba-benchmark): unable to run on my system / a GPU server - Some version incompatibility issues.
- [ASV](https://github.com/airspeed-velocity/asv) 
- [Pybenchmarks](https://pybenchmarks.org): this one has a lot of data benchmark tests, espically for basic programs. - Don't know about the realibility.
