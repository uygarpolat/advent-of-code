def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            print(grid[row][col], end="")
        print("")

def get_summary1(grid):
    for row in range(len(grid)):
        if row < len(grid) - 1 and grid[row] == grid[row+1]:
            save1 = grid[:row + 1][::-1]
            save2 = grid[row + 1:]

            min_length = min(len(save1), len(save2))

            if all(save1[i] == save2[i] for i in range(min_length)):
                return row + 1
    return 0

def get_summary2(grid):
    for row in range(len(grid) - 1):
        difference = sum(a != b for a, b in zip(grid[row], grid[row+1]))
        if difference < 2:

            save1 = grid[:row + 1][::-1]
            save2 = grid[row + 1:]
            min_length = min(len(save1), len(save2))
            save1 = save1[:min_length]
            save2 = save2[:min_length]

            if difference == 1:
                if all(save1[i] == save2[i] for i in range(1, min_length)):
                    return row + 1
            else:
                difference2 = 0
                for rw in range(len(save1)):
                    difference2 += sum(a != b for a, b in zip(save1[rw], save2[rw]))
                if difference2 == 1:
                    return row + 1
    return 0

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        summaries = 0
        content = file.read().strip()
        grids = [tuple(map(tuple, grid.splitlines())) for grid in content.split('\n\n')]
        func = [get_summary1, get_summary2]
        for i in range(2):
            summaries = 0
            for grid in grids:
                summary_row = func[i](grid)
                grid_rotated_90_degree_clockwise = tuple(zip(*grid[::-1]))
                summary_col = func[i](grid_rotated_90_degree_clockwise)
                summaries += summary_row * 100 + summary_col
            print(f"Solution for Part {i+1}: {summaries}")

if __name__ == "__main__":
    main()