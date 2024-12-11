from functools import lru_cache
from collections import defaultdict

@lru_cache(None)
def execute_move_two(stone):
    stone_str = str(stone)
    half_len = len(stone_str) // 2
    left = int(stone_str[:half_len])
    right = int(stone_str[half_len:])
    return (left, right)

def execute_changes(stones):
    next_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            next_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            left, right = execute_move_two(stone)
            next_stones[left] += count
            next_stones[right] += count
        else:
            next_stones[stone * 2024] += count
    return next_stones

def main():
    blinks = [25, 75]
    for i in range(2):
        stones = {27: 1, 10647: 1, 103: 1, 9: 1, 0: 1, 5524: 1, 4594227: 1, 902936: 1}
        total_stones = 0
        for i in range(blinks[i]):
            stones = execute_changes(stones)
        total_stones = sum(stones.values())
        print(f"Solution for Part {i+1}: {total_stones}")

if __name__ == "__main__":
    main()