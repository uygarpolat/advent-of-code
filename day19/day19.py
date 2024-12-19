def main():
    file_path = "input.txt"

    with open(file_path, 'r') as file:
        patterns, designs = file.read().split('\n\n')
        patterns = [p.strip() for p in patterns.split(',')]
        designs = designs.split('\n')

    longest_element = max(patterns, key=len)
    res = 0
    for i, design in enumerate(designs):
        if slice_and_solve(design, patterns, longest_element):
            res += 1
    print(f"Solution for Part 1: {res}")

def slice_and_solve(design, patterns, longest_element):
    if design == "":
        return True
    for i in range(0, len(longest_element), 1):
        if design[:i+1] in patterns:
            if slice_and_solve(design[i+1:], patterns, longest_element):
                return True
    return False

if __name__ == "__main__":
    main()