from itertools import combinations
from collections import Counter

def main():
    file_path = "input.txt"
    network = {}
    with open(file_path, 'r') as file:
        for line in file:
            part1, part2 = line.strip().split('-')
            if not part1 in network:
                network[part1] = []
            network[part1].append(part2)
            if not part2 in network:
                network[part2] = []
            network[part2].append(part1)

    starts_with_t = {key for key in network.keys() if key.startswith('t')}
    three_combos = []
    for combo in combinations(network.keys(), 3):
        if any(c in starts_with_t for c in combo):
            three_combos.append(combo)

    result = 0
    for combo in three_combos:
        count = 0
        for i, c in enumerate(combo):
            if combo[(i+1) % len(combo)] in network[c] and combo[(i+2) % len(combo)] in network[c]:
                count += 1
        if count == 3:
            result += 1
    print(f"Solution for Part 1: {result}")

    solution_part_two = calculate_biggest_lan(network)
    print(f"Solution for Part 2: {solution_part_two}")

def calculate_biggest_lan(network):
    max_global = 0
    max_list = []
    for key, values in network.items():
        current_lan = []
        current_lan.extend(values)
        for value in values:
            current_lan.append(value)
            current_lan.extend(network[value])
        freq = sorted(Counter(current_lan).values(), reverse=True)

        max_value = max(freq)
        recurrence_count = freq.count(max_value)

        if max_global < recurrence_count:
            max_list = [key]
            max_global = recurrence_count
        elif max_global == recurrence_count:
            max_list.append(key)
            
    return ','.join(sorted(max_list))

if __name__ == "__main__":
    main()