def is_valid_arrangement(logs, nums):
    comparison_list = []
    count = 0
    for log in logs:
        if len(comparison_list) > len(nums) or comparison_list != nums[:len(comparison_list)]:
            return 0
        if log == '#':
            count += 1
        else:
            if count != 0:
                comparison_list.append(count)
            count = 0
    comparison_list.append(count)
    comparison_list = [x for x in comparison_list if x != 0]
    if comparison_list == nums:
        return 1
    else:
        return 0

def count_valid_arrangement(logs, nums):
    
    from itertools import product

    total = 0
    count = 0
    q_mark = logs.count('?')
    groups = list(product('#.', repeat=q_mark))

    for group in groups:
        temp = []
        k = 0
        for j in range(len(logs)):
            if logs[j] == '?':
                temp.append(group[k])
                k += 1
            else:
                temp.append(logs[j])
        total = is_valid_arrangement(temp, nums)
        count += total
    return count

def main():
    file_path = "input.txt"
    valid = 0
    with open(file_path, 'r') as file:
        for line in file:
            logs, part2 = line.split()
            logs = list(logs)
            nums = list(map(int, part2.split(",")))
            valid += count_valid_arrangement(logs, nums)
    print (valid)

if __name__ == "__main__":
    main()