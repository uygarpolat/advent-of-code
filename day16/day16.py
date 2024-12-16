from collections import deque
from collections import defaultdict


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




def traverse(grid, loc_cur, loc_end, old_dir, logbook):
    print(f"Testing {loc_cur}")
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]

    value_loc_cur = grid[loc_cur[0]][loc_cur[1]]
    value_loc_end = grid[loc_end[0]][loc_end[1]]
    loc_cur_logbook_value = logbook[loc_cur]
    
    for new_dir in dirs:
        boost = 1
        if new_dir[0] + old_dir[0] == 0 and new_dir[1] + old_dir[1] == 0:
            continue
        if new_dir[0] != old_dir[0] or new_dir[1] == old_dir[1]:
            boost == 1000
        else:
            boost == 0
        
        loc_new = tuple(map(sum, zip(loc_cur, new_dir)))
        value_loc_new = grid[loc_new[0]][loc_new[1]]
        loc_new_logbook_value = logbook[loc_new]

        if value_loc_new == '#':
            continue

        
        if value_loc_new == value_loc_end:
            logbook[loc_new].append(loc_cur_logbook_value + loc_new_logbook_value)
            return
        else:
            if logbook[loc_new] > boost + 1 + loc_cur_logbook_value:
                logbook[loc_new] = boost + 1 + loc_cur_logbook_value
                traverse(grid, loc_new, loc_end, new_dir, logbook)
    return

def main():
    file_path = "input3.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    loc_cur, loc_end = print_grid(grid, 0)
    print(loc_cur, loc_end)

    logbook = defaultdict(lambda: 1000000000)
    logbook[loc_cur] = 0
    logbook[loc_end] = []

    traverse(grid, loc_cur, loc_end, (0,1), logbook)
    print(logbook)

if __name__ == "__main__":
    main()