## Numba

```
python bench_numba.py 35
Warm up: 0.1485919952392578 seconds
Average over runs = 5: 0.036810 seconds

python bench_numba.py 36
Warm up: 0.16486001014709473 seconds
Average over runs = 5: 0.059331 seconds

python bench_numba.py 37
Warm up: 0.20724773406982422 seconds
Average over runs = 5: 0.096891 seconds

python bench_numba.py 38
Warm up: 0.259660005569458 seconds
Average over runs = 5: 0.157086 seconds

python bench_numba.py 39
Warm up: 0.3578341007232666 seconds
Average over runs = 5: 0.253975 seconds

python bench_numba.py 40
Warm up: 0.5798218250274658 seconds
Average over runs = 5: 0.410295 seconds
```

## PyPy

```
pypy bench_basic.py 35
Warm up: 0.0798797607421875 seconds
Average over runs = 5: 0.061621 seconds

pypy bench_basic.py 36
Warm up: 0.11710405349731445 seconds
Average over runs = 5: 0.100627 seconds

pypy bench_basic.py 37
Warm up: 0.2450408935546875 seconds
Average over runs = 5: 0.228489 seconds

pypy bench_basic.py 38
Warm up: 0.4486558437347412 seconds
Average over runs = 5: 0.433097 seconds

pypy bench_basic.py 39
Warm up: 0.7878379821777344 seconds
Average over runs = 5: 0.769435 seconds

pypy bench_basic.py 40
Warm up: 1.2624828815460205 seconds
Average over runs = 5: 1.242805 seconds
```
