from collections import defaultdict


def main():

    filepath = "input.txt"
    with open(filepath, "r") as f:
        grid = [list(line.strip()) for line in f]

    rows, cols, result1 = len(grid), len(grid[0]), 0
    start = (0, grid[0].index("S"))
    tally = defaultdict(int, {start[1]: 1})

    for i in range(start[0] + 1, rows):
        for j in range(cols):
            if grid[i][j] == "^" and j in tally:
                result1 += 1
                tally[j - 1] += tally[j]
                tally[j + 1] += tally[j]
                del tally[j]

    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {sum(tally.values())}")


if __name__ == "__main__":
    main()
