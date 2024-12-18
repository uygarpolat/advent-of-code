from queue import PriorityQueue
from collections import defaultdict

def is_in_grid(grid_size, loc):
    rows = grid_size
    cols = grid_size
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        coordinates = tuple(tuple(int(num) for num in line.strip().split(',')) for line in file)
    
    defaultdict_value = 1000000
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    grid_size = 71
    for i in range(1024, len(coordinates), 1):
        first_n = i
        first_n_coordinates = coordinates[:first_n]
        logbook = defaultdict(lambda: defaultdict_value)
        logbook.clear()
        pq = PriorityQueue()
        logbook[(0,0)] = 0
        pq.put((logbook[(0,0)], (0,0)))

        while not pq.empty():
            priority, old_loc = pq.get()
            for dir in dirs:
                new_loc = tuple(map(sum, zip(old_loc, dir)))
                if not is_in_grid(grid_size, new_loc) or new_loc in first_n_coordinates:
                    continue
                if logbook[new_loc] > priority + 1:
                    logbook[new_loc] = priority + 1
                    pq.put((logbook[new_loc], new_loc))
                if logbook[(grid_size - 1, grid_size - 1)] != defaultdict_value:
                    pq.empty()
                    break
        local_solution = logbook[(grid_size - 1, grid_size - 1)]
        if i == 1024:
            print(f"Solution for Part 1: {local_solution}")
        if local_solution == defaultdict_value:
            print(f"Solution for Part 2: {",".join(map(str, first_n_coordinates[-1]))}")
            return    

if __name__ == "__main__":
    main()