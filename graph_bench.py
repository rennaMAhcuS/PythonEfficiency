import re
import os
import matplotlib.pyplot as plt
import numpy as np

CLASSIFIED_FILE = "bench-classified.txt"
COMPARE_DIR = "results/cpy_pypy"
OUT_DIR = "results/graphs"

HEADER_RE = re.compile(r"^###\s*(.+?)\s*###")
RATIO_RE  = re.compile(r":\s*([0-9.]+)x\s*(slower|faster)", re.I)


def load_groups(path):
    groups = {}
    current = None

    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if not line.startswith("-"):
                current = line
                groups[current] = []
            else:
                groups[current].append(line[1:].strip())

    return groups


def parse_compare_file(path, bench_name):
    text = open(path).read()
    lines = text.splitlines()

    results = {}
    current = None
    block = []

    def parse_ratio(block):
        m = RATIO_RE.search(block)
        if not m:
            return None
        v = float(m.group(1))
        return 1 / v if m.group(2).lower() == "slower" else v

    for line in lines:
        h = HEADER_RE.match(line)
        if h:
            if current and block:
                results[current] = parse_ratio("\n".join(block))
            current = bench_name + "_" + h.group(1).strip()
            block = []
        else:
            block.append(line)

    if current and block:
        results[current] = parse_ratio("\n".join(block))

    return results


def plot_group(name, data):
    os.makedirs(OUT_DIR, exist_ok=True)

    labels = list(data.keys())
    vals   = [data[k] for k in labels]

    # Apply log transform BEFORE plotting
    log_vals = np.log(vals)  # natural log; log(1)=0 baseline

    x = np.arange(len(log_vals))
    plt.figure(figsize=(14, 6), dpi=200)

    colors = plt.cm.tab20(np.linspace(0, 1, len(log_vals)))

    # Baseline at log(1)=0
    plt.axhline(0.0, color="black", linewidth=1)

    bars = plt.bar(
        x, log_vals,
        width=0.4,
        color=colors,
        edgecolor="black",
        linewidth=0.5
    )

    plt.xticks([])  # no bottom labels
    plt.ylabel("log(speedup)")
    plt.title(name)

    plt.legend(
        bars,
        labels,
        loc="upper left",
        bbox_to_anchor=(1.02, 1.0),
        borderaxespad=0,
        fontsize="small"
    )
    # plt.ylim(-8, 8)
    plt.tight_layout()

    out = os.path.join(OUT_DIR, f"{name.replace('/', '_')}.png")
    plt.savefig(out)
    plt.close()
    print("Generated:", out)


groups = load_groups(CLASSIFIED_FILE)

for group, benches in groups.items():
    collected = {}

    for b in benches:
        path = os.path.join(COMPARE_DIR, f"compare_{b}.txt")
        if not os.path.exists(path):
            continue
        collected.update(parse_compare_file(path, b))

    if collected:
        plot_group(group, collected)
