def main():
    keys_values = []
    locks_values = []
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        schematics = file.read().split('\n\n')
    for schematic in schematics:
        grid = [line.strip() for line in schematic.split('\n')]
        if all(c == '.' for c in grid[0]):
            grid = list(zip(*grid[::-1])) # Rotate grid 90 degrees clockwise for easier calculation
            keys_values.append([row.count('#') - 1 for row in grid])
        else:
            grid = list(zip(*grid[::-1]))
            locks_values.append([row.count('#') - 1 for row in grid])

    count = 0
    length = max(max(max(sublist) for sublist in keys_values), max(max(sublist) for sublist in locks_values))
    for key_values in keys_values:
        for lock_values in locks_values:
            if all(total <= length for total in map(sum, zip(key_values, lock_values))):
                count += 1
    print(f"Solution for Part 1: {count}")


if __name__ == "__main__":
    main()