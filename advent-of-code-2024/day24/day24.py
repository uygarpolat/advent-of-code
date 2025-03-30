from queue import PriorityQueue

def main():
    file_path = "input.txt"
    system = {}
    with open(file_path, 'r') as file:
        phase1, phase2 = file.read().strip().split('\n\n')
        for line in phase1.split('\n'):
            key, value = line.strip().split(':')
            system[key] = []
            system[key].append(int(value.strip()))
            system[key].append(['None'])
        for line in phase2.split('\n'):
            three_values, target = line.strip().split(' -> ')
            source1, logical, source2 = three_values.strip().split()
            if target not in system:
                system[target] = []
            system[target].append(-1)
            system[target].append([source1, logical, source2])

    # swap_wires(system, 'z34', 'wrc')
    # swap_wires(system, 'nnf', 'z09')
    # swap_wires(system, 'z20', 'nhs')
    # swap_wires(system, 'ddn', 'kqh')

    num_x = get_decimal(system, 'x')
    num_y = get_decimal(system, 'y')
    ultimate_target = num_x + num_y

    pq = PriorityQueue()
    populate_queue(system, pq)

    while not pq.empty():
        target = pq.get()
        logical_operation(system, target)
        populate_queue(system, pq)
    
    result = get_decimal(system, 'z')
    print(f"Solution for Part 1: {result}")

    ultimate_target_binary = bin(ultimate_target)[2:]
    result_binary = bin(result)[2:]

    wrong_z_list = []
    affected = set()
    unaffected = set()
    for i in range(len(ultimate_target_binary) - 1, -1 , -1):
        if len(ultimate_target_binary) - i - 1 < 10:
            word = 'z0'
        else:
            word = 'z'
        final_product = word + str(len(ultimate_target_binary) - i - 1)

        if ultimate_target_binary[i] != result_binary[i]:
            wrong_z_list.append(final_product)
            chopped_list = system[final_product][1][:1] + system[final_product][1][2:] 
            for val in chopped_list:
                if val.startswith('x') or val.startswith('y'):
                    continue
                affected.add(val)
        else:
            chopped_list = system[final_product][1][:1] + system[final_product][1][2:]
            for val in chopped_list:
                if val.startswith('x') or val.startswith('y'):
                    continue
                unaffected.add(val)
    # print(f"Discrepany count and culprits: {len(wrong_z_list)}: {wrong_z_list}")
    # print(affected)
    # print(len(affected))

def swap_wires(system, wire1, wire2):
    temp = system[wire1]
    system[wire1] = system[wire2]
    system[wire2] = temp

def get_decimal(system, keyword):
    system = dict(sorted(system.items(), reverse=True))
    binary_string = ""
    for key, value in system.items():
        if key.startswith(keyword):
            binary_string += str(value[0])
    return int(binary_string, 2)

def logical_operation(system, target):
    source1 = system[target][1][0]
    logical = system[target][1][1]
    source2 = system[target][1][2]
    source1_val = system[source1][0]
    source2_val = system[source2][0]
    if logical == 'AND':
        system[target][0] = int(source1_val and source2_val)
    elif logical == 'OR':
        system[target][0] = int(source1_val or source2_val)
    elif logical == 'XOR':
        system[target][0] = int(source1_val != source2_val)

def populate_queue(system, pq):
    contents_of_queue = list(pq.queue)
    for key in system.keys():
        if key in contents_of_queue:
            continue
        current_val = system[key][0]
        if system[key][1][0] == 'None':
            continue
        source1 = system[key][1][0]
        source2 = system[key][1][2]
        if current_val < 0 and system[source1][0] >=0 and system[source2][0] >= 0:
            pq.put(key)

if __name__ == "__main__":
    main()