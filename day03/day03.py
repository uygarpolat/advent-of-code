from collections import Counter

def main():
    filepath = "input.txt"
    priority_1 = 0
    priority_2 = 0
    joined = ""
    with open(filepath, 'r') as file:
        for i, line in enumerate(file):
            joined += "".join(set(line.strip()))
            if i % 3 == 2:
                priority_2 += calculate_priority(find_triple_repeating_char(joined))
                joined = ""
            
            length = len(line.strip())
            left = line[:length//2]
            right = line[length//2:].strip()
            for c in left:
                if c in right:
                    priority_1 += calculate_priority(c)
                    break
        
    print(f"Solution for Part 1: {priority_1}")
    print(f"Solution for Part 2: {priority_2}")

def calculate_priority(c):
    priority = 0
    priority += ord(c.lower()) - ord('a') + 1
    if c.isupper():
        priority += 26
    return priority

def find_triple_repeating_char(s):
    char_count = Counter(s)
    for char, count in char_count.items():
        if count == 3:
            return char

if __name__ == "__main__":
    main()