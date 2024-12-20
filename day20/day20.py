from queue import PriorityQueue
from collections import defaultdict

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

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

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    loc_start, loc_end = print_grid(grid, 0)

    defaultdict_value = 1000000
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    logbook = defaultdict(lambda: defaultdict_value)
    pq = PriorityQueue()
    logbook[loc_start] = 0
    pq.put((logbook[(loc_start)], (loc_start)))

    while not pq.empty():
        priority, old_loc = pq.get()
        for dir in dirs:
            new_loc = tuple(map(sum, zip(old_loc, dir)))
            if grid[new_loc[0]][new_loc[1]] == '#':
                continue
            if logbook[new_loc] > priority + 1:
                logbook[new_loc] = priority + 1
                pq.put((logbook[new_loc], new_loc))
            if logbook[(loc_end[0], loc_end[1])] != defaultdict_value:
                break

    cheat_sheet = defaultdict(lambda: 0)

    for key in logbook:
        cheat_ps_1 = calculate_best_cheat_1(grid, logbook, key, dirs)
        # if key == (7,9):
        #     print(f"Cheat amount for {key} is {cheat_ps}")
        for ps in cheat_ps_1:
            cheat_sheet[ps] += 1

    # for key in cheat_sheet:
    #     print(f"cheat_sheet[{key}]: {cheat_sheet[key]}")
    tally = 0
    for key, value in cheat_sheet.items():
        if key == 0:
            continue
        if key >= 100:
            tally += value
    print(f"Solution for Part 1: {tally}")
    
def calculate_best_cheat_1(grid, logbook, key, dirs):
    delta = [0]
    target = logbook[key]

    for dir in dirs:
        new_loc_1 = tuple(map(sum, zip(key, dir)))
        new_loc_2 = tuple(map(sum, zip(new_loc_1, dir)))
        if not is_in_grid(grid, new_loc_2) or grid[new_loc_2[0]][new_loc_2[1]] == '#':
            continue

        if target < logbook[new_loc_2]:
            delta.append(logbook[new_loc_2] - target - 2)
            # if key == (7,9):
            #     print(f"old time for {key} was {logbook[key]} and new suggested time is {logbook[new_loc_2] - target - 2}")

    return delta




if __name__ == "__main__":
    main()