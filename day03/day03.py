from collections import deque


def getMax(line: str, slot: int):
    n = len(line)
    stack = deque()
    for index, c in enumerate(line):
        while stack and stack[-1] < c and slot < n - index:
            stack.pop()
            slot += 1
        if slot:
            stack.append(c)
            slot -= 1
    return int("".join(stack))


def main():
    result1 = 0
    result2 = 0
    with open("input.txt", "r") as f:
        file = f.read()
    for line in file.split("\n"):
        result1 += getMax(line, 2)
        result2 += getMax(line, 12)
    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {result2}")
    return result1, result2


if __name__ == "__main__":
    main()
