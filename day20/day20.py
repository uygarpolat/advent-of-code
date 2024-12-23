from collections import defaultdict

def main():
    file_path = "input3.txt"
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

    for _ in range(100):
        targets = []
        for destination in modules["broadcaster"][2:]:
            targets.extend([(destination, "low", "broadcaster")])
        print_fancy(targets)

        while targets:
            targets = send_signals(modules, targets)
            print_fancy(targets)
        input("Enter...")

def print_fancy(targets):
    for target in targets:
        print(f"{target[2]} -{target[1]}-> {target[0]}")

def send_signals(modules, targets):
    new_targets = []
    for target in targets:
        if target[0] == "output":
            continue
        if modules[target[0]][0] == '%' and target[1] != 'high':
            target = send_flipflop(modules, target)
            new_targets.append(target)
        elif modules[target[0]][0] == '&':
            target = send_conjunction(modules, target)
            new_targets.append(target)
    return new_targets

def send_flipflop(modules, target):
    new_target = []
    if modules[target[0]][1] == 'off':
        modules[target[0]][1] = 'on'
        pulse = 'high'
    else:
        modules[target[0]][1] = 'off'
        pulse = 'low'
    for destination in modules[target[0]][2:]:
        new_target.extend([destination, pulse, target[0]])
    return new_target

def send_conjunction(modules, target):
    new_target= []
    modules[target[0]][1][target[2]] = target[1]
    if 'low' in modules[target[0]][1].values():
        pulse = 'high'
    else:
        pulse = 'low'
    for destination in modules[target[0]][2:]:
        new_target.extend([destination, pulse, target[0]])
    return new_target

if __name__ == "__main__":
    main()