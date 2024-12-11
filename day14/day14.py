def print_grid(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            print(grid[row][col], end="")
        print("")

def sort_row(row):
    sorted_list = sorted(row, key=lambda x: x != 'O')
    return(sorted_list)

def divide_row(row):

    replacement_row = []

    while(row):
        if '#' in row:
            index = row.index('#')
            # print(f"Found # at index {index}")
            first_part = row[:index]
            # print(f"first_part is {first_part}")
            replacement_row.extend(sort_row(first_part))
            replacement_row.append('#')
            row = row[index+1:] # Second part
            # print(f"second_part is {row}")
        else:
            replacement_row.extend(sort_row(row))
            row = []

    return replacement_row

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
        # grid_rotated_90_degree_clockwise = list(zip(*grid[::-1]))
        grid_rotated_90_degree_counterclockwise = list(zip(*grid))[::-1]
        # print_grid(grid)
        # print("----")
        for i in range(len(grid_rotated_90_degree_counterclockwise)):
            grid_rotated_90_degree_counterclockwise[i] = divide_row(
                grid_rotated_90_degree_counterclockwise[i])
        grid2 = list(zip(*grid_rotated_90_degree_counterclockwise[::-1]))
        # print_grid(grid2)

        count = 0
        for i, row in enumerate(grid2):
            count += row.count('O') * (len(grid) - i)
        print(count)

if __name__ == "__main__":
    main()