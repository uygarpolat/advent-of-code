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

def print_grid(grid, visited, flag=1):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            temp = grid[row][col]
            if flag and (row,col) in visited:
                temp = 'O'
            if flag:
                print(temp, end="")
        if flag:
            print("")

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]

    pq = PriorityQueue()
    step_count = 0
    start_loc = (0,1)
    old_dir = (1,0)
    pq.put((step_count, start_loc, old_dir, frozenset([start_loc])))

    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    dirs_char_opp = ['^', '<', 'v', '>']
    dirs_char_same = ['v', '>', '^', '<']
    solutions = []
    
    memo = defaultdict(lambda: float('-inf'))

    while not pq.empty():
        step, old_loc, old_dir, visited = pq.get()
        
        state = (old_loc, old_dir, visited)
        if step <= memo[state]:
            continue
        memo[state] = step

        if old_loc == (len(grid) - 1, len(grid[0]) - 2):
            if step not in solutions:
                solutions.append(step)
                print(f"One unique solution for Part 1: {abs(step)}")
            continue

        for dir in dirs:
            new_loc = tuple(map(sum, zip(old_loc, dir)))
            dir_delta = tuple(map(sum, zip(old_dir, dir)))
            
            if (not is_in_grid(grid, new_loc) or 
                grid[new_loc[0]][new_loc[1]] == '#' or 
                dir_delta == (0,0) or 
                new_loc in visited):
                continue

            index = dirs.index(dir)
            if grid[new_loc[0]][new_loc[1]] == dirs_char_opp[index]:
                continue
                
            new_visited = frozenset(visited | {new_loc})
            
            if grid[new_loc[0]][new_loc[1]] == '.':
                pq.put((step - 1, new_loc, dir, new_visited))
            else:
                pq.put((step - 1, new_loc, dir, new_visited))
                index = dirs_char_same.index(grid[new_loc[0]][new_loc[1]])
                next_loc = tuple(map(sum, zip(new_loc, dirs[index])))
                if next_loc not in visited:
                    next_visited = frozenset(new_visited | {next_loc})
                    pq.put((step - 2, next_loc, dir, next_visited))
    
    print(f"Solution for Part 1: {-min(solutions)}")

if __name__ == "__main__":
    main()