def parse_file(file_path, file):
    first_section = []
    second_section = []
    in_first_section = True

    for line in file:
        line = line.strip()
        if in_first_section and line == "":
            in_first_section = False
            continue
        
        if in_first_section:
            parts = line.split('|')
            first_section.append((int(parts[0]), int(parts[1])))
        else:
            numbers = list(map(int, line.split(',')))
            second_section.append(numbers)
    
    return first_section, second_section

def create_dict_from_tuples(tuples_list):
    result_dict = {}
    for first, second in tuples_list:
        if second not in result_dict:
            result_dict[second] = []
        result_dict[second].append(first)
    return result_dict

def check_order(current, target, first_section_dict):
    if not current in first_section_dict:
        return 0
    elif target in first_section_dict[current]:
        return 1
    return 0

def correct_the_order(sublist, first_section_dict):
    for i in range(len(sublist) - 1, 0, -1):
        for j in range(i):
            if check_order(sublist[i - j - 1], sublist[i], first_section_dict):
                temp = sublist[i - j - 1]
                sublist[i - j - 1] = sublist[i]
                sublist[i] = temp
    return sublist[len(sublist) // 2]

def main():

    file_path = "input.txt"
    with open(file_path, 'r') as file:
        first_section, second_section = parse_file(file_path, file)
    first_section_dict = create_dict_from_tuples(first_section)

    total = 0
    total_wrong = 0
    for sublist in second_section:
        flag = 0
        for i in range(len(sublist)):
            for j in range(i + 1, len(sublist)):
                flag = check_order(sublist[i], sublist[j], first_section_dict)
                if flag == 1:
                    total_wrong += correct_the_order(sublist, first_section_dict)
                    break
            if flag == 1:
                break
        if flag == 0:
            total += sublist[len(sublist) // 2]
    print (f" Answer for the first part: {total}")
    print (f"Answer for the second part: {total_wrong}")

if __name__ == "__main__":
    main()