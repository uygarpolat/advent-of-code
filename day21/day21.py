from queue import PriorityQueue

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
            if temp == 'S':
                loc_start = (row,col)
            if flag and (row,col) in visited:
                temp = 'O'
            if flag:
                print(temp, end="")
        if flag:
            print("")
    return loc_start

def main():
    file_path = "input.txt"
    visited = set()
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    loc_start = print_grid(grid, visited, 0)

    pq = PriorityQueue()
    pq.put((1, loc_start))

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    visited.add(loc_start)
    target_move = 64 + 1

    while not pq.empty():
        move_count, old_loc = pq.get()
        if move_count == target_move:
            continue
        for dir in dirs:
            new_loc = tuple(map(sum, zip(old_loc, dir)))
            if is_in_grid(grid, new_loc) and grid[new_loc[0]][new_loc[1]] != '#' and not new_loc in visited:
                pq.put((move_count + 1, new_loc))
                visited.add(new_loc)
        if old_loc in visited:
            visited.remove(old_loc)

    print(f"Solution for Part 1: {len(visited)}")

if __name__ == "__main__":
    main()