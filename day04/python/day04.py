def read_grid(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def search_xmas(grid, row, col, sequence):

    counter = 0
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    for dr, dc in directions:
        found = True
        r, c = row, col
        for char in sequence[1:]:
            r += dr
            c += dc
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != char:
                found = False
                break
        if found:
            counter += 1
    
    return counter


def search_x_mas(grid, row, col, sequence):

    r, c = row, col
    counter = 0
    rows = len(grid)
    cols = len(grid[0])
    directions = [(1, 1), (-1, 1)]
    if not (0 <= row + 1 < rows and 0 <= col + 1 < cols and 0 <= row - 1 < rows and 0 <= col - 1 < cols):
        return 0
    
    found = 0
    for i, char in enumerate(sequence):
        for dr, dc in directions:
            if grid[r + dr][c + dc] == char and grid[r - dr][c - dc] == sequence[(i + 1) % 2]:
                found += 1
    if found == 2:
        return 1
    return 0

def main():
    xmas_counter = 0
    x_mas_counter = 0
    grid = read_grid("input.txt")
    
    sequence_xmas = "XMAS"
    sequence_mas = "MAS"
    middle_index = len(sequence_mas) // 2
    for row_idx, row in enumerate(grid):
        for col_idx, cell in enumerate(row):
            if cell == sequence_xmas[0]:
                xmas_counter += search_xmas(grid, row_idx, col_idx, sequence_xmas)
            if cell == sequence_mas[middle_index]:
                x_mas_counter += search_x_mas(grid, row_idx, col_idx, sequence_mas[:middle_index] + sequence_mas[middle_index + 1:])
    print(f"XMAS count: {xmas_counter}")
    print(f" MAS count: {x_mas_counter}")

if __name__ == "__main__":
    main()