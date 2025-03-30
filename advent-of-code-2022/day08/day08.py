def rot_90_c_clock(grid):
    return list(zip(*grid))[::-1]

def rot_90_clock(grid):
    return list(zip(*grid[::-1]))

def calculate_visibility_amount(grid, row, col):
    res1 = 0
    res2 = 1
    part_one, part_two = get_left_right_visibility(grid[row], col)
    res1 += part_one
    res2 *= part_two
    grid = rot_90_clock(grid)
    part_one, part_two = get_left_right_visibility(grid[col], len(grid) - row - 1)
    res1 += part_one
    res2 *= part_two
    grid = rot_90_c_clock(grid)
    if res1:
        return 1, res2
    return 0, res2

def get_left_right_visibility(row, index):
    part_one = 0
    left = row[:index]
    right = row[index+1:]
    target = row[index]

    if all(x<target for x in left):
        part_one = 1
    
    if all(y<target for y in right):
        part_one = 1

    temp1 = 0
    for i in range(len(left) - 1, -1, -1):
        temp1 += 1
        if left[i] >= target:
            break

    temp2 = 0
    for i in range(len(right)):
        temp2 += 1
        if right[i] >= target:
            break

    part_two = temp1 * temp2
    return part_one, part_two

def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        grid = [[int(c) for c in line.strip()] for line in file]
    vis_count = 0
    maximum_part_two = 0

    rows = len(grid)
    cols = len(grid[0])
    for row in range(1, rows - 1, 1):
        for col in range(1, cols - 1, 1):
            part_one, part_two = calculate_visibility_amount(grid, row, col)
            vis_count += part_one
            if maximum_part_two < part_two:
                maximum_part_two = part_two
                
    print(f"Solution for Part 1: {vis_count + (rows + cols - 2) * 2}")
    print(f"Solution for Part 2: {maximum_part_two}")

if __name__ == "__main__":
    main()