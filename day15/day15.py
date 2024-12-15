def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
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
            if grid[row][col] == 'O':
                total_score += (row + 1) * 100 + (col + 1)
    return total_score


def main():
    file_path = "input.txt"
    grid, moves, loc_robot = parse_file(file_path)
    # print(moves)
    # print(loc_robot)
    # print_grid(grid)

    for dir in moves:
        # print("---------")
        # print(loc_robot, dir)
        old_loc = loc_robot
        loc_robot = move_the_robot(grid, old_loc, dir)
        # print_grid(grid)
        # print(loc_robot)
    
    sum_of_boxes = calculate_sum(grid)
    print(f"Solution for Part 1: {sum_of_boxes}")

def move_the_robot(grid, old_loc, dir):
    new_loc = tuple(map(sum, zip(old_loc, dir)))
    if not is_in_grid(grid, new_loc):
        return old_loc
    value_old = grid[old_loc[0]][old_loc[1]]
    value_new = grid[new_loc[0]][new_loc[1]]
    if value_new == '#':
        return old_loc
    if value_new == '.':
        grid[new_loc[0]][new_loc[1]] = value_old
        grid[old_loc[0]][old_loc[1]] = '.'
        return new_loc
    elif value_new == 'O':
        returnable = move_the_robot(grid, new_loc, dir)
        if returnable == new_loc:
            return old_loc
        else:
            grid[new_loc[0]][new_loc[1]] = value_old
            grid[old_loc[0]][old_loc[1]] = '.'
            return new_loc

if __name__ == "__main__":
    main()