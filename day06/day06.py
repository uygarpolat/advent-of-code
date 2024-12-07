import copy
from multiprocessing import Pool, Manager

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

def square_inside_grid(grid, loc):
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

def traverse(grid, start_loc, flag=False, dir=(-1,0)):
    count = 1
    # dir = (-1, 0)
    temp = {}
    hits = [start_loc]
    traversing = True
    while(traversing):
        if not flag:
            grid[start_loc[0]][start_loc[1]] = 'x'
            hits.append(start_loc)

        next_loc = tuple(a + b for a, b in zip(start_loc, dir))

        # if flag:
        if next_loc in temp:
            if dir in temp[next_loc]:
                if flag:
                    return -1, None, temp
            else:
                temp[next_loc].append(dir)
        else:
            temp[next_loc] = [dir]

        if square_inside_grid(grid, next_loc):
            if grid[next_loc[0]][next_loc[1]] == '#':
                dir = change_dir(dir)
            else:
                if grid[next_loc[0]][next_loc[1]] != 'x':
                    count += 1
                start_loc = next_loc
        else:
            break
    return count, hits, temp

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end ="")
        print("")

# def process_cell(tasks):
#     i, j, grid_perm, start_loc, hits = tasks
#     if grid_perm[i][j] == '^' or not (i, j) in hits:
#         return 0
        
#     temp = grid_perm[i][j]
#     grid_perm[i][j] = '#'
#     if traverse(grid_perm, start_loc, True) == -1:
#         grid_perm[i][j] = temp
#         return 1
#     grid_perm[i][j] = temp
#     return 0

def process_cell(tasks):
    i, j, grid_perm, start_loc, hits ,temp = tasks
    if grid_perm[i][j] == '^' or not (i, j) in hits:
        return 0
    
    what = tuple(a * b for a, b in zip((-1,-1), temp[(i,j)][0]))
    start_loc_new = tuple(a + b for a, b in zip((i,j), what))
    if start_loc_new in temp:
        new_dir = temp[start_loc_new][0]
    else:
        start_loc_new = start_loc
        new_dir = (-1,0)

    temp2 = grid_perm[i][j]
    grid_perm[i][j] = '#'
    flag, _, _ = traverse(grid_perm, start_loc_new, True, new_dir)
    grid_perm[i][j] = temp2
    if flag == -1:
        return 1
    return 0

def main():
    import copy
    with open("input.txt", 'r') as file:
        grid = [list(line.strip()) for line in file]
        grid_perm = copy.deepcopy(grid)
        start_loc = get_start_loc(grid)
        unique_locs, hits, temp = traverse(grid, start_loc)
        
        tasks = []
        for i in range(len(grid_perm)):
            for j in range(len(grid_perm[i])):
                tasks.append((i, j, grid_perm, start_loc, hits, temp))
        
        with Pool() as pool:
            results = pool.map(process_cell, tasks)
        obstacles = sum(results)
        
        print(f"Part 1 solution: {unique_locs}")
        print(f"Part 2 solution: {obstacles}")

if __name__ == "__main__":
    main()