class Keypad:
    pad = ['x^A', '<v>']

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = len(grid[0])

    if rows == 4 and loc == (3,0):
        return 0
    elif rows == 2 and loc == (0,0):
        return 0
    if 0 <= loc[0] < rows and 0 <= loc[1] < cols:
        return 1
    return 0

def main():
    file_path = "input2.txt"
    with open(file_path, 'r') as file:
        sequences = [line.strip() for line in file]
    numpad = ['789', '456', '123', 'X0A']
    keypad1 = Keypad()
    result = 0

    for sequence in sequences:
        list_of_moves = ""
        start_of_target_pad = (3,2)
        for char_target_in_target_pad in sequence:
            list, start_of_target_pad = move_pad(numpad, char_target_in_target_pad, start_of_target_pad)
            list_of_moves += list + 'A'

        list_of_moves_2 = ""
        start_of_target_pad = (0,2)
        for move in list_of_moves:
            list, start_of_target_pad = move_pad(keypad1.pad, move, start_of_target_pad)
            list_of_moves_2 += list + 'A'

        list_of_moves_3 = ""
        start_of_target_pad = (0,2)
        for move in list_of_moves_2:
            list, start_of_target_pad = move_pad(keypad1.pad, move, start_of_target_pad)
            list_of_moves_3 += list + 'A'
 
        result += len(list_of_moves_3) * int(sequence[:-1])

        print(f"My solution for {sequence}: {list_of_moves_3}")

def move_pad(pad, char_target_in_target_pad, start_of_target_pad):

    target_loc = find_character_location(pad, char_target_in_target_pad)
    list_of_moves = execute_moves(target_loc, start_of_target_pad)
    return list_of_moves, target_loc

def execute_moves(target_loc, start_of_keypad):
    list_of_moves = ""
    dir0 = target_loc[0] - start_of_keypad[0]
    dir1 = target_loc[1] - start_of_keypad[1]

    # Theory 1: If one is smaller, do the smaller one first
    # Theory 2: Decrement them at the same pace
    # Both theories seem to miss something.
    
    char_x = ""
    char_y = ""

    if dir0 < 0:
        char_x = '^'
        dir0 = -dir0
    else:
        char_x = 'v'

    if dir1 < 0:
        char_y = '<'
        dir1 = -dir1
    else:
        char_y = '>'

    minimum = min(dir0, dir1)
    maximum = max(dir0, dir1)

    for _ in range(minimum):
        if minimum == dir0:
            list_of_moves += char_x
        else:
            list_of_moves += char_y

    for _ in range(maximum):
        if maximum == dir1:
            list_of_moves += char_y
        else:
            list_of_moves += char_x

    return list_of_moves  

def find_character_location(pad, char):
    for row_idx, row in enumerate(pad):
        for col_idx, col_char in enumerate(row):
            if col_char == char:
                return (row_idx, col_idx)

if __name__ == "__main__":
    main()