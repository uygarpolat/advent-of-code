def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            print(grid[row][col], end="")
        print("")

def sort_row(row):
    sorted_list = sorted(row, key=lambda x: x != 'O')
    return(sorted_list)

def modify_row(row):

    replacement_row = []

    while(row):
        if '#' in row:
            index = row.index('#')
            first_part = row[:index]
            replacement_row.extend(sort_row(first_part))
            replacement_row.append('#')
            row = row[index+1:]
        else:
            replacement_row.extend(sort_row(row))
            row = []

    return replacement_row

def rot_90_c_clock(grid):
    return list(zip(*grid))[::-1]

def rot_90_clock(grid):
    return list(zip(*grid[::-1]))

def rot_180(grid):
    grid = rot_90_c_clock(grid)
    return rot_90_c_clock(grid)

def push_o_to_left(grid):
    for i in range(len(grid)):
        grid[i] = modify_row(grid[i])
    return grid

def calculate_load(grid):
    count = 0
    for i, row in enumerate(grid):
        count += row.count('O') * (len(grid) - i)
    return count

def tilt_north(grid):
    grid = rot_90_c_clock(grid)
    grid = push_o_to_left(grid)
    grid = rot_90_clock(grid)
    return grid

def tilt_west(grid):
    grid = push_o_to_left(grid)
    return grid

def tilt_east(grid):
    grid = rot_180(grid)
    grid = push_o_to_left(grid)
    grid = rot_180(grid)
    return grid

def tilt_south(grid):
    grid = rot_90_clock(grid)
    grid = push_o_to_left(grid)
    grid = rot_90_c_clock(grid)
    return grid

def do_cycle(grid):
    grid = tilt_north(grid)
    grid = tilt_west(grid)
    grid = tilt_south(grid)
    grid = tilt_east(grid)
    return grid

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    grid2 = grid
    grid2 = tilt_north(grid2)
    print(f"Solution for Part 1: {calculate_load(grid2)}")

    cycle_results = []
    iterations = 1000000000
    for i in range(iterations):
        grid = do_cycle(grid)
        if grid in cycle_results:
            index = cycle_results.index(grid)
            revert = (((iterations) - index - 1) % (i - index)) + index + 1 - 1
            grid = cycle_results[revert]
            break
        cycle_results.append(grid)
    print(f"Solution for Part 2: {calculate_load(grid)}")

if __name__ == "__main__":
    main()