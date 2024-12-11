def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            print(grid[row][col], end="")
        print("")
"""
def get_summary(grid):
    for row in range(len(grid)):
        if row < len(grid) - 1 and grid[row] == grid[row+1]:
            save1 = grid[:row + 1][::-1]
            save2 = grid[row + 1:]
            # print_grid(save1)
            # print("-------")
            # print_grid(save2)
            min_length = min(len(save1), len(save2))
            
            # for i in range(min_length):
            #     print(f"save1[{i}] = {save1[i]}")
            #     print(f"save2[{i}] = {save2[i]}")
            #     print("Equal?", save1[i] == save2[i])

            if all(save1[i] == save2[i] for i in range(min_length)):
                return row + 1
    return 0
"""

def get_summary(grid):
    for row in range(len(grid) -1 ):
        if grid[row] == grid[row+1]:
            save1 = grid[:row + 1][::-1]
            save2 = grid[row + 1:]
            # print_grid(save1)
            # print("-------")
            # print_grid(save2)
            min_length = min(len(save1), len(save2))
            
            # for i in range(min_length):
            #     print(f"save1[{i}] = {save1[i]}")
            #     print(f"save2[{i}] = {save2[i]}")
            #     print("Equal?", save1[i] == save2[i])

            if all(save1[i] == save2[i] for i in range(min_length)):
                return row + 1
    return 0

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        summaries = 0
        summary = 0
        content = file.read().strip()
        grids = [tuple(map(tuple, grid.splitlines())) for grid in content.split('\n\n')]
        for grid in grids:
            summary_row = get_summary(grid)
            grid2 = tuple(zip(*grid[::-1]))
            summary_col = get_summary(grid2)
            # print(summary_row)
            # print(summary_col)
            summaries += summary_row * 100 + summary_col
        print(summaries)


if __name__ == "__main__":
    main()