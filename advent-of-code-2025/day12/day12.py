import re


def parse(filepath):
    with open(filepath, "r") as f:
        chunks = f.read().strip().split("\n\n")

    shape_areas = []
    regions = []

    for chunk in chunks:
        if re.match(r"^\d+:", chunk):
            _, grid = chunk.split(":", 1)
            area = sum(1 for ch in grid if ch == "#")
            shape_areas.append(area)
        else:
            for line in chunk.splitlines():
                if not line.strip():
                    continue
                size_part, counts_part = line.split(":")
                w, h = map(int, size_part.split("x"))
                counts = list(map(int, counts_part.strip().split()))
                regions.append((w, h, counts))
    return shape_areas, regions


def main():
    filepath = "input.txt"
    shape_areas, regions = parse(filepath)

    result1 = 0
    for w, h, counts in regions:
        needed = sum(a * c for a, c in zip(shape_areas, counts))
        if needed <= w * h:
            result1 += 1
    print(f"Solution for Part 1: {result1}")


if __name__ == "__main__":
    main()
