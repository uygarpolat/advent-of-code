def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])
    row = loc[0]
    col = loc[1]
    if 0 <= row < rows and 0 <= col < cols:
        return True
    return False

def traverse(grid, row, col, nums, index, loc_list, temp_list):

    count = 0
    new_dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    for new_dir in new_dirs:
        new_loc = (row + new_dir[0], col + new_dir[1])

        if not is_in_grid(grid, new_loc):
            continue
        if grid[new_loc[0]][new_loc[1]] == nums[index]:
            if index == len(nums) - 1:
                count += 1
                if not new_loc in loc_list:
                    loc_list.append(new_loc)
                temp_list.append(new_loc)
                continue
            else:
                sum, loc_list, temp_list = traverse(grid, new_loc[0], new_loc[1], nums, index + 1, loc_list, temp_list)
                count += sum
    return count, loc_list, temp_list
    
def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(map(int, line.strip())) for line in file]
    
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 0
    sum = 0
    total = 0
    loc_list = []
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                temp_list = []
                count, loc_list, temp_list = traverse(grid, row, col, nums, 1, loc_list, temp_list)
                sum += count
                total += len(set(temp_list))
    print(f"Solution for Part 1: {total}")
    print(f"Solution for Part 2: {sum}")

if __name__ == "__main__":
    main()