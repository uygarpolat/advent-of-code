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

    pads = [['x^A', '<v>'], ['x^A', '<v>'], ['789', '456', '123', 'x0A']]
    pointers = [(0,2), (0,2), (3,2)]

    sequences = ["029A"]
    moves = ['<', '>', 'v', '^', 'A']

    for sequence in sequences:
        for c in sequence:
            typed = ""
            gibberish = ""
            move = ""
            cost = 0
            state = [cost, pointers, gibberish, typed]
            pq.put(state)

            while not pq.empty():

                # my_queue = list(pq.queue)
                # for queue in my_queue:
                #     print(queue)
                # input("Press Enter to continue...")
                state = pq.get()

                for move in moves:
                    state_new = press_key(state, move, 0)
                    
                    if state_new == None:
                        continue
                    # print(state_new)
                    # input(f"Press Enter to continue...")
                    if state_new[0] > 0:
                        if state_new[3] == c: # correct char has been found
                            print(f"Character {c} has been reached in {cost} moves, the moves were: {state_new[2]}")
                            return
                        if state_new[2] == "<vA<AA>>^A": # "<vA<AA>>^AvAA<^A>A":
                            print(f"BIG SUCCESS!")
                            return
                        if state_new[3] != '':
                            continue
                        pq.put(state_new)

                    
def press_key(state, move, level):
    # pointers = [(0,2), (0,2), (3,2)]
    # state = [cost, pointers, gibberish, typed]
    ultimate_pads = [['x^A', '<v>'], ['x^A', '<v>'], ['789', '456', '123', 'x0A']]

    pads = ultimate_pads[level:]
    cost = state[0]
    pointers = state[1][level:]
    gibberish = state[2]
    typed = state[3]

    if level == 0:
        cost += 1
    if move == 'A':
        # input(f"entering A for {state} {move} {level}")
        if level == 0:
            gibberish += 'A'
            # input(f"appending gibberish")
        if level + 2 == len(ultimate_pads):
            typed = pads[1][pointers[1][0]][pointers[1][1]]
            state_new = [cost, state[1], gibberish, typed]
            return state_new
        # input(f"level is {level}")
        next_move_loc = pointers[0] # (e.g. (1,1))
        # input(f"next_move_loc is {next_move_loc}")
        next_move = pads[0][next_move_loc[0]][next_move_loc[1]]
        # input(f"next_move is {next_move}")
        state_new = [cost, state[1], gibberish, typed]
        # input(f"state_new is {state_new}, next_move is {next_move}, next level is {level+1}")
        return press_key(state_new, next_move, level + 1)
    
    moves_alp = ['<', '>', 'v', '^']
    moves_num = [(0,-1), (0,1), (1,0), (-1,0)]

    dir = moves_num[moves_alp.index(move)]

    target = tuple(map(sum, zip(pointers[0], dir)))

    # input(f"target is {target}")
    if is_in_grid(pads[0], target):
        if level == 0:
            gibberish += move

        new_pointers = copy.deepcopy(state[1])
        new_pointers[level] = target
        new_state = [cost, new_pointers, gibberish, typed]
        # input(f"{new_state}")
        return new_state
    return None

def find_character_location(pad, char):
    for row_idx, row in enumerate(pad):
        for col_idx, col_char in enumerate(row):
            if col_char == char:
                return (row_idx, col_idx)

if __name__ == "__main__":
    main()