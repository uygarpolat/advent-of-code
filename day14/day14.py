from dataclasses import dataclass
from collections import defaultdict
from functools import reduce
from operator import mul
from collections import Counter

@dataclass
class Robot:
    pos: list[int]
    vel: tuple[int, int]

def generate_grid(final_state, x_len, y_len):
    grid = []
    for col in range(y_len):
        grid.append([])
        for row in range(x_len):
            if (row,col) in final_state:
                grid[col].append(final_state.count((row,col)))
            else:
                grid[col].append('.')
    return grid

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

def execute_move(pos, vel, x_len, y_len):
    new_pos_raw = tuple(map(sum, zip(pos, vel)))
    new_pos = (new_pos_raw[0] % x_len, new_pos_raw[1] % y_len)
    return new_pos

def calculate_quadrant(final_state, x_len, y_len):
    quads = defaultdict(int)
    for state in final_state:
        state_x = state[0]
        state_y = state[1]
        if state_x == (x_len - 1) / 2 or state_y == (y_len - 1) / 2:
            continue
        if (state_x < x_len / 2):
            if (state_y < y_len / 2):
                quads[0] += 1
            else:
                quads[1] += 1
        else:
            if (state_y < y_len / 2):
                quads[2] += 1
            else:
                quads[3] += 1
    return reduce(mul, quads.values(), 1)

def main():
    file_path = "input.txt"
    robots = {}
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            pos, vel = [tuple(map(int, part.lstrip('vp=').split(','))) for part in line.split()]
            robots[i] = Robot(list(pos), vel)

    part_one_solution = 0
    x_len = 101
    y_len = 103

    iter = 10000
    for i in range(iter):
        final_state = []
        for j in robots:
            pos = robots[j].pos
            vel = robots[j].vel
            robots[j].pos = execute_move(pos, vel, x_len, y_len)
        for k in robots:
            final_state.append(robots[k].pos)
        if i == 99:
            part_one_solution = calculate_quadrant(final_state, x_len, y_len)
            print(f"Solution for Part 1: {part_one_solution}")
        else:
            maximum_x = max(Counter(x[0] for x in final_state).values())
            maximum_y = max(Counter(y[1] for y in final_state).values())
            if maximum_x > x_len / 4 and maximum_y > y_len / 4:
                print(f"Solution for Part 2: {i+1}")
                if i > 99:
                    return
                
if __name__ == "__main__":
    main()