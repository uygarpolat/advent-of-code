def get_galaxy_locations(grid):
    galaxy_locations = []
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '#':
                galaxy_locations.append((row, col))
    return galaxy_locations

def get_sum_of_distances(galaxy_locations, flag, empty_rows, empty_cols):
    from itertools import combinations

    pairs = list(combinations(galaxy_locations, 2))
    sum = 0
    for pair in pairs:
        row_multiplier = 0
        col_multiplier = 0
        for loc in range(len(empty_rows)):
            if pair[0][0] < empty_rows[loc] < pair[1][0] or pair[0][0] > empty_rows[loc] > pair[1][0]:
                row_multiplier += 1
        
        for loc1 in range(len(empty_cols)):
            if pair[0][1] < empty_cols[loc1] < pair[1][1] or pair[0][1] > empty_cols[loc1] > pair[1][1]:
                col_multiplier += 1

        row_dif = abs(pair[0][0] - pair[1][0])
        col_dif = abs(pair[0][1] - pair[1][1])
        sum += row_dif + col_dif + (col_multiplier * (flag - 1)) + (row_multiplier * (flag - 1))

    return sum

def get_empty_cols(grid):
    empty_cols = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(cols - 1, -1, -1):
        flag = 0
        for j in range(rows):
            if grid[j][i] == '#':
                break
            flag += 1
        if flag == rows:
            empty_cols.append(i)
    return empty_cols

def get_empty_rows(grid):
    empty_rows = []
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows - 1, -1, -1):
        if not '#' in grid[i]:
            empty_rows.append(i)
    return empty_rows

def main():
    import copy
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

        empty_rows = get_empty_rows(grid)
        empty_cols = get_empty_cols(grid)
        gal_loc = get_galaxy_locations(grid)

        sum_of_distances1 = get_sum_of_distances(gal_loc, 2, empty_rows, empty_cols)
        sum_of_distances2 = get_sum_of_distances(gal_loc, 1000000, empty_rows, empty_cols)

        print(f"Solution for Part 1: {sum_of_distances1}")
        print(f"Solution for Part 2: {sum_of_distances2}")

if __name__ == "__main__":
    main()