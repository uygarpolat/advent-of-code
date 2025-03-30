def move_next(c, start, prev):
    result = (0,0)
    table = {
        '|': [(-1,0),(1,0)],
        '-': [(0,-1),(0,1)], 
        'L': [(-1,0),(0,1)], 
        'J': [(0,-1),(-1,0)], 
        '7': [(0,-1),(1,0)], 
        'F': [(0,1),(1,0)], 
        '.': [(0,0),(0,0)], 
        'S': [(0,0),(0,0)], 
    }

    res = tuple(map(lambda i, j: i - j, prev, start))
    if table[c][0] == res:
        result = table[c][1]
    elif table[c][1] == res:
        result = table[c][0]
    temp = tuple(map(lambda i, j: i + j, start, result))
    return temp

def traverse(grid, loc):
    path = []
    prev = loc
    start = tuple(map(lambda i, j: i + j, loc, (-1,0))) # This line and one other line need to be modified accordingly for other maps

    path.append(start)
    count = 1
    i = 0
    while(True):
        c = grid[start[0]][start[1]]
        # print(c)
        if c == 'S':
            return count, path
        else:
            next = move_next(c, start, prev)
            path.append(next)
            count += 1
            prev = start
            start = next
        i += 1

def get_loc(grid, char):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == char:
                return (row,col)

def main():
    file_path = "input.txt"
    path = []
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
        s_loc = get_loc(grid, 'S')
        move_count, path = traverse(grid, s_loc)
        print(f"Solution for Part 1: {int(move_count / 2)}")

        rows = len(grid)
        cols = len(grid[0])
        in_count = 0
        out_count = 0
        what_is_s = 'L' # This line and one other line need to be modified accordingly for other maps
        for row in range(rows):
            toggle = 0
            for col in range(cols):
                c = grid[row][col]
                if c == 'S':
                    c = what_is_s
                if c == 'F' and (row,col) in path:
                    while(col+1 < cols and grid[row][col+1] == '-'):
                        col += 1
                    if grid[row][col+1] == 'J':
                        toggle += 1
                elif c == 'L' and (row,col) in path:
                    while(col+1 < cols and grid[row][col+1] == '-'):
                        col += 1
                    if grid[row][col+1] == '7':
                        toggle += 1
                elif c == '|' and (row,col) in path:
                    toggle += 1
                elif toggle % 2 == 1 and not (row,col) in path:
                    in_count += 1
                else:
                    out_count += 1
        print(f"Solution for Part 2: {in_count}")

if __name__ == "__main__":
    main()