from queue import PriorityQueue
import copy
from collections import defaultdict

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
        finality = [line.strip() for line in file]

    finality = [[char] for char in finality[0]]

    moves = ['<', '>', 'v', '^', 'A']
    numpad_pointer = (3,2)
    keypad_pointer = (0,2)
    pointers = [keypad_pointer]

    for mmm in range(25):

        if mmm == 0:
            pointers = [numpad_pointer]
        else:
            pointers = [keypad_pointer]

        sequences2 = finality

        finality = []

        for sequence in sequences2:

            info_of_alternatives = defaultdict(lambda: 0)
            
            for i, member in enumerate(sequence):

                tabulation = []

                for c in member:

                    typed = ""
                    gibberish = ""
                    move = ""
                    cost = 0
                    state = [cost, pointers, gibberish, typed]
                    pq = PriorityQueue()
                    pq.put(state)
                    sub_tabulation = []
                    big_cost = 1000000000000
                    while not pq.empty():

                        state = pq.get()

                        for move in moves:
                            state_new = press_key_two_keypads(state, move, mmm, 0)
                            if state_new == None:
                                continue
                            if state_new[3] != '' and state_new[3] != c:
                                continue
                            if state_new[3] == c:
                                if big_cost == 1000000000000:
                                    pointers = state_new[1]
                                if state_new[0] <= big_cost:
                                    pointers = state_new[1]
                                    big_cost = state_new[0]
                                    sub_tabulation.append(state_new[2])
                                else:
                                    while not pq.empty():
                                        pq.get()
                                    break
                            pq.put(state_new)

                    tabulation.append(sub_tabulation)

                info_of_alternatives[i] = tabulation
            int_check = 10000000000
            indexx = 0
            for key, value in info_of_alternatives.items():
                count = 0
                for val in value:
                    # for cal in val:
                    count += len(val[0])
                if int_check > count:
                    int_check = count
                    indexx = key
            finality.extend(info_of_alternatives[indexx])
        count = 0
        for dal in finality:
            count += len(dal[0])

def press_key_two_keypads(state, move, mmm, level):

    if mmm == 0:
        pad = ['789', '456', '123', 'x0A']
    else:
        pad = ['x^A', '<v>']
    ultimate_pads = [pad]

    pads = ultimate_pads[level:]
    cost = state[0]
    pointers = state[1][level:]
    gibberish = state[2]
    typed = state[3]

    cost += 1
    if move == 'A':
        gibberish += 'A'
        typed = pads[0][pointers[0][0]][pointers[0][1]]
        state_new = [cost, state[1], gibberish, typed]
        return state_new

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

if __name__ == "__main__":
    main()