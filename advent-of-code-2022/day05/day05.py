import re
import copy

def main():
    filepath = "input.txt"
    containers = ['_', 'GJZ', 'CVFWPRLQ', 'RGLCMPF', 'MHPWBFL', 'QVSFCG', 'LTQMZJHW', 'VBSFH', 'SZJF', 'TBHFPDCM']
    stack = create_stack(containers)
    stack2 = copy.deepcopy(stack)

    part_one = True
    with open(filepath, 'r') as file:
        for line in file:
            if not line.strip():
                part_one = False
                continue
            if part_one:
                continue
            new_line = re.sub(r'[a-zA-Z]', ' ', line)
            procedure = [int(x) for x in new_line.split()]
            execute_procedure(stack, procedure)
            execute_procedure_2(stack2, procedure)

    print(f"Solution for Part 1: {display_result(stack)}")
    print(f"Solution for Part 2: {display_result(stack2)}")

def display_result(stack):
    result = ""
    for s in stack:
        result += s[0]
    return result[1:]
    
def execute_procedure(stack, procedure):
    for i in range(procedure[0]):
        stack[procedure[2]].insert(0, stack[procedure[1]][0])
        stack[procedure[1]].pop(0)

def execute_procedure_2(stack, procedure):
    length = procedure[0]
    source_sliced = stack[procedure[1]][:length]
    stack[procedure[1]] = stack[procedure[1]][length:]
    source_sliced.extend(stack[procedure[2]])
    stack[procedure[2]] = source_sliced

def create_stack(containers):
    stack = []
    for container in containers:
        temp = []
        for c in container:
            temp.extend(c)
        stack.append(temp)
    return stack

if __name__ == "__main__":
    main()