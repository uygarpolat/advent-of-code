def main():
    filepath = "input.txt"
    with open(filepath, 'r') as file:
        input = file.read()
    for part_no, size in enumerate((4, 14), start=1):
        get_marker(input, size, part_no)
    
def get_marker(input, marker_size, part_no):
    for i, c in enumerate(input):
        if i < marker_size - 1:
            continue
        target = input[i-(marker_size - 1):i+1]
        if len(target) == len(set(target)):
            print(f"Solution for Part {part_no}: {i+1}")
            break

if __name__ == "__main__":
    main()