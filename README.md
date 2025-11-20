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

Get info on Startup / short-lived scripts - measures interpreter startup and import overhead.

## To Do

- Interpreter overhead
- Syscalls - FileIO and stuff
- GPU
- Benchmark more numpy and numba
