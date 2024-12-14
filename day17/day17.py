def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= loc[0] < rows and 0 <= loc[1] < cols

def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            print(grid[row][col], end="")
        print("")

def traverse(grid, heatmap, loc, running_tally, old_dir, straight_count):
    dirs = [(1,0), (0,-1), (-1,0), (0,1)]
    min_tally = 100
    do_not_go_dir = (-old_dir[1],-old_dir[0])
    index = -1

    for i, dir in enumerate (dirs):
        if dir == do_not_go_dir or (dir == old_dir and straight_count == 3):
            continue
        new_loc = tuple(sum(zip(dir, loc))) # (0,1)
        if not is_in_grid(new_loc):
            return 0
        tally_of_new_loc = grid[new_loc[0]][new_loc[1]] # 4

        if min_tally > running_tally + tally_of_new_loc:
            min_tally = running_tally + tally_of_new_loc
            index = i

        if not new_loc in heatmap:
            heatmap[new_loc] = running_tally + tally_of_new_loc # 4

        traverse(grid, heatmap, new_loc, running_tally, old_dir, heatmap[new_loc])
    return min_tally


def main():
    file_path = "input2.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    heatmap = {}
    loc = (0,0)
    running_tally = 0
    straight_count = 0
    heat_loss1 = traverse(grid, heatmap, loc, running_tally, (1,0), straight_count)
    heat_loss2 = traverse(grid, heatmap, loc, running_tally, (0,1), straight_count)
    print(min(heat_loss1,heat_loss2))
if __name__ == "__main__":
    main()