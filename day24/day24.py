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
    # for key, value in system.items():
    #     print(f"system[{key}] = {value}")

    pq = PriorityQueue()
    populate_queue(system, pq)

    while not pq.empty():
        target = pq.get()
        logical_operation(system, target)
        populate_queue(system, pq)
    
    print(f"Solution for Part 1: {get_decimal(system)}")

def get_decimal(system):
    system = dict(sorted(system.items(), reverse=True))
    binary_string = ""
    for key, value in system.items():
        if key.startswith('z'):
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