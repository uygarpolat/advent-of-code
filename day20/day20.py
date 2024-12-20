def print_grid(grid, flag=1):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            temp = grid[row][col]
            if temp == 'S':
                loc_start = (row,col)
            elif temp == 'E':
                loc_end = (row,col)
            if flag:
                print(temp, end="")
        if flag:
            print("")
    return loc_start, loc_end

def main():
    file_path = "input2.txt"
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file]
    loc_start, loc_end = print_grid(grid, 0)
    print(loc_start, loc_end)

    

if __name__ == "__main__":
    main()