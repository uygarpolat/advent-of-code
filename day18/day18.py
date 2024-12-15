def main():
    file_path = "input.txt"
    digs = {}
    edges = []
    start = (0,0)
    dirs_num = [(1,0),(0,1),(-1,0),(0,-1)]
    dirs_alp = ['D', 'R', 'U', 'L']
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            digs[i] = [int(part.strip()) if j == 1 else part.strip('()') for j, part in enumerate(line.split())]
            digs[i][0] = next(dirs_num[j] for j in range(len(dirs_alp)) if digs[i][0] == dirs_alp[j])
            for _ in range(digs[i][1]):
                start = tuple(map(sum, zip(start,digs[i][0])))
                edges.append((start, digs[i][2]))
    # print(digs)
    print(edges)
    # ff_x = digs[0][0][0] + digs[0][1]
    # ff_y = digs[0][0][1] + digs[0][1]
    # move_back = (-digs[0][0][0], -digs[0][0][1])
    # move_new = tuple(map(sum, zip((ff_x, ff_y), move_back)))
    # flood_fill_start_loc = zi(digs[0][0], digs[0][1]) tuple(map(sum, zip(a, b)))
            

if __name__ == "__main__":
    main()