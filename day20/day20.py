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

def simplify_tuple_set(input_set):
    max_dict = {}
    
    for left, right in input_set:
        if left not in max_dict or right > max_dict[left]:
            max_dict[left] = right

    simplified_set = {((a, b), c) for (a, b), c in max_dict.items()}
    return simplified_set

def calculate_best_cheat(setting, target, grid, logbook, key, dirs, move_count, current_move_count, visited):
    if current_move_count > move_count:
        return
    
    state = (key, current_move_count)
    if state in visited:
        return
    visited.add(state)
    
    for dir in dirs:
        new_loc = tuple(map(sum, zip(key, dir)))

        if not is_in_grid(grid, new_loc):
            continue

        if grid[new_loc[0]][new_loc[1]] != '#':
            saving = logbook[new_loc] - target - current_move_count
            if saving > 0 and target < logbook[new_loc]:
                setting.add((new_loc, saving))

        calculate_best_cheat(setting, target, grid, logbook, new_loc, dirs, move_count, current_move_count + 1, visited)
    return

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

    for i in range(2, 21, 18):
        result = 0 
        for key in list(logbook.keys()):
            visited = set()
            setting = set()
            calculate_best_cheat(setting, logbook[key], grid, logbook, key, dirs, i, 1, visited)
            simplified_set = simplify_tuple_set(setting)
            result += sum(1 for _, right in simplified_set if right >= 100)
        print(f"Solution for Part {i//20+1}: {result}")

if __name__ == "__main__":
    main()
