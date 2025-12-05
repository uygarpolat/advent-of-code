def parseFile(filepath: str):

    with open(filepath) as f:
        initial_ranges, initial_targets = f.read().strip().split("\n\n")

    ranges = [(int(start), int(end)) for line in initial_ranges.splitlines() for start, end in [line.split("-")]]
    targets = [int(line) for line in initial_targets.splitlines()]
    return ranges, targets


def main():

    filepath = "input.txt"
    ranges, targets = parseFile(filepath)

    result1 = 0
    result2 = 0
    prev = 0
    temp_for_result2 = 0
    ranges.sort(key=lambda x: (x[0], x[1]))

    for target in targets:
        for start, end in ranges:

            if not result2:
                new_start = max(start, prev)
                temp_for_result2 += max(0, end - new_start + 1)
                prev = max(prev, end + 1)

            if start <= target <= end:
                result1 += 1
                if result2:
                    break

        result2 = temp_for_result2

    print(f"Solution for Part 1: {result1}")
    print(f"Solution for Part 2: {result2}")


if __name__ == "__main__":
    main()
