from collections import defaultdict

def main():
    file_path = "input.txt"
    modules = {}
    with open(file_path, 'r') as file:
        for line in file:
            definition, targets = line.strip().split('->')
            compressed = [definition[0], 'off' if definition[0] == '%' else defaultdict(lambda: 'low')]
            compressed.extend([c.strip() for c in targets.strip().split(',')])
            modules[definition[1:].strip()] = compressed
        modules["broadcaster"] = modules["roadcaster"]
        modules["broadcaster"][0] = "broadcaster"
        del modules["roadcaster"]

    populate_conjunction_inputs(modules)

    print(modules['df'])

    low_pulse_count = 0
    high_pulse_count = 0
    solution_part_two = 1

    target_keyword = 'rx'
    for key, value in modules.items():
        if target_keyword in modules[key]:
            source_keyword = key

    i = 0
    dict_saver = []

    while True:
        targets = []
        for destination in modules["broadcaster"][2:]:
            targets.append([destination, "low", "broadcaster"])
            low_pulse_count += 1
        low_pulse_count += 1

        while targets:
            lookup = list(modules[source_keyword][1].values())
            if 'high' in lookup:
                if lookup not in dict_saver:
                    dict_saver.append(lookup)
                    solution_part_two *= i+1
                    if len(dict_saver) == len(lookup):
                        print(f"Solution for Part 2: {solution_part_two}")
                        return
            targets, flag = send_signals(modules, targets, target_keyword)
  
            for target in targets:
                if 'low' in target:
                    low_pulse_count += 1
                elif 'high' in target:
                    high_pulse_count += 1
        i += 1
        if i == 1000:
            print(f"Solution for Part 1: {low_pulse_count * high_pulse_count}")

def print_fancy(targets):
    for target in targets:
        print(f"{target[2]} -{target[1]}-> {target[0]}")

def send_signals(modules, targets, keyword):
    flag = False
    new_targets = []
    for target in targets:
        if target[0] == keyword:
            continue
        if modules[target[0]][0] == '%' and target[1] != 'high':
            target = send_flipflop(modules, target)
            new_targets.extend(target)
        elif modules[target[0]][0] == '&':
            target = send_conjunction(modules, target)
            new_targets.extend(target)
    return new_targets, flag

def send_flipflop(modules, target):
    new_target = []
    if modules[target[0]][1] == 'off':
        modules[target[0]][1] = 'on'
        pulse = 'high'
    else:
        modules[target[0]][1] = 'off'
        pulse = 'low'
    for destination in modules[target[0]][2:]:
        new_target.append([destination, pulse, target[0]])
    return new_target

def send_conjunction(modules, target):
    new_target= []
    modules[target[0]][1][target[2]] = target[1]
    if 'low' in modules[target[0]][1].values():
        pulse = 'high'
    else:
        pulse = 'low'
    for destination in modules[target[0]][2:]:
        new_target.append([destination, pulse, target[0]])
    return new_target

def populate_conjunction_inputs(modules):
    for key, value in modules.items():
        value = value[2:]
        for val in value:
            if val in modules and modules[val][0] == '&':
                modules[val][1][key] = 'low'

if __name__ == "__main__":
    main()