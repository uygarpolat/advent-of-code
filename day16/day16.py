from collections import deque
from collections import defaultdict
import sys

sys.setrecursionlimit(10000)

def print_set(grid, set):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            temp = grid[row][col]
            if (row,col) in set:
                print("O", end="")
            elif temp == 'S':
                print("S", end="")
            elif temp == 'E':
                print("E", end="")
            elif temp == '#':
                print("#", end="")

            else:
                print(".", end="")
        print("")

def print_grid(grid, flag=1):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            temp = grid[row][col]
            if temp == 'S':
                loc_start = (row,col)
            elif temp == 'E':
                loc_end = (row,col)
            if flag:
                print(temp, end="")
        if flag:
            print("")
    return loc_start, loc_end

def traverse(grid, loc_cur, loc_end, old_dir, logbook, best_set):

    bool_val = 0
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    value_loc_end = grid[loc_end[0]][loc_end[1]]
    loc_cur_logbook_value = logbook[loc_cur]
    
    for new_dir in dirs:
        boost = 0
        if new_dir[0] + old_dir[0] == 0 and new_dir[1] + old_dir[1] == 0:
            continue
        if new_dir[0] != old_dir[0] and new_dir[1] != old_dir[1]:
            boost = 1000
        else:
            boost = 0
        
        loc_new = tuple(map(sum, zip(loc_cur, new_dir)))
        value_loc_new = grid[loc_new[0]][loc_new[1]]

        if value_loc_new == '#':
            continue

        if value_loc_new == value_loc_end:
            if logbook[loc_new] > boost + 1 + loc_cur_logbook_value:
                best_set.add(loc_new)
                logbook[loc_new] = boost + 1 + loc_cur_logbook_value
                return True
            return False
        else:
            if logbook[loc_new] > boost + 1 + loc_cur_logbook_value:
                logbook[loc_new] = boost + 1 + loc_cur_logbook_value
                if traverse(grid, loc_new, loc_end, new_dir, logbook, best_set):
                    best_set.add(loc_new)
                    bool_val = True
    return bool_val

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    loc_cur, loc_end = print_grid(grid, 0)
    print(loc_cur, loc_end)

    logbook = defaultdict(lambda: 1000000000)
    logbook[loc_cur] = 0
    best_set = set()
    best_set.add(loc_cur)

    traverse(grid, loc_cur, loc_end, (0,1), logbook, best_set)
    print(f"Solution for Part 1: {logbook[loc_end]}")
    # print(best_set)
    # print_set(grid, best_set)

if __name__ == "__main__":
    main()