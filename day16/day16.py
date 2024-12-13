from multiprocessing import Process, Queue
from datetime import datetime
import time

def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            print(grid[row][col], end="")
        print("")

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def start_process(grid, output_queue, processes, dir, loc):
    process = Process(target=execute_ray, args=(grid, output_queue, processes, dir, loc))
    processes.append(process)
    process.start()

def wait_for_processes(processes):
    for p in processes:
        p.join()
        print("Process joined...")

def execute_ray(grid, output_queue, processes, dir, loc):
    dirs = [(1,0), (0,-1), (-1,0), (0,1)]
    # dir = (0,1)
    # loc = (0,-1)
    while(True):
        loc = tuple(map(sum, zip(loc, dir)))
        dir_index = dirs.index(dir)
        if not is_in_grid(grid, loc):
            break
        output_queue.put(loc)
        symbol = grid[loc[0]][loc[1]]
        if symbol == '.' or (symbol == '|' and dir[1] == 0) or (symbol == '-' and dir[0] == 0):
            continue
        elif symbol == '/':
            if dir[1] == 0:
                dir = dirs[(dir_index+1)%4]
            elif dir[0] ==  0:
                dir = dirs[(dir_index-1)%4]
        elif symbol == '\\':
            if dir[1] == 0:
                dir = dirs[(dir_index-1)%4]
            elif dir[0] ==  0:
                dir = dirs[(dir_index+1)%4]
        elif (symbol == '|' and dir[0] == 0) or (symbol == '-' and dir[1] == 0):
            dir1 = (dir[1], dir[0])
            dir2 = (-dir[1], -dir[0])
            start_process(grid, output_queue, processes, dir1, loc)
            dir = dir2

def main():
    file_path = "input2.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    output_queue = Queue()
    processes = []

    execute_ray(grid, output_queue, processes, (0, 1), (0, -1))
    if processes:
        wait_for_processes(processes)
    else:
        print("No processes...")

    # Collect unique results
    results = set()
    while not output_queue.empty():
        results.add(output_queue.get())
    # print(results)
    print(f"Unique results count: {len(results)}")

if __name__ == "__main__":
    main()