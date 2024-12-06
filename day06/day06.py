def get_start_loc(grid):
    marked_location = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                marked_location = (i, j)
                break
        if marked_location:
            break
    return marked_location

def next_square_within(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def change_dir(dir):
    row = dir[0]
    col = dir[1]
    if (col == 0):
        return (-col, -row)
    else:
        return (col, row)

def traverse(grid):
    start_loc = get_start_loc(grid)
    count = 1
    dir = (-1, 0)
    traversing = True
    while(traversing):
        grid[start_loc[0]][start_loc[1]] = 'x'
        next_loc = tuple(a + b for a, b in zip(start_loc, dir))
        if next_square_within(grid, next_loc):
            if grid[next_loc[0]][next_loc[1]] == '#':
                dir = change_dir(dir)
            else:
                if grid[next_loc[0]][next_loc[1]] != 'x':
                    count += 1
                grid[next_loc[0]][next_loc[1]] = 'x'
                start_loc = next_loc
        else:
            break
    return count

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end ="")
        print("")

def main():
    with open("input.txt", 'r') as file:
        grid = [list(line.strip()) for line in file]
    unique_locs = traverse(grid)
    # print_grid(grid)
    print(unique_locs)

if __name__ == "__main__":
    main()