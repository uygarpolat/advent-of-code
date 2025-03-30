
def match_grids(grid2, row, col, result):
    num = ''
    for i in range(len(result)):
        num += grid2[row][col + i]

    try:
        if (int(num) == int(result)):
            return 0
    except ValueError:
        return 1
    return 1

def compare_grids(grid, grid2):
    total = 0
    for row_idx, row in enumerate(grid):
        result = ''
        for col_idx, cell in enumerate(row):
            if not cell.isdigit():
                if result:
                    if match_grids(grid2, row_idx, col_idx - len(result), result):
                        total += int(result)
                    result = ''
                continue
            else:
                result += cell
                if col_idx + 1 == len(grid[0]):
                    if match_grids(grid2, row_idx, col_idx - len(result) + 1, result):
                        total += int(result)
                    
    print(f"Sum is {total}")

def modify_storage(grid2, row, col):
    rows = len(grid2)
    cols = len(grid2[0])
    for rw in range(row - 1, row + 2):
        for cl in range(col - 1, col + 2):
            if (0 <= rw < rows and 0 <= cl < cols):
                grid2[rw][cl] = 'x'

def what_is_the_number(grid, rw, cl):
    res = ''
    rows = len(grid)
    cols = len(grid[0])
    for i in range(5):
        if (0 <= cl - i < cols):
            if grid[rw][cl - i].isdigit():
                res += grid[rw][cl - i]
            else:
                break
    res = res[::-1]
    for i in range(5):
        if (0 <= cl + 1 + i < cols):
            if grid[rw][cl + 1 + i].isdigit():
                res += grid[rw][cl + 1 + i]
            else:
                break
    return int(res)


def check_gear(grid, row, col):
    number = 1
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    for rw in range(row - 1, row + 2):
        for cl in range(col - 1, col + 2):
            if (0 <= rw < rows and 0 <= cl < cols):
                if grid[rw][cl].isdigit():
                    if cl == col:
                        number *= what_is_the_number(grid, rw, cl)
                        count += 1
                    elif rw == row:
                        number *= what_is_the_number(grid, rw, cl)
                        count += 1
                    elif not grid[rw][col].isdigit():
                        number *= what_is_the_number(grid, rw, cl)
                        count += 1
    if count == 2:
        return number
    return 0

def main():
    import copy

    number = 0
    with open("input.txt", 'r') as file:
        grid = [list(line.strip()) for line in file]
        grid2 = copy.deepcopy(grid)

        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                if not cell.isdigit() and cell != '.':
                    modify_storage(grid2, row_idx, col_idx)
                    number += check_gear(grid, row_idx, col_idx)
        print(f"Gear total is {number}")
        compare_grids(grid, grid2)

if __name__ == "__main__":
    main()
