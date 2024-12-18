import operator

def main():
    file_path = "input.txt"
    second_part = False
    workflows = {}
    parts = {}
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                second_part = True
                continue
            if not second_part:
                part1, part2 = line.strip().split('{')
                conditions = part2.rstrip('}').split(',')
                workflows[part1] = conditions
            else:
                ratings = line.strip('{}\n').split(',')
                next_key = len(parts)
                for rating in ratings:
                    parts.setdefault(next_key, []).append(int(rating.strip('xmas=')))

    counter = 0
    for part in parts.values():
        specific = "in"
        result = 'X'
        while result != 'A' and result != 'R':
            i = 0
            while i < len(workflows[specific]):
                result = execute_workflow(workflows[specific][i], part)
                if result == 'A' or result == 'R':
                    break
                elif result == 0:
                    i += 1
                else:
                    i = 0
                    specific = result
        if result == 'A':
            counter += sum(part)
    print(counter)

def execute_workflow(workflow, part):
    if ':' in workflow:
        comparison, target = workflow.split(':')
        if evaluate_comparison(comparison, part):
            return target
        else:
            return 0
    return workflow

def evaluate_comparison(comparison, part):
    operators = {
    '>': operator.gt,
    '<': operator.lt,
    }
    xmas = ['x', 'm', 'a', 's']

    op_func = operators.get(comparison[1])
    source_to_compare, num = comparison.split(comparison[1])
    target_to_compare = xmas.index(source_to_compare)
    return op_func(part[target_to_compare], int(num))

if __name__ == "__main__":
    main()