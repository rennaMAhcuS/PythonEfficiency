import argparse
import subprocess
import pathlib

def run_bench(python_bin, prefix, bench_name):
    bench_name = bench_name.strip()
    if not bench_name:
        return

    out = f"results/{prefix}_{bench_name}.json"
    cmd = [
        "pyperformance", "run",
        "-p", python_bin,
        "--benchmark", bench_name,
        "-o", out
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print(f"FAILED: {bench_name}")

p = argparse.ArgumentParser()
p.add_argument("--python", required=True)
p.add_argument("--prefix", required=True)
p.add_argument("--bench-file", default="bench.txt")
args = p.parse_args()

benches = [b for b in pathlib.Path(args.bench_file).read_text().splitlines() if b.strip()]

for b in benches:
    run_bench(args.python, args.prefix, b)
