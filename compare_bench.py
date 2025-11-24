import argparse
import subprocess
import pathlib

def compare_bench(bench_name):
    bench_name = bench_name.strip()
    if not bench_name:
        return

    cpy_bench = f"results/res_cpy/cpy_{bench_name}.json"
    pypy_bench = f"results/res_pypy/pypy_{bench_name}.json"

    out_dir = pathlib.Path("results/cpy_pypy")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / f"compare_{bench_name}.txt"

    cmd = ["pyperformance", "compare", cpy_bench, pypy_bench]

    try:
        result = subprocess.run(
            cmd, check=True, capture_output=True, text=True
        )

        lines = result.stdout.splitlines()
        start = next((i for i, l in enumerate(lines) if l.startswith("###")), len(lines))
        filtered = "\n".join(lines[start:])

        out_file.write_text(filtered)
    except subprocess.CalledProcessError:
        print(f"FAILED: {bench_name}")

p = argparse.ArgumentParser()
p.add_argument("--bench-file", default="bench.txt")
args = p.parse_args()

benches = [
    b.strip() for b in pathlib.Path(args.bench_file).read_text().splitlines() if b.strip()
]

for b in benches:
    compare_bench(b)
