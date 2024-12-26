from queue import PriorityQueue
import copy

def is_in_grid(grid, loc):
    rows = len(grid)
    cols = 3

    if rows == 4 and loc == (3,0):
        return 0
    elif rows == 2 and loc == (0,0):
        return 0
    if 0 <= loc[0] < rows and 0 <= loc[1] < cols:
        return 1
    return 0

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        sequences = [line.strip() for line in file]

    pq = PriorityQueue()

    total = 0
    for sequence in sequences:
        numpad_pointer = (3,2)
        keypad_pointer = (0,2)
        pointers = [keypad_pointer for _ in range(2)] + [numpad_pointer]
        moves = ['<', '>', 'v', '^', 'A']
        final_typed = ""
        num = int(sequence[:-1])

        for c in sequence:
            typed = ""
            gibberish = ""
            move = ""
            cost = 0
            state = [cost, pointers, gibberish, typed]
            pq.put(state)

            while not pq.empty():

                state = pq.get()

                for move in moves:
                    state_new = press_key(state, move, 0)
                    
                    if state_new == None:
                        continue
                    if state_new[0] > 0:
                        if state_new[3] == c:
                            final_typed += state_new[2]
                            pointers = state_new[1]
                            while not pq.empty():
                                pq.get()
                            break
                        if state_new[3] != '':
                            continue
                    
                        pq.put(state_new)
        midsum = len(final_typed) * num
        print(f"midsum for {sequence} is {midsum}")
        total += midsum
    print(f"Solution for Part 1: {total}")
                    
def press_key(state, move, level):

    numpad = ['789', '456', '123', 'x0A']
    keypad = ['x^A', '<v>']
    ultimate_pads = [keypad for _ in range(2)] + [numpad]

    pads = ultimate_pads[level:]
    cost = state[0]
    pointers = state[1][level:]
    gibberish = state[2]
    typed = state[3]

    if level == 0:
        cost += 1
    if move == 'A':
        if level == 0:
            gibberish += 'A'
        if level == len(ultimate_pads) - 1:
            typed = pads[0][pointers[0][0]][pointers[0][1]]
            state_new = [cost, state[1], gibberish, typed]
            return state_new
 
        next_move_loc = pointers[0] # (e.g. (1,1))
        next_move = pads[0][next_move_loc[0]][next_move_loc[1]]
        state_new = [cost, state[1], gibberish, typed]
        return press_key(state_new, next_move, level + 1)

    moves_alp = ['<', '>', 'v', '^']
    moves_num = [(0,-1), (0,1), (1,0), (-1,0)]

    dir = moves_num[moves_alp.index(move)]

    if not path_check(gibberish, dir):
        return None

    target = tuple(map(sum, zip(pointers[0], dir)))

    if is_in_grid(pads[0], target):
        if level == 0:
            gibberish += move

        new_pointers = copy.deepcopy(state[1])
        new_pointers[level] = target
        new_state = [cost, new_pointers, gibberish, typed]
        return new_state
    return None

def path_check(gibberish, dir):
    moves_alp = ['<', '>', 'v', '^']
    moves_num = [(0,-1), (0,1), (1,0), (-1,0)]

    if gibberish:
        last_move_in_char = gibberish[len(gibberish) - 1]
        if last_move_in_char != 'A':
            las_move_in_num = moves_num[moves_alp.index(last_move_in_char)]
            joined = tuple(map(sum, zip(dir,las_move_in_num)))
            if joined == (0,0):
                return False
        if len(gibberish) > 3 and not 'A' in gibberish[-4:]:
            return False
    return True

def find_character_location(pad, char):
    for row_idx, row in enumerate(pad):
        for col_idx, col_char in enumerate(row):
            if col_char == char:
                return (row_idx, col_idx)

if __name__ == "__main__":
    main()