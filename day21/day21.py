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
    visited_just_coord = set()
    required_steps = 26501365

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    loc_start = print_grid(grid, visited, 0)

    pq = PriorityQueue()
    pq.put((0, loc_start))
    visited.add((0, loc_start))
    visited_just_coord.add(loc_start)
    
    while not pq.empty():
        move_count, old_loc = pq.get()
        for dir in dirs:
            new_loc = tuple(map(sum, zip(old_loc, dir)))
            if is_in_grid(grid, new_loc) and grid[new_loc[0]][new_loc[1]] != '#' and not new_loc in visited_just_coord:
                pq.put((move_count + 1, new_loc))
                visited.add((move_count + 1, new_loc))
                visited_just_coord.add(new_loc)

    part_two_coefficient = (required_steps - len(grid) // 2) // len(grid)
    part_one_solution = 0
    visited_odd = 0
    visited_even = 0
    visited_corner_odd = 0
    visited_corner_even = 0
    for move, _ in visited:
        if move % 2 == 0:
            visited_even += 1
        else:
            visited_odd += 1
        if move <= 64 and move % 2 == 0:
            part_one_solution += 1
        if move > 65:
            if move % 2 == 0:
                visited_corner_even += 1
            else:
                visited_corner_odd += 1

    print(f"Solution for Part 1: {part_one_solution}")
    print(f"Solution for Part 2: {calculate_second_part(visited_odd, visited_even, visited_corner_odd, visited_corner_even, part_two_coefficient)}")

def calculate_second_part(visited_odd, visited_even, visited_corner_odd, visited_corner_even, part_two_coefficient):
    return (
        ((part_two_coefficient + 1) ** 2) * visited_odd
        + (part_two_coefficient ** 2) * visited_even
        - (part_two_coefficient + 1) * visited_corner_odd
        + part_two_coefficient * visited_corner_even)

if __name__ == "__main__":
    main()