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
    from itertools import combinations

    needed_hashes = sum(nums) - logs.count('#')
    q_mark_positions = [i for i, ch in enumerate(logs) if ch == '?']
    if needed_hashes < 0 or needed_hashes > len(q_mark_positions):
        return 0

    count = 0
    for hash_positions_subset in combinations(q_mark_positions, needed_hashes):
        temp = logs[:]
        for i in q_mark_positions:
            temp[i] = '#' if i in hash_positions_subset else '.'

        if is_valid_arrangement(temp, nums) == 1:
            count += 1
    return count

# first draft of this function
# def count_valid_arrangement(logs, nums):
    
#     from itertools import product

#     total = 0
#     count = 0
#     q_mark = logs.count('?')
#     print("waiting")
#     groups = [p for p in product('#.', repeat=q_mark) if p.count('#') == sum(nums) - logs.count('#')]

#     print(groups)

#     for group in groups:
#         temp = []
#         k = 0
#         for j in range(len(logs)):
#             if logs[j] == '?':
#                 temp.append(group[k])
#                 k += 1
#             else:
#                 temp.append(logs[j])
#         total = is_valid_arrangement(temp, nums)
#         count += total
#     return count

def main():
    file_path = "input.txt"
    valid = 0
    valid_extended = 0
    with open(file_path, 'r') as file:
        i = 1
        for line in file:
            logs, part2 = line.split()
            logs = list(logs)
            nums = list(map(int, part2.split(",")))
            copies = 5
            extended_logs = [item for i in range(copies) for item in (logs if i == copies - 1 else logs + ['?'])]
            extended_nums = nums * 5

            valid += count_valid_arrangement(logs, nums)
            # valid_extended += count_valid_arrangement(extended_logs, extended_nums)
            print(f"Line {i} done...")
            i += 1
        print(f"Solution for Part 1: {valid}")
        # print(f"Solution for Part 2: {valid_extended}")

if __name__ == "__main__":
    main()