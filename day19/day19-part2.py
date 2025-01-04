from copy import deepcopy

def main():
    file_path = "input.txt"
    workflows = {}
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                break
            part1, part2 = line.strip().split('{')
            conditions = part2.rstrip('}').split(',')
            workflows[part1] = conditions

    initial_ranges = {
        'x': (1, 4000),
        'm': (1, 4000),
        'a': (1, 4000),
        's': (1, 4000)
    }
    
    total = process_workflow('in', initial_ranges, workflows)
    print(f"Solution for Part 2: {total}")

def process_workflow(workflow_name, ranges, workflows):
    if workflow_name == 'R':
        return 0
    if workflow_name == 'A':
        product = 1
        for low, high in ranges.values():
            product *= max(0, high - low + 1)
        return product

    total = 0
    current_ranges = deepcopy(ranges)
    
    for rule in workflows[workflow_name]:
        if ':' not in rule:
            total += process_workflow(rule, current_ranges, workflows)
            break
            
        condition, next_workflow = rule.split(':')
        rating = condition[0]
        operator_char = condition[1]
        value = int(condition[2:])
        
        passed_ranges = deepcopy(current_ranges)
        if operator_char == '<':
            passed_ranges[rating] = (current_ranges[rating][0], min(value - 1, current_ranges[rating][1]))
            current_ranges[rating] = (max(value, current_ranges[rating][0]), current_ranges[rating][1])
        else:
            passed_ranges[rating] = (max(value + 1, current_ranges[rating][0]), current_ranges[rating][1])
            current_ranges[rating] = (current_ranges[rating][0], min(value, current_ranges[rating][1]))
        
        total += process_workflow(next_workflow, passed_ranges, workflows)
        
        if current_ranges[rating][0] > current_ranges[rating][1]:
            break
            
    return total

if __name__ == "__main__":
    main()