from itertools import combinations

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def get_antenna_locations(grid):
    dict = {}
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col].isalnum():
                if grid[row][col] not in dict:
                    dict[grid[row][col]] = []
                dict[grid[row][col]].append((row,col))
    return(dict)

def precise_anti_node_loc(a, b, grid, flag):
    flag1 = 1
    flag2 = 1
    list_of_locs = []
    i = 1
    step_size_0 = a[0] - b[0]
    step_size_1 = a[1] - b[1]

    loc1 = (a[0] + i * step_size_0, a[1] + i * step_size_1)
    if is_in_grid(grid, loc1):
        list_of_locs.append(loc1)
    loc2 = (b[0] - i * step_size_0, b[1] - i * step_size_1)
    if is_in_grid(grid, loc2):
        list_of_locs.append(loc2)

    while(flag and (flag1 or flag2)):
        i += 1
        loc1 = (a[0] + i * step_size_0, a[1] + i * step_size_1)
        if is_in_grid(grid, loc1):
            list_of_locs.append(loc1)
        else:
            flag1 = 0
        loc2 = (b[0] - i * step_size_0, b[1] - i * step_size_1)
        if is_in_grid(grid, loc2):
            list_of_locs.append(loc2)
        else:
            flag2 = 0
    return list_of_locs

def get_anti_nodes(value, grid, anti_nodes_general, flag):
    anti_nodes_local = []
    if flag:
        elements_to_add = set(value) - set(anti_nodes_general)
        anti_nodes_general.extend(elements_to_add)
    for a, b in combinations(value, 2):
        locs = precise_anti_node_loc(a, b, grid, flag)
        elements_to_add = set(locs) - (set(anti_nodes_local) | set(anti_nodes_general))
        anti_nodes_local.extend(elements_to_add)
    return anti_nodes_local

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
        locs = get_antenna_locations(grid)
        for i in range(2):
            anti_nodes_local = []
            anti_nodes_general = []
            for key in locs:
                anti_nodes_local = get_anti_nodes(locs[key], grid, anti_nodes_general, i)
                anti_nodes_general.extend(anti_nodes_local)
            print (f"Answer for part {i+1}: {len(anti_nodes_general)}")

if __name__ == "__main__":
    main()