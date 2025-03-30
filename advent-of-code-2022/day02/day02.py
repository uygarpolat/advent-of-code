def main():
    filepath = "input.txt"
    score = 0
    collusion = 0
    with open(filepath, 'r') as file:
        for line in file:
            left, right = line.strip().split()
            score += calculate_score(left, right)
            collusion += calculate_collusion(left, right)
    print(f"Solution for Part 1: {score}")
    print(f"Solution for Part 2: {collusion}")

def calculate_collusion(left, right):
    left_table = ['A', 'B', 'C']
    right_table = ['X', 'Y', 'Z']
    left_index = left_table.index(left)
    right_index = right_table.index(right)

    if right_index == 1:
        score = 3 + left_index + 1
    elif right_index == 2:
        score = 6 + ((left_index + 1) % 3) + 1
    else:
        score = 0 + ((left_index - 1) % 3) + 1
    return score

def calculate_score(left, right):

    left_table = ['A', 'B', 'C']
    right_table = ['X', 'Y', 'Z']
    left_index = left_table.index(left)
    right_index = right_table.index(right)
    score = right_index + 1

    if left_index == right_index:
        score += 3
    elif left_index + right_index != 2:
        if right_index == max(left_index, right_index):
            score += 6
    elif right_index == min(left_index, right_index):
        score += 6
    return score

if __name__ == "__main__":
    main()