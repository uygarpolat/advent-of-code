from collections import deque


def get_neighbors(r, c, rows, cols):
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            nx, ny = r + x, c + y
            if 0 <= nx < rows and 0 <= ny < cols:
                yield (nx, ny)


def solve(grid_lines):

    rows = len(grid_lines)
    cols = len(grid_lines[0])

    paper_rolls = set()
    for r in range(rows):
        for c in range(cols):
            if grid_lines[r][c] == "@":
                paper_rolls.add((r, c))

    neighbors = {}
    queue = deque()
    discardable = set()

    for r, c in paper_rolls:
        count = 0
        for nr, nc in get_neighbors(r, c, rows, cols):
            if grid_lines[nr][nc] == "@":
                count += 1
        neighbors[(r, c)] = count

        if count < 4:
            queue.append((r, c))
            discardable.add((r, c))

    result1 = len(queue)
    result2 = 0

    while queue:
        r, c = queue.popleft()
        result2 += 1

        for nr, nc in get_neighbors(r, c, rows, cols):
            if (nr, nc) in paper_rolls and (nr, nc) not in discardable:
                neighbors[(nr, nc)] -= 1

                if neighbors[(nr, nc)] < 4:
                    queue.append((nr, nc))
                    discardable.add((nr, nc))

    return result1, result2


def main():
    filepath = "input.txt"
    with open(filepath, "r") as f:
        grid = [list(line.strip()) for line in f]

    result1, result2 = solve(grid)
    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {result2}")


if __name__ == "__main__":
    main()
