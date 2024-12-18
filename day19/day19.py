import operator

def main():
    file_path = "input2.txt"
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
    print(workflows)
    print(parts)

    result = execute_workflow(workflows['px'][1], parts[0])
    print(result)

def execute_workflow(workflow, part):
    print(f"workflow is {workflow} and part is {part}")
    if workflow == 'A':
        return 2
    elif workflow == 'R':
        return -1
    elif ':' not in workflow:
        return workflow
    else:
        comparison, target = workflow.split(':')
        result = evaluate_comparison(comparison, part)
        if result:
            return target
        else:
            return 0

def evaluate_comparison(comparison, part):
    # 'a<2006'    and     [2127, 1623, 2188, 1013]
    operators = {
    '>': operator.gt,
    '<': operator.lt,
    }
    xmas = ['x', 'm', 'a', 's']

    op_func = operators.get(comparison[1])
    source_to_compare, num = comparison.split(comparison[1])
    target_to_compare = xmas.index(source_to_compare)
    print(f"operator is {op_func}, first part is {part[target_to_compare]}, second part is {int(num)}")
    return op_func(part[target_to_compare], int(num))


if __name__ == "__main__":
    main()