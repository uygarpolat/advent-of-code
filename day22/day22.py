from collections import defaultdict

def calculate_secret(num):
    mod = 16777216
    num = (num ^ (num * 64)) % mod
    num = (num ^ (num // 32)) % mod
    num = (num ^ (num * 2048)) % mod
    num_one = num % 10
    return num, num_one

def main():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    tally = defaultdict(lambda: 0)
    iteration = 2000
    result = 0
    tally = []

    for i, number in enumerate(numbers):
        tally.append(defaultdict(lambda: 0))
        listing = ()
        previous_number_one = number % 10
        for _ in range(iteration):
            number, current_number_one = calculate_secret(number)
            change = current_number_one - previous_number_one
            listing = listing[-3:] + (change, )
            if listing not in tally[i]:
                tally[i][listing] = current_number_one
            previous_number_one = current_number_one
        result += number

    print(f"Solution for Part 1: {result}")

    global_sum = defaultdict(int)
    for d in tally:
        for k, v in d.items():
            global_sum[k] += v
    best_result = max(global_sum.values())
    print(f"Solution for Part 2: {best_result}")

if __name__ == "__main__":
    main()