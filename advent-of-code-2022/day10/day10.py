from collections import defaultdict


def main():
    filepath = "input.txt"
    with open(filepath, "r") as f:
        nums = [0]
        for line in f:
            amount = 0
            if " " in line:
                amount = int(line.strip().split()[1])
            nums.append(amount)

    result = 1
    time = 0
    book = defaultdict(int)
    for num in nums:
        time += 1
        book[time] = result
        if num:
            time += 1
        result += num
        book[time] = result

    print(f"Solution for Part 1: {sum(i * book[i] for i in range(20, 221, 40))}")


if __name__ == "__main__":
    main()
