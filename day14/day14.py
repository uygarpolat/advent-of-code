from dataclasses import dataclass
from collections import defaultdict
from functools import reduce
from operator import mul

@dataclass
class Robot:
    pos: list[int]
    vel: tuple[int, int]

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

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
    # print(quads.values())
    return reduce(mul, quads.values(), 1)


def main():
    file_path = "input.txt"
    robots = {}
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            pos, vel = [tuple(map(int, part.lstrip('vp=').split(','))) for part in line.split()]
            robots[i] = Robot(list(pos), vel)
            # print(robots[i].pos[0])

    x_len = 101
    y_len = 103
    iter = 100
    final_state = []
    for i in range(iter):
        for j in robots:
            # print(f"pos: {robots[j].pos}, vel: {robots[j].vel}")
            pos = robots[j].pos
            vel = robots[j].vel
            robots[j].pos = execute_move(pos, vel, x_len, y_len)
            # print(robots[j].pos)
    for k in robots:
        final_state.append(robots[k].pos)
    # print(final_state)
    print(calculate_quadrant(final_state, x_len, y_len))

def display_state(final_state):
    return 0

if __name__ == "__main__":
    main()