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

def traverse(grid, loc, visited, local_visited):
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
            local_visited.add(new_loc)
            local_area, local_perimeter = traverse(grid, new_loc, visited, local_visited)
            area += local_area
            perimeter += local_perimeter
    return area, perimeter

def get_part_two_perimeters(local_visited):
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    first_elements, second_elements = zip(*local_visited)
    max_first = max(first_elements)
    max_second = max(second_elements)
    min_first = min(first_elements)
    min_second = min(second_elements)

    corner_count = 0
    for row in range(min_first, max_first + 1, 1):
        for col in range(min_second, max_second + 1, 1):
            loc = (row, col)

            for i in range(len(dirs)):
                new_loc1 = tuple(map(sum, zip(loc, dirs[i])))
                new_loc2 = tuple(map(sum, zip(loc, dirs[(i+1)%len(dirs)])))
                new_dir = tuple(map(sum, zip(dirs[i],dirs[(i+1)%len(dirs)])))
                new_loc_3 = tuple(map(sum, zip(loc, new_dir)))
                locs3 = [new_loc1, new_loc2, new_loc_3]
                locs2 = [new_loc1, new_loc2]

                if loc in local_visited:
                    if all(element not in local_visited for element in locs3):
                        corner_count += 1
                else:
                    if all(element in local_visited for element in locs2):
                        corner_count += 1
    return corner_count

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
        table = defaultdict(list)
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        part_two_region_price = 0
        for row in range(rows):
            for col in range(cols):
                loc = (row,col)
                if not loc in visited:
                    local_visited = set()
                    local_visited.add(loc)
                    visited.add(loc)
                    area, perimeter = traverse(grid, loc, visited, local_visited)
                    part_two_perimeters = get_part_two_perimeters(local_visited)
                    part_two_region_price += area * part_two_perimeters
                    local_visited = ()
                    combo = (area, perimeter)
                    table[grid[row][col]].append(combo)
        total_price = 0
        for key in table:
            price = 0
            for i in range(len(table[key])):
                price += table[key][i][0] * table[key][i][1]
            total_price += price
        print(f"Solution for Part 1: {total_price}")
        print(f"Solution for Part 2: {part_two_region_price}")
                
if __name__ == "__main__":
    main()