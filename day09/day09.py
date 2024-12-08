
# compile with python3.10 day09.py

import numpy as np

def is_there_a_pattern(nums, flag):
    numbers = np.diff(nums).tolist()
    pattern = numbers[1] - numbers[0]
    if not all(numbers[i + 1] - numbers[i] == pattern for i in range(len(numbers) - 1)):
        pattern = is_there_a_pattern(numbers, flag)
    return numbers[(len(numbers) - 1 + flag) % len(numbers)] + (1 - 2 * flag) * pattern

def main():
    file_path = "input.txt"
    for i in range(2):
        with open(file_path, 'r') as file:
            total = 0
            for line in file:
                nums = list(map(int, line.split()))
                extension_pos = nums[(len(nums) - 1 + i) % len(nums)] + (1 - 2 * i) * is_there_a_pattern(nums, i)
                total += extension_pos
        print(f"Solution for part {i+1}: {total}")

if __name__ == "__main__":
    main()