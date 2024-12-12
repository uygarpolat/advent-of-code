from collections import defaultdict

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            print(grid[row][col], end="")
        print("")

def traverse(grid, loc, visited):
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    area = 1
    perimeter = 0

    for dir in dirs:
        new_loc = tuple(map(sum, zip(loc, dir)))
        if new_loc in visited:
            if grid[loc[0]][loc[1]] != grid[new_loc[0]][new_loc[1]]:
                perimeter += 1
            continue
        if not is_in_grid(grid, new_loc):
            perimeter += 1
            continue
        if grid[loc[0]][loc[1]] != grid[new_loc[0]][new_loc[1]]:
            perimeter += 1
        else:
            visited.add(new_loc)
            local_area, local_perimeter = traverse(grid, new_loc, visited)
            area += local_area
            perimeter += local_perimeter
    return area, perimeter

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
        table = defaultdict(list)
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                loc = (row,col)
                if not loc in visited:
                    visited.add(loc)
                    area, perimeter = traverse(grid, loc, visited)
                    combo = (area, perimeter)
                    table[grid[row][col]].append(combo)
        # print(list(table.keys()))
        # print(list(table.values()))
        total_price = 0
        for key in table:
            price = 0
            for i in range(len(table[key])):
                price += table[key][i][0] * table[key][i][1]
            # print(f"price of {key} is {price}")
            total_price += price
        print(total_price)
                
if __name__ == "__main__":
    main()