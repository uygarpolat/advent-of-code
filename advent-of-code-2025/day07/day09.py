from collections import defaultdict


def main():

    filepath = "input.txt"
    with open(filepath, "r") as f:
        grid = [list(line.strip()) for line in f]

    rows = len(grid)
    cols = len(grid[0])
    start = (0, grid[0].index("S"))
    locs = set([start[1]])
    tally = defaultdict(int, {start[1]: 1})
    result1 = 0

    for i in range(start[0] + 1, rows):
        for j in range(cols):
            if grid[i][j] == "^" and j in locs:

                if j - 1 >= 0:
                    locs.add(j - 1)
                    tally[j - 1] += tally[j]

                if j + 1 <= cols - 1:
                    locs.add(j + 1)
                    tally[j + 1] += tally[j]

                locs.remove(j)
                tally[j] = 0
                result1 += 1

    result2 = sum(tally.values())

    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {result2}")


if __name__ == "__main__":
    main()
