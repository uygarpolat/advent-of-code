def main():
    file_path = "input.txt"
    digs = {}
    edges = []
    start = (0,0)
    steps = []

    dirs_num = [(0,1),(1,0),(0,-1),(-1,0)]
    dirs_alp = ['R', 'D', 'L', 'U']

    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            # Part 1 calculations
            digs[i] = [int(part.strip()) if j == 1 else part.strip('()') for j, part in enumerate(line.split())]
            digs[i][0] = next(dirs_num[j] for j in range(len(dirs_alp)) if digs[i][0] == dirs_alp[j])
            for _ in range(digs[i][1]):
                start = tuple(map(sum, zip(start, digs[i][0])))
                edges.append((start, digs[i][2]))

            # Part 2 calculations
            hex_number = int(digs[i][2][1:-1], 16)
            hex_dir = digs[i][2][-1]
            steps.append((hex_dir,hex_number))

    perimeters = set(mem[0] for mem in edges)
    interior = set()
    traverse_2(perimeters, interior, (1,1))
    joined = set(perimeters).union(interior)
    print(f"Solution for Part 1: {len(joined)}")

    area = polygon_area(steps)
    print(f"Solution for Part 2: {area}")

# Attempt #1 with recursion
def traverse(perimeters, interior, old_loc):
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    if old_loc in perimeters:
        return
    if not old_loc in interior:
        interior.add(old_loc)
    
    for dir in dirs:
        new_loc = tuple(map(sum, zip(old_loc, dir)))
        if new_loc in perimeters or new_loc in interior:
            continue
        else:     
            traverse(perimeters, interior, new_loc)
            
# Attempt #2 with stacks
def traverse_2(perimeters, interior, start):
    stack = [start]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]

    while stack:
        old_loc = stack.pop()
        if old_loc in perimeters or old_loc in interior:
            continue
        interior.add(old_loc)

        for d in dirs:
            new_loc = (old_loc[0] + d[0], old_loc[1] + d[1])
            if new_loc not in perimeters and new_loc not in interior:
                stack.append(new_loc)

def polygon_area(steps):

    direcmap = {
        "0": (0, 1),
        "1": (1, 0),
        "2": (0, -1),
        "3": (-1, 0)
    }

    x, y = 0, 0
    perimeter = 0
    area = 0

    for direc, length in steps:
        dy, dx = direcmap[direc]
        dy, dx = dy * length, dx * length

        y, x = y + dy, x + dx
        perimeter += length

        area += x * dy

    total_area = area + perimeter // 2 + 1
    return total_area

if __name__ == "__main__":
    main()