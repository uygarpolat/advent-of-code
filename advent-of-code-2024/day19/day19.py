def main():
    file_path = "input.txt"

    with open(file_path, 'r') as file:
        patterns, designs = file.read().split('\n\n')
        patterns = [p.strip() for p in patterns.split(',')]
        designs = designs.split('\n')

    longest_element = max(patterns, key=len)
    result_1 = 0
    result_2 = 0

    for design in designs:
        memo = {}
        res = slice_and_solve(design, patterns, longest_element, memo)
        if res:
            result_1 += 1
            result_2 += res
    print(f"Solution for Part 1: {result_1}")
    print(f"Solution for Part 2: {result_2}")

def slice_and_solve(design, patterns, longest_element, memo):
    if design in memo:
        return memo[design]
    if design == "":
        return 1

    value = 0
    for i in range(1, min(len(longest_element), len(design)) + 1):
        if design[:i] in patterns:
            value += slice_and_solve(design[i:], patterns, longest_element, memo)

    memo[design] = value
    return value

if __name__ == "__main__":
    main()