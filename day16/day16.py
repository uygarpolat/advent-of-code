from collections import defaultdict
from collections import deque

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= loc[0] < rows and 0 <= loc[1] < cols

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]

    dirs = [(1,0), (0,-1), (-1,0), (0,1)]

    edges = defaultdict()
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if col == 0:
                initial_dir = (0,1)
                initial_loc = (row,-1)
            elif row == 0:
                initial_dir = (1,0)
                initial_loc = (-1,col)
            elif row == rows - 1:
                initial_dir = (-1,0)
                initial_loc = (rows,col)
            elif col == cols - 1:
                initial_dir = (0,-1)
                initial_loc = (row,cols)
            edges[initial_loc] = initial_dir
    maximum = 0
    for key, value in edges.items():
        initial_loc = key
        initial_dir = value

        queue = deque()
        queue.append((initial_loc, initial_dir))

        visited = set()
        output = set()

        while queue:
            loc, dir = queue.popleft()

            new_loc = (loc[0] + dir[0], loc[1] + dir[1])

            if not is_in_grid(grid, new_loc):
                continue
            if (new_loc, dir) in visited:
                continue
            visited.add((new_loc, dir))
            output.add(new_loc)

            symbol = grid[new_loc[0]][new_loc[1]]
            dirs_index = dirs.index(dir)

            if symbol == '.' or (symbol == '|' and dir[1] == 0) or (symbol == '-' and dir[0] == 0):
                queue.append((new_loc, dir))
            elif symbol == '/':
                if dir[1] == 0:  # vertical
                    new_dir = dirs[(dirs_index+1)%4]
                else:
                    new_dir = dirs[(dirs_index-1)%4]
                queue.append((new_loc, new_dir))
            elif symbol == '\\':
                if dir[1] == 0:
                    new_dir = dirs[(dirs_index-1)%4]
                else:
                    new_dir = dirs[(dirs_index+1)%4]
                queue.append((new_loc, new_dir))
            elif (symbol == '|' and dir[0] == 0) or (symbol == '-' and dir[1] == 0):
                dir1 = (dir[1], dir[0])
                dir2 = (-dir[1], -dir[0])

                # Enqueue both directions
                queue.append((new_loc, dir1))
                queue.append((new_loc, dir2))
        if initial_dir == (0,1) and initial_loc == (0,-1):
            print(f"Solution for Part 1: {len(output)}")
        if maximum < len(output):
            maximum = len(output)
    print(f"Solution for Part 2: {maximum}")

if __name__ == "__main__":
    main()
