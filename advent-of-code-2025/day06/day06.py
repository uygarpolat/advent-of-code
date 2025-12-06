from operator import mul, add
from functools import reduce


def parse_file(filepath):
    book1 = []
    book2 = []
    operations = []
    with open(filepath, "r") as f:
        for line in f:
            if not "*" in line and not "+" in line:
                book1.append(list(map(int, line.strip().split())))
                book2.append(line.strip("\n"))
            else:
                operations = list(line.strip().split())
    book1 = list(zip(*book1[::-1]))
    book2 = list(zip(*book2))[::-1]
    return book1, book2, operations


def main():

    filepath = "input.txt"
    book1, book2, operations = parse_file(filepath)
    result1 = 0
    ops = {"*": mul, "+": add}
    for i, nums in enumerate(book1):
        result1 += reduce(ops[operations[i]], nums, operations[i] == "*")

    print(f"Solution for Part 1: {result1}")

    op_index = len(operations) - 1
    result2 = 0
    local_result = operations[op_index] == "*"

    for book in book2:
        if all(x == " " for x in book):
            result2 += local_result
            local_result = operations[op_index := op_index - 1] == "*"
        else:
            local_result = ops[operations[op_index]](local_result, int("".join(book)))

    result2 += local_result
    print(f"Solution for Part 2: {result2}")


if __name__ == "__main__":
    main()
