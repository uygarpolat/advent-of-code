from itertools import cycle
import math
from functools import reduce

def parse_file(file_path):
    second_part = False
    with open(file_path, 'r') as file:
        nodes = {}
        for line in file:
            line = line.strip()
            if not second_part:
                if line == "":
                    second_part = True
                    continue
                else:
                    dirs = line
            else:
                parts = line.split("=")
                one, two = parts[1].rstrip(" )").lstrip(" (").split(",")
                nodes[parts[0].rstrip()] = [one, two.lstrip()]
        return dirs, nodes

def traverse_map(dirs, nodes, start):
    count = 0
    while (True):
        for c in cycle(dirs):
            if c == 'L':
                start = nodes[start][0]
            elif c == 'R':
                start = nodes[start][1]
            count += 1
            if start[2] == "Z":
                return count

def main():
    file_path = "input.txt"
    dirs, nodes = parse_file(file_path)
    count = traverse_map(dirs, nodes, "AAA")
    print("Part 1 solution:", count)

    keys = list(nodes.keys())
    keys_A = [key for key in keys if key[2] == 'A']

    numbers = [int(count)]
    for key in keys_A:
        numbers.append(int(traverse_map(dirs, nodes, key)))
    def lcm(a, b):
        return a * b // math.gcd(a, b)
    result = reduce(lcm, numbers)

    print("Part 2 solution:", result)

if __name__ == "__main__":
    main()