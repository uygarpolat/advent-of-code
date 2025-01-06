def execute_moves(start_h, start_t, visited, move, count):
    dirs_char = ['U', 'D', 'L', 'R']
    dirs_num = [(-1,0), (1,0), (0,-1), (0,1)]
    index = dirs_char.index(move)
    dir = dirs_num[index]

    for i in range(count):
        start_h = tuple(map(sum, zip(start_h, dir)))
        if abs(start_t[0] - start_h[0]) > 1 or abs(start_t[1] - start_h[1]) > 1:
            start_t = get_new_tail(start_h, start_t)
            visited.add(start_t)
    return start_h, start_t

def get_new_tail(start_h, start_t):
    dirs = [(-1,0), (1,0), (0,-1), (0,1), (1,1), (-1,-1), (1,-1), (-1,1)]

    for dir in dirs:
        new_dir = tuple(map(sum, zip(start_t, dir)))
        temp1 = abs(new_dir[0] - start_h[0])
        temp2 = abs(new_dir[1] - start_h[1])
        if temp1 + temp2 == 1:
            return new_dir
        
def main():
    filepath = "input.txt"
    visited = set()
    start_h = (0,0)
    start_t = (0,0)
    visited.add(start_t)

    with open(filepath, 'r') as file:
        for line in file:
            move, right = line.strip().split()
            count = int(right)
            start_h, start_t = execute_moves(start_h, start_t, visited, move, count)

    print(f"Solution for Part 1: {len(visited)}")

if __name__ == "__main__":
    main()