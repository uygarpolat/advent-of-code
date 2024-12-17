def main():
    file_path = "input2.txt"
    second_part = False
    workflows = {}
    parts = {}
    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                second_part = True
                continue
            if not second_part:
                part1, part2 = line.strip().split('{')
                conditions = part2.rstrip('}').split(',')
                workflows[part1] = conditions
            else:
                ratings = line.strip('{}\n').split(',')
                next_key = len(parts)
                for rating in ratings:
                    parts.setdefault(next_key, []).append(int(rating.strip('xmas=')))
    print(workflows)
    print(parts)

if __name__ == "__main__":
    main()