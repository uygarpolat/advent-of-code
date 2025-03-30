def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def print_grid(grid, loc_robot):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if row == loc_robot[0] and col == loc_robot[1]:
                print("@", end="")
            else:
                print(grid[row][col], end="")
        print("")

def parse_file(file_path):
    dirs_num = [(1,0),(0,1),(-1,0),(0,-1)]
    dirs_alp = ['v', '>', '^', '<']

    direction_map = dict(zip(dirs_alp, dirs_num))
    grid = []
    moves = []
    second_part = False

    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            if not second_part:
                if line == "\n":
                    second_part = True
                    continue
                if set(line.strip()) == {"#"}:
                    continue
                modified_line = list(line.strip())[1:-1]
                if '@' in modified_line:
                    index = modified_line.index('@')
                    loc_robot = (i - 1, index)
                    modified_line[index] = '.'
                grid.append(modified_line)
            else:
                moves.extend(direction_map[c] for c in line.strip() if c in direction_map)
    return grid, moves, loc_robot

def calculate_sum(grid):
    total_score = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '[':
                total_score += (row + 1) * 100 + (col + 2)

    return total_score

def widefy_grid(grid):
    grid_wider = []
    for row in grid:
        widened_row = [
            item if item != 'O' else char 
            for item in row 
            for char in ([item, item] if item != 'O' else ['[', ']'])
        ]
        grid_wider.append(widened_row)
    return grid_wider

def main():
    file_path = "input.txt"
    grid, moves, loc_robot = parse_file(file_path)
    
    grid = widefy_grid(grid)
    loc_robot = (loc_robot[0],loc_robot[1] * 2)

    for dir in moves:
        if is_move_possible(grid, loc_robot, dir):
            loc_robot = make_the_move(grid, loc_robot, dir)
    print(f"Solution for Part 2: {calculate_sum(grid)}")

def make_the_move(grid, old_loc, dir):
    new_loc = tuple(map(sum, zip(old_loc, dir)))

    value_new_loc = grid[new_loc[0]][new_loc[1]]
    
    if value_new_loc == '.':
        grid[old_loc[0]][old_loc[1]], grid[new_loc[0]][new_loc[1]] = grid[new_loc[0]][new_loc[1]], grid[old_loc[0]][old_loc[1]]
        return new_loc
    if dir == (0,1) or dir == (0,-1):
        make_the_move(grid, new_loc, dir)
    elif value_new_loc == '[':
        make_the_move(grid, new_loc, dir)
        make_the_move(grid, (new_loc[0], new_loc[1] + 1), dir)
    elif value_new_loc == ']':
        make_the_move(grid, new_loc, dir)
        make_the_move(grid, (new_loc[0], new_loc[1] - 1), dir)
    grid[old_loc[0]][old_loc[1]], grid[new_loc[0]][new_loc[1]] = grid[new_loc[0]][new_loc[1]], grid[old_loc[0]][old_loc[1]]
    return new_loc

def is_move_possible(grid, old_loc, dir):
    new_loc = tuple(map(sum, zip(old_loc, dir)))

    if not is_in_grid(grid, new_loc):
        return False
    
    value_new_loc = grid[new_loc[0]][new_loc[1]]

    if value_new_loc == '#':
        return False
    elif value_new_loc == '.':
        return True
    elif dir == (0,1) or dir == (0,-1):
        res = is_move_possible(grid, new_loc, dir)
        return res
    elif value_new_loc == '[':
        res1 = is_move_possible(grid, new_loc, dir)
        res2 = is_move_possible(grid, (new_loc[0], new_loc[1] + 1), dir)
        return res1 and res2
    elif value_new_loc == ']':
        res1 = is_move_possible(grid, new_loc, dir)
        res2 = is_move_possible(grid, (new_loc[0], new_loc[1] - 1), dir)
        return res1 and res2

if __name__ == "__main__":
    main()