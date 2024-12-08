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

    res = tuple(map(lambda i, j: i - j, prev, start)) # (2,0)-(2,1)=(0,-1)
    # print(f"{start} - {prev} = {res}")
    # print(f"card_strenght[c][0]: {table[c][0]}")
    # print(f"card_strenght[c][1]: {table[c][1]}")
    if table[c][0] == res:
        result = table[c][1] # (0,-1)
    elif table[c][1] == res:
        result = table[c][0] # (-1,0) we want this!
    # print(f"result before test is {result}")
    test = tuple(map(lambda i, j: i + j, start, result))
    # print(f"test is {test}")
    return test


def traverse(grid, loc):
    prev = loc
    start = tuple(map(lambda i, j: i + j, loc, (-1,0)))
    count = 1
    i = 0
    while(True):

        c = grid[start[0]][start[1]]
        # print(c)
        if c == 'S':
            return count
        else:
            next = move_next(c, start, prev)
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
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
        s_loc = get_loc(grid, 'S')
        move_count = traverse(grid, s_loc)
    print(int(move_count / 2))

if __name__ == "__main__":
    main()