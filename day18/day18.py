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

def print_grid(grid_size, first_n_coordinates):
    rows = grid_size
    cols = grid_size
    for row in range(cols):
        for col in range(rows):
            if (col,row) in first_n_coordinates:
                print("#", end="")
            else:
                print(".", end="")
        print("")

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        coordinates = tuple(tuple(int(num) for num in line.strip().split(',')) for line in file)
    # print(coordinates)
    
    dirs = [(1,0),(0,1),(-1,0),(0,-1)]
    grid_size = 71
    first_n = 1024
    first_n_coordinates = coordinates[:first_n]
    # print_grid(grid_size, first_n_coordinates)
    logbook = defaultdict(lambda: 1000000)
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
    print(logbook[(grid_size - 1, grid_size - 1)])

    

if __name__ == "__main__":
    main()