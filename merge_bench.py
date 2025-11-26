import os

CLASSIFIED_FILE = "bench-classified.txt"
COMPARE_DIR = "results/cpy_pypy"
MERGED_OUT_DIR = "results/cpy_pypy/merged_groups"


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


def read_compare_file(path):
    with open(path) as f:
        return f.read()


def save_merged_file(group, contents):
    os.makedirs(MERGED_OUT_DIR, exist_ok=True)
    out = os.path.join(MERGED_OUT_DIR, f"{group.replace('/', '_')}.txt")
    with open(out, "w") as f:
        f.write(contents)
    print("Merged:", out)


groups = load_groups(CLASSIFIED_FILE)

for group, benches in groups.items():
    merged = []

    for b in benches:
        path = os.path.join(COMPARE_DIR, f"compare_{b}.txt")
        if not os.path.exists(path):
            continue

        merged.append(f"========== {b} ==========\n")
        merged.append(read_compare_file(path))
        merged.append("\n")

    if merged:
        save_merged_file(group, "".join(merged))
